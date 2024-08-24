import sys
import pygame
from pygame.color import THECOLORS
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    asteroid_field = AsteroidField()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.is_collided(player):
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_collided(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill(THECOLORS["black"])

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()