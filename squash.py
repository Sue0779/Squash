import pygame
import sys

pygame.init()

# --- Ustawienia ekranu i gry ---
# Zamiast stałych szerokości i wysokości, używamy pełnego ekranu.
# Możemy użyć (0, 0) wraz z flagą pygame.FULLSCREEN.
# Ewentualnie pobieramy rozdzielczość ekranu systemowego:
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

FPS = 60

# Tworzymy okno gry w trybie pełnoekranowym
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Squash w Pythonie")

clock = pygame.time.Clock()

# --- Definicje poziomów ---
levels = {
    1: {"ball_color": (255, 0, 0),     # czerwony
        "paddle_width_ratio": 0.15,
        "show_trajectory": True},
    2: {"ball_color": (0, 255, 0),     # zielony
        "paddle_width_ratio": 0.10,
        "show_trajectory": True},
    3: {"ball_color": (255, 255, 255), # biały
        "paddle_width_ratio": 0.10,
        "show_trajectory": False},
}

current_level = 1

# --- Zmienne gry ---
ball_radius = 10
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 12, -12

paddle_height = 20
paddle_speed = 15
paddle_width = int(WIDTH * levels[current_level]["paddle_width_ratio"])
paddle_x = (WIDTH - paddle_width) // 2

score = 0
is_game_over = False
is_paused = False

# Flagi klawiszy
left_pressed = False
right_pressed = False

# Czcionki
font = pygame.font.SysFont(None, 40)
game_over_font = pygame.font.SysFont(None, 60)

def reset_game():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    global score, is_game_over, current_level, is_paused
    global paddle_width, paddle_x

    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_speed_x = 12
    ball_speed_y = -12
    score = 0
    current_level = 1
    is_game_over = False
    is_paused = False

    update_level(current_level)

def update_level(level):
    global current_level, paddle_width
    current_level = level
    paddle_width = int(WIDTH * levels[current_level]["paddle_width_ratio"])

def check_level_change():
    global current_level
    if score >= 200 and current_level < 3:
        update_level(3)
    elif score >= 100 and current_level < 2:
        update_level(2)

def draw_paddle():
    pygame.draw.rect(screen, (255, 255, 255),
                     (paddle_x, HEIGHT - paddle_height - 10,
                      paddle_width, paddle_height))

def draw_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, is_game_over, score

    if not is_paused and not is_game_over:
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Odbicia od boków ekranu
        if ball_x + ball_radius > WIDTH or ball_x - ball_radius < 0:
            ball_speed_x *= -1

        # Odbicie od górnej krawędzi
        if ball_y - ball_radius < 0:
            ball_speed_y *= -1

    color = levels[current_level]["ball_color"]
    pygame.draw.circle(screen, color, (int(ball_x), int(ball_y)), ball_radius)

def draw_trajectory():
    if levels[current_level]["show_trajectory"] is False or is_game_over:
        return

    temp_x = ball_x
    temp_y = ball_y
    temp_speed_x = ball_speed_x
    temp_speed_y = ball_speed_y

    trajectory_points = [(temp_x, temp_y)]

    # Symulacja ruchu piłki, aż przekroczy dolną krawędź
    while True:
        temp_x += temp_speed_x
        temp_y += temp_speed_y

        if temp_x - ball_radius < 0 or temp_x + ball_radius > WIDTH:
            temp_speed_x *= -1
        if temp_y - ball_radius < 0:
            temp_speed_y *= -1

        trajectory_points.append((temp_x, temp_y))

        if temp_y + ball_radius > HEIGHT:
            break

    if len(trajectory_points) > 1:
        pygame.draw.lines(screen, (255, 255, 255), False, trajectory_points, 2)

def draw_score():
    text = font.render(f"Wynik: {score}", True, (0, 255, 0))
    screen.blit(text, (10, 10))

def handle_collisions():
    global ball_speed_y, score, is_game_over

    paddle_y = HEIGHT - paddle_height - 10

    # Kolizja piłki z paletką
    if (ball_y + ball_radius > paddle_y and
        paddle_x < ball_x < paddle_x + paddle_width):
        ball_speed_y *= -1
        score_check()

    # Jeśli piłka wypadnie poza dolną krawędź
    if ball_y - ball_radius > HEIGHT:
        is_game_over = True

def score_check():
    global score
    score += 1
    check_level_change()

def draw_game_over():
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    text = game_over_font.render("Koniec gry!", True, (255, 255, 255))
    score_text = font.render(f"Twój wynik: {score}", True, (0, 255, 0))

    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

    screen.blit(text, text_rect)
    screen.blit(score_text, score_rect)

    sub_text = font.render("Naciśnij SPACJĘ, aby zagrać ponownie", True, (255, 255, 255))
    sub_text_rect = sub_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
    screen.blit(sub_text, sub_text_rect)

def main_loop():
    global left_pressed, right_pressed, paddle_x, is_paused, is_game_over
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_pressed = True
                elif event.key == pygame.K_RIGHT:
                    right_pressed = True
                elif event.key == pygame.K_SPACE:
                    if is_game_over:
                        reset_game()
                    else:
                        is_paused = not is_paused
                elif event.key == pygame.K_ESCAPE:
                    # Wyjście z gry Esc
                    running = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_pressed = False
                elif event.key == pygame.K_RIGHT:
                    right_pressed = False

        screen.fill((0, 0, 0))

        # Ruch paletki (tylko gdy gra nie jest zapauzowana i nie jest zakończona)
        if not is_paused and not is_game_over:
            if left_pressed and paddle_x > 0:
                paddle_x -= paddle_speed
            if right_pressed and paddle_x < WIDTH - paddle_width:
                paddle_x += paddle_speed

        draw_paddle()
        draw_ball()
        draw_trajectory()
        draw_score()
        handle_collisions()

        if is_game_over:
            draw_game_over()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

reset_game()
main_loop()
