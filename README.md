# Squash Game

Squash Game to prosta gra stworzona w Pythonie z użyciem biblioteki **Pygame**. Projekt powstał jako szybka demonstracja podstawowych mechanizmów gry – sterowania, animacji, kolizji oraz logiki punktacji.

## Opis

W grze sterujesz paletką za pomocą klawiszy strzałek (lewo/prawo) w celu odbijania poruszającej się piłki. Każde udane odbicie liczy się jako punkt. Gdy piłka spadnie poniżej paletki, gra wyświetla ekran Game Over z wynikiem i możliwością restartu (klawisz **R**).

**Uwaga:** W tej wersji gra wygląda bardzo uproszczonym sposobem – nie ma rozbudowanych efektów wizualnych, trajektorii ruchu piłki czy zaawansowanych animacji. Najważniejsze, że gra działa!

## Funkcje

- **Sterowanie:** Paletka porusza się poziomo przy użyciu klawiszy strzałek.
- **Ruch piłki:** Piłka porusza się po ekranie i odbija od ścian oraz paletki.
- **Punktacja:** Każde odbicie piłki od paletki zwiększa wynik.
- **Game Over:** Po utracie piłki wyświetlany jest ekran końcowy z wynikiem oraz możliwością restartu gry (klawisz **R**).

## Instalacja

### Wymagania

- **Python 3.x**
- **Pygame** – zainstalujesz ją poleceniem:
  ```bash
  pip install pygame
