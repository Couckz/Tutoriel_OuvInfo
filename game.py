# import des modules et des autres fichiers
import pygame
from move import Move
from game_config import GameConfig
from game_state import GameState
#from game config import *
...
# fonctions utiles pour la gestion du jeu # ( affichage de message , rejouer , etc .)
def get_next_move():
    nextmove = Move()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] : 
        nextmove.right = True
    if keys[pygame.K_LEFT] : 
        nextmove.left = True
    if keys[pygame.K_UP] :
        nextmove.jump = True
    return nextmove

# Boucle de jeu
def game_loop(window) : 
    quitting = False
    game_state = GameState()
    while not quitting : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
        next_move = get_next_move()
        game_state.advance_state(next_move)
        game_state.draw(window)
        pygame.display.update()
        pygame.time.delay(20)

# Lancement du jeu
if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((GameConfig.WINDOW_W, GameConfig.WINDOW_H))
    pygame.display.set_caption("Avoid Bats")
    GameConfig.init()
    game_loop(window)
    pygame.quit()
    quit()
