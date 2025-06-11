# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player  
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawables)
    Asteroid.containers = (asteroids, updatable, drawables)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, shots,drawables)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                return print("Game Over!")
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
        
        
    

if __name__ == "__main__":
    main()


