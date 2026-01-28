import pygame

class GameConfig:
    WINDOW_H = 640
    WINDOW_W = 960
    BACKGROUND_IMG = None
    Y_PLATEFORM = 516
    PLAYER_W = 64
    PLAYER_H = 64
    STANDING_IMG = None
    DT = 0.5
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT
    GRAVITY = 9.81
    FORCE_JUMP = -100
    def init():
        GameConfig.BACKGROUND_IMG = pygame.image.load('ressources/background.png')
        GameConfig.STANDING_IMG = pygame.image.load('ressources/standing.png')
        