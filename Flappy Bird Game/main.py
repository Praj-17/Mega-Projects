import random # For generating random numbers
import sys   # will use sys.exit() to exit the program
import pygame
import pygame.locals import*  
#Global variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHIEGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHIEGHT))
GROUNDY = SCREENHIEGHT *0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\bird.png'
BACKGROUND = 'E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\background.png'
PIPE = 'E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\pipe.png'

if __name__ ==  "__main__":
   #this will be the main point from where our game will start
   pygame.init() #initialize all pygame modules
   FPSCLOCK = pygame.time.Clock()
   pygame.display.set_caption("Flappy Bird by Prajwal Waykos")
   GAME_SPRITES['numbers'] = (
       pygame.image.load('E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\0.png').convert_alpha(), 
       pygame.image.load('E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\1.png').convert_alpha(),
       pygame.image.load('E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\2.png').convert_alpha(), 
       pygame.image.load('E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\3.png').convert_alpha(),
       pygame.image.load('E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\4.png').convert_alpha(), 
       pygame.image.load('E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\5.png').convert_alpha(), 
       pygame.image.load('E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\6.png').convert_alpha(),
       pygame.image.load('E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\7.png').convert_alpha(),
       pygame.image.load('E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\8.png').convert_alpha(),
       pygame.image.load('E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\9.png').convert_alpha())
GAME_SPRITES['message'] = pygame.imge.load('E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\message.png').convert_aplha()
GAME_SPRITES['base'] = pygame.imge.load('E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\base.png').convert_aplha()
GAME_SPRITES['pipe'] = pygame.imge.load('E:\CODING PLAYGROUND\CODE\Projects\Flappy Bird Game\gallery\sprites\\pipe.png').convert_aplha()
   
