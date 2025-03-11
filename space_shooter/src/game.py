import pygame
import sys
import random
import math
import numpy as np
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class GameObject(ABC):
    """Abstract base class for all game objects"""
    def __init__(self, x: float, y: float, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = pygame.math.Vector2(0, 0)
        
    @abstractmethod
    def update(self, dt: float) -> None:
        """Update object state"""
        pass
        
    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        """Draw object on screen"""
        pass
        
    def get_rect(self) -> pygame.Rect:
        """Get current rectangle for collision detection"""
        self.rect.x = self.x
        self.rect.y = self.y
        return self.rect

class ParticleSystem:
    """Handles particle effects for explosions and thrusters"""
    def __init__(self, x: float, y: float, color: Tuple[int, int, int]):
        self.particles: List[dict] = []
        self.x = x
        self.y = y
        self.color = color
        
    def emit(self, count: int, speed: float) -> None:
        """Emit new particles"""
        for _ in range(count):
            angle = random.uniform(0, 2 * math.pi)
            speed_var = random.uniform(0.5, 1.5) * speed
            self.particles.append({
                'x': self.x,
                'y': self.y,
                'vx': math.cos(angle) * speed_var,
                'vy': math.sin(angle) * speed_var,
                'lifetime': random.uniform(0.5, 1.5)
            })
            
    def update(self, dt: float) -> None:
        """Update particle positions and lifetimes"""
        for particle in self.particles[:]:
            particle['x'] += particle['vx'] * dt
            particle['y'] += particle['vy'] * dt
            particle['lifetime'] -= dt
            if particle['lifetime'] <= 0:
                self.particles.remove(particle)
                
    def draw(self, screen: pygame.Surface) -> None:
        """Draw all particles"""
        for particle in self.particles:
            alpha = int(255 * (particle['lifetime'] / 1.5))
            color = (*self.color, alpha)
            pos = (int(particle['x']), int(particle['y']))
            pygame.draw.circle(screen, color, pos, 2)

class Player(GameObject):
    """Player spaceship class"""
    def __init__(self, x: float, y: float):
        super().__init__(x, y, 40, 40)
        self.thrust = 300
        self.rotation = 0
        self.shooting_cooldown = 0
        self.thruster_particles = ParticleSystem(x, y, BLUE)
        
    def update(self, dt: float) -> None:
        # Handle input
        keys = pygame.key.get_pressed()
        
        # Rotation
        if keys[pygame.K_LEFT]:
            self.rotation -= 180 * dt
        if keys[pygame.K_RIGHT]:
            self.rotation += 180 * dt
            
        # Movement
        if keys[pygame.K_UP]:
            angle_rad = math.radians(self.rotation)
            self.velocity.x += math.cos(angle_rad) * self.thrust * dt
            self.velocity.y -= math.sin(angle_rad) * self.thrust * dt
            # Emit thruster particles
            self.thruster_particles.emit(5, 100)
            
        # Apply friction
        self.velocity *= 0.99
        
        # Update position
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt
        
        # Screen wrapping
        self.x = self.x % SCREEN_WIDTH
        self.y = self.y % SCREEN_HEIGHT
        
        # Update thruster particles
        self.thruster_particles.x = self.x + self.width/2
        self.thruster_particles.y = self.y + self.height/2
        self.thruster_particles.update(dt)
        
        # Update shooting cooldown
        if self.shooting_cooldown > 0:
            self.shooting_cooldown -= dt
            
    def draw(self, screen: pygame.Surface) -> None:
        # Draw thruster particles
        self.thruster_particles.draw(screen)
        
        # Draw ship
        surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        points = [
            (self.width/2, 0),
            (0, self.height),
            (self.width/2, self.height*0.8),
            (self.width, self.height)
        ]
        pygame.draw.polygon(surface, WHITE, points)
        
        # Rotate ship
        rotated = pygame.transform.rotate(surface, self.rotation)
        rect = rotated.get_rect(center=(self.x + self.width/2, self.y + self.height/2))
        screen.blit(rotated, rect)

class Game:
    """Main game class"""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space Shooter")
        self.clock = pygame.time.Clock()
        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.running = True
        
    def handle_events(self) -> None:
        """Handle game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    
    def update(self, dt: float) -> None:
        """Update game state"""
        self.player.update(dt)
        
    def draw(self) -> None:
        """Draw game state"""
        self.screen.fill(BLACK)
        self.player.draw(self.screen)
        pygame.display.flip()
        
    def run(self) -> None:
        """Main game loop"""
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self.handle_events()
            self.update(dt)
            self.draw()
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run() 