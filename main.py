import sys
import pygame
import random
import hero

class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        """Load the sprites that we need"""
        self.enemies = []
        for i in range(3):
            x = random.randrange(100, 400)
            y = random.randrange(100, 400)
            self.enemies.append(hero.Hero("Boogie", x, y, 'enemy.png' ))
        self.hero = hero.Hero("Conan", 50, 50, "hero.png")
        self.sprites = pygame.sprite.Group((self.hero,)+tuple(self.enemies))

    def mainLoop(self):
        """This is the Main Loop of the Game"""
        pygame.key.set_repeat(1,50)
        while True:
            self.background.fill((250, 250, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.hero.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move_right()
            #check for collisions
            for i in range(len(self.enemies)):
                if(pygame.sprite.collide_rect(self.hero, self.enemies[i])):
                    if(self.hero.fight(self.enemies[i])):
                        self.enemies[i].kill()
                        del self.enemies[i]
                    else:
                        self.background.fill((250, 0, 0))
                    break
            if(self.hero.health == 0):
                self.hero.kill()
            #redraw the entire screen
            self.screen.blit(self.background, (0, 0))
            self.sprites.draw(self.screen)
            pygame.display.flip()


def main():
    main_window = Controller()
    main_window.mainLoop()
main()
