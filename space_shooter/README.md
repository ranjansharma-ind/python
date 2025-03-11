# Modern Space Shooter

A modern implementation of a space shooter game using Python and Pygame, featuring advanced game development concepts and clean architecture.

## Features

- Object-Oriented Design with abstract base classes and inheritance
- Modern particle system for visual effects
- Physics-based movement with thrust and momentum
- Screen wrapping for infinite space movement
- Type hints for better code maintainability
- Smooth rotation and movement controls
- Efficient collision detection system
- Frame-rate independent movement using delta time

## Technical Highlights

- **Abstract Base Classes**: Uses ABC for a robust game object hierarchy
- **Particle System**: Real-time particle effects for thrusters and explosions
- **Vector Mathematics**: Utilizes pygame's Vector2 for precise physics calculations
- **Delta Time**: Frame-rate independent physics using time-based updates
- **Type Annotations**: Modern Python type hints for better code quality
- **Clean Architecture**: Separation of concerns with well-organized classes

## Controls

- **Arrow Up**: Apply thrust
- **Arrow Left/Right**: Rotate ship
- **ESC**: Quit game

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix/MacOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python src/game.py
```

## Project Structure

```
space_shooter/
├── src/
│   └── game.py         # Main game implementation
├── assets/             # Game assets (images, sounds)
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Resume-Worthy Elements

- Implementation of a particle system for visual effects
- Physics-based movement system
- Object-oriented design with inheritance
- Modern Python features (type hints, abstract classes)
- Clean code architecture and organization
- Real-time game loop management
- Efficient collision detection
- Vector mathematics for game physics 