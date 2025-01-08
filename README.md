# LineClipper: Visual Line Clipping and Visibility Management

**LineClipper** is an interactive application designed to demonstrate line clipping algorithms. It provides a dynamic environment for visualizing and testing the visibility of lines relative to a defined viewport.

## Key Features
- **Dynamic viewport control:** Move the viewport using arrow keys and observe changes in line visibility.
- **Line visibility visualization:** Visible lines are drawn as solid lines, while hidden segments are displayed as dashed lines.
- **Algorithm flexibility:** Supports implementing and experimenting with different clipping algorithms, such as:
  - Cohen-Sutherland
  - Liang-Barsky
  - Full and partial boundary intersections

## Project Structure
The project is modular for better readability and extensibility:
- **`main.py`** — The main game loop, responsible for rendering and managing input.
- **`viewport.py`** — A class for handling the viewport logic and boundaries.
- **`line.py`** — A class for managing lines, visibility checks, and boundary intersections.
- **`utils.py`** — Utility functions, such as dashed line rendering.

## Requirements
- Python 3.8+
- Pygame 2.0+

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ArtemLyasovich/LineClipper.git
   cd LineClipper
   ```
2. Install dependencies:
   ```bash
   pip install pygame
   ```
3. Usage
To run the application, execute:
   ```bash
   python main.py
   ```

## Controls
Arrow keys (Up, Down, Left, Right): Move the viewport.
Close window: Press Esc or click the window close button.

## Contact
For suggestions or questions, feel free to reach out:
Email: artemlysovich@gmail.com

Created with love for geometry and algorithms 💻❤️
