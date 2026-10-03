from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame
from logger import log_event
import random
from player import Shot
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
       self.kill()
       if self.radius <= ASTEROID_MIN_RADIUS:
           return
       else:
           log_event("asteroid_split")
           new_angle = random.uniform(20, 50)
           first_asteroid_direction = self.velocity.rotate(new_angle)
           second_asteroid_direction = self.velocity.rotate(-new_angle)
           smaller_asteroid = self.radius - ASTEROID_MIN_RADIUS
           new_asteroid1 = Asteroid(self.position.x, self.position.y, smaller_asteroid)
           new_asteroid2 = Asteroid(self.position.x, self.position.y, smaller_asteroid)
           new_asteroid1.velocity = first_asteroid_direction * 1.2
           new_asteroid2.velocity = second_asteroid_direction * 1.2
