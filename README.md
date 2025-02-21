# Squash Game

Squash Game is a simple game developed in Python using the **Pygame** library. This project was created as a quick demonstration of basic game mechanics – including controls, animation, collision detection, and scoring logic.

## Description

In this game, you control a paddle using the left/right arrow keys to bounce a moving ball. Each successful bounce earns you a point. If the ball falls below the paddle, a "Game Over" screen displays your final score and offers a restart option (press **SPACE**).

**Note:** This version of the game runs in fullscreen mode and uses a minimalistic graphical style. The focus is on functionality, providing a solid base for further enhancements.

## Features

- **Fullscreen Mode:** The game launches in fullscreen mode using your system's current resolution.
- **Controls:** Move the paddle left and right using the arrow keys.
- **Ball Movement:** The ball moves across the screen, bouncing off walls and the paddle.
- **Scoring:** Each bounce off the paddle increases your score.
- **Game Over:** When the ball is missed, a game over screen displays your score and prompts you to restart (press **SPACE**).
- **Levels:** The game adjusts ball color and paddle size based on your score (three levels in total).
- **Trajectory:** A trajectory is drawn on the screen based on settings for the current level.

## Installation

### Requirements

- **Python 3.x**
- **Pygame** – Install it using:
  ```bash
  pip install pygame
