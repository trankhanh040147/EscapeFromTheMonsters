import pygame, sys
from obj.define import *
from obj.map import *
from obj.player import *
from obj.monster import *
from obj.game import *
from obj.button import *

def init():
    pygame.init()
    SCREEN = pygame.display.set_mode((WORLD_X, WORLD_Y))
    pygame.display.set_caption("Menu")
    BG = pygame.transform.scale(pygame.image.load("assets/img/BACKGOUND/Background.png"), (WORLD_X, WORLD_Y))
    return SCREEN, BG

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/img/BACKGOUND/font.ttf", size)

def play():
    game = Program()
    game.startProcess()
    game.main()
    game.endProcess()  

def main_menu():
    SCREEN, BG = init()
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(WORLD_X/2, 250*u))

        PLAY_BUTTON = Button(image=pygame.image.load("./assets/img/BACKGOUND/Play Rect.png"), pos=(WORLD_X/2, 420*u), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("./assets/img/BACKGOUND/Quit Rect.png"), pos=(WORLD_X/2, 550*u), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                    SCREEN, BG = init()
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
main_menu()