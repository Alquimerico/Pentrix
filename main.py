# Partial code based on:
# Tetromino (a Tetris clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Creative Commons BY-NC-SA 3.0 US

# Pentrix
# Adapted by Ecab & Fanny :D
# Repo avaliable at Github
# https://github.com/Alquimerico/Tetrix
# Please fork us :3


## Agradecimientos a wagakimi, por ser wagakimi ##

try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass

import random, time, pygame, sys
#Esto es usado para crear el binario, no?
try:
    from distutils.core import setup
    import py2exe
except ImportError:
    pass


from pygame.locals import *

pygame.init()

    #Code used to init the joystick
    #Commit joystick?

try:
    j1 = pygame.joystick.Joystick(0)
    j1.init()
    joystickConnected = True
except:
    joystickConnected = False

FPS = 25
WINDOWWIDTH = 720
WINDOWHEIGHT = 550
BOXSIZE = 20
BOARDWIDTH = 15
BOARDHEIGHT = 20
BLANK = '.'

MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.1

XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5



#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (247, 232, 232)
BLACK       = (  0,   0,   0)
RED         = (232,  45,  54)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 150, 136)
LIGHTGREEN  = (  1, 255, 134)
BLUE        = ( 40,  86, 182)
LIGHTBLUE   = ( 79, 181, 203)
YELLOW      = (234, 199,  97)
LIGHTYELLOW = (175, 175,  20)
PINK        = (154,  82,  88)
PURPLE      = ( 61,  48,  83)
ORANGE      = (255,  49,  83)
BORDER      = (112, 160, 136)

def color():
    colors=[WHITE, GRAY, BLACK, RED, LIGHTRED, GREEN,LIGHTGREEN,BLUE,LIGHTBLUE,YELLOW,LIGHTYELLOW,PINK,PURPLE]
    BGCOLOR = random.choice(colors)
    return BGCOLOR

BGCOLOR=color()

BORDERCOLOR = YELLOW

TEXTCOLOR = BLACK
TEXTSHADOWCOLOR = GRAY
COLORS      = (     BLUE,      GREEN,      RED,      YELLOW)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
assert len(COLORS) == len(LIGHTCOLORS) # each color must have light color

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5

DEDOIZQUIERDO_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OOO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '..OOO',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '..OO.',
                     '..OO.',
                     '...O.']
                    ]

DEDODERECHO_SHAPE_TEMPLATE = \
                    [['.....',
                     '...O.',
                     '..OO.',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '..OO.',
                     '..OOO',
                     '.....'],
                    ['.....',
                     '.....',
                     '..OO.',
                     '..OO.',
                     '..O..'],
                    ['.....',
                     '.....',
                     '..OO.',
                     '.OOO.',
                     '.....']
                    ]

LONGI_SHAPE_TEMPLATE = \
                    [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '..O..'],
                    ['.....',
                     '.....',
                     'OOOOO',
                     '.....',
                     '.....']]

FILLSHAPE_SHAPE_TEMPLATE = \
                    [['.....',
                     '..O..',
                     '.OOO.',
                     '..O..',
                     '.....']
                    ]

ARCO_SHAPE_TEMPLATE = \
                    [['.....',
                     '.O.O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O.O.',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '.OO..',
                     '.....']]

DEDO_DE_ENMEDIO_SHAPE_TEMPLATE = \
                    [['.....',
                     '...O.',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OOO.',
                     '.....'],
                    ['.....',
                     '.O...',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OOO.',
                     '..O..',
                     '..O..',
                     '.....']]

MACANA_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOOO',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '..O..'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '..O..',
                     '.....'],
                    ['..O..',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]
MACANA2_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOOO',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '..O..'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.O...',
                     '.....'],
                    ['..O..',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]


LONGL_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OOO',
                     '....O',
                     '....O'],
                      ['.....',
                       '...O.',
                       '...O.',
                       '.OOO.',
                       '.....'],
                    ['.....',
                     '.O...',
                     '.O...',
                     '.OOO.',
                     '.....'],
                    ['.....',
                     '.OOO.',
                     '.O...',
                     '.O...',
                     '.....']]


S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]

L_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

T_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]

LMINI_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '..OO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '.....',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '..OO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.....',
                     '.....']]
IMINI_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.....',
                     '.....']]



PIECES = {
    #Tetraminos
        'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE,
          #Pentaminos
          'DI': DEDOIZQUIERDO_SHAPE_TEMPLATE,
          'DD': DEDODERECHO_SHAPE_TEMPLATE,
          'LI': LONGI_SHAPE_TEMPLATE,
          'FI': FILLSHAPE_SHAPE_TEMPLATE,
          'AR': ARCO_SHAPE_TEMPLATE,
          'DE': DEDO_DE_ENMEDIO_SHAPE_TEMPLATE,
          'MA': MACANA_SHAPE_TEMPLATE,
          'M2': MACANA2_SHAPE_TEMPLATE,
          'LL': LONGL_SHAPE_TEMPLATE,
          #Triminos
          'LM': LMINI_SHAPE_TEMPLATE,
          'IM': IMINI_SHAPE_TEMPLATE
          }


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, ALERTFONT, BIGFONT
    FPSCLOCK = pygame.time.Clock()
    
    #print(pygame.joystick.get_init())
    #print(pygame.joystick.get_count())

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    ALERTFONT = pygame.font.Font('freesansbold.ttf', 20)
    BASICFONT = pygame.font.Font('hetero.ttf', 20)
    BIGFONT = pygame.font.Font('pepperoni_pizza.ttf', 100)
    pygame.display.set_caption('Pentrix')
    BGCOLOR=color()

    showTextScreen('Pentrix')
    while True: # game loop
        if random.randint(0, 1) == 0:
            pygame.mixer.music.load("Video_Game_Themes_-_Crash_Bandicoot_Warped.mid")
        else:
            pygame.mixer.music.load("djwill96_-_Day_'n'_Nite_v2.mid")
        pygame.mixer.music.play(-1, 0.0)
        runGame()
        pygame.mixer.music.stop()
        showTextScreen('Perdiste')


def runGame():
    # setup variables for the start of the game
    BGCOLOR=color()
    board = getBlankBoard()
    lastMoveDownTime = time.time()
    lastMoveSidewaysTime = time.time()
    lastFallTime = time.time()
    movingDown = False # note: there is no movingUp variable
    movingLeft = False
    movingRight = False
    score = 0
    level, fallFreq = calculateLevelAndFallFreq(score)

    fallingPiece = getNewPiece()
    nextPiece = getNewPiece()

    while True: # game loop
        if fallingPiece == None:
            # No falling piece in play, so start a new piece at the top
            BGCOLOR=color()
            fallingPiece = nextPiece
            nextPiece = getNewPiece()
            lastFallTime = time.time() # reset lastFallTime

            if not isValidPosition(board, fallingPiece):
                return # can't fit a new piece on the board, so game over

        checkForQuit()
        '''
        for x in range(j1.get_numbuttons()):
            if event.type == pygame.JOYBUTTONUP:
                if j1.get_button(0) == 1:
                    movingDown = False
                    movingLeft = False
                    movingRight = False
                    for i in range(1, BOARDHEIGHT):
                        if not isValidPosition(board, fallingPiece, adjY=i):
                             break
                    fallingPiece['y'] += i - 1

            if event.type == pygame.JOYBUTTONDOWN:
                if j1.get_button(2) == 1:
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                        '''

        for event in pygame.event.get(): # event handling loop
            #Derecha
            if joystickConnected:
                if j1.get_hat(0)[0] == 1 and isValidPosition(board, fallingPiece, adjX=1):
                    fallingPiece['x'] += 1
                    movingRight = True
                    movingLeft = False
                    lastMoveSidewaysTime = time.time()
                if j1.get_hat(0)[0] == 0:
                    movingRight = False
                    movingLeft = False

                #Izquierda
                if j1.get_hat(0)[0] == -1 and isValidPosition(board, fallingPiece, adjX=-1):
                    fallingPiece['x'] -= 1
                    movingLeft = True
                    movingRight = False
                    lastMoveSidewaysTime = time.time()
                #Abajo, acelerar caida
                if j1.get_hat(0)[1] == -1:
                    movingDown = True
                    if isValidPosition(board, fallingPiece, adjY=1):
                        fallingPiece['y'] += 1
                    lastMoveDownTime = time.time()
                if j1.get_hat(0)[1] == 0:
                    movingDown = False


            #TODO: Terminar eventos de botones pausa, rotacion inversa y down
            if event.type == pygame.JOYBUTTONDOWN:
                #El boton 2 equivale a X en xinput -> Rota la pieza
                if joystickConnected:
                    if j1.get_button(2) == 1:
                        fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
                        if not isValidPosition(board, fallingPiece):
                            fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                    #El boton 1 equivale a A en xinput -> Suela fuerte la pieza
                    if j1.get_button(0) == 1:
                        movingDown = False
                        movingLeft = False
                        movingRight = False
                        for i in range(1, BOARDHEIGHT):
                            if not isValidPosition(board, fallingPiece, adjY=i):
                                 break
                        fallingPiece['y'] += i - 1

                    #TODO: This isn't correctly bind to the start button in xinput protocol
                    #TODO Correct this when F710 is avaliable
                    if j1.get_button(9) == 1:
                        DISPLAYSURF.fill(BGCOLOR)
                        pygame.mixer.music.stop()
                        showTextScreen('Pausa :D')  # pause until a key press
                        pygame.mixer.music.play(-1, 0.0)
                        lastFallTime = time.time()
                        lastMoveDownTime = time.time()
                        lastMoveSidewaysTime = time.time()
            
            if event.type == KEYUP:
                if (event.key == K_p):
                    # Pausing the game
                    DISPLAYSURF.fill(BGCOLOR)
                    pygame.mixer.music.stop()
                    showTextScreen('Pausa :D') # pause until a key press
                    pygame.mixer.music.play(-1, 0.0)
                    lastFallTime = time.time()
                    lastMoveDownTime = time.time()
                    lastMoveSidewaysTime = time.time()
                elif (event.key == K_LEFT or event.key == K_a):
                    movingLeft = False
                elif (event.key == K_RIGHT or event.key == K_d):
                    movingRight = False
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = False

            elif event.type == KEYDOWN:
                # moving the piece sideways
                if (event.key == K_LEFT or event.key == K_a) and isValidPosition(board, fallingPiece, adjX=-1):
                    fallingPiece['x'] -= 1
                    movingLeft = True
                    movingRight = False
                    lastMoveSidewaysTime = time.time()

                elif (event.key == K_RIGHT or event.key == K_d) and isValidPosition(board, fallingPiece, adjX=1):
                    fallingPiece['x'] += 1
                    movingRight = True
                    movingLeft = False
                    lastMoveSidewaysTime = time.time()

                # rotating the piece (if there is room to rotate)
                elif (event.key == K_UP or event.key == K_w):
                    fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                elif (event.key == K_q): # rotate the other direction
                    fallingPiece['rotation'] = (fallingPiece['rotation'] - 1) % len(PIECES[fallingPiece['shape']])
                    if not isValidPosition(board, fallingPiece):
                        fallingPiece['rotation'] = (fallingPiece['rotation'] + 1) % len(PIECES[fallingPiece['shape']])

                # making the piece fall faster with the down key
                elif (event.key == K_DOWN or event.key == K_s):
                    movingDown = True
                    if isValidPosition(board, fallingPiece, adjY=1):
                        fallingPiece['y'] += 1
                    lastMoveDownTime = time.time()

                # move the current piece all the way down
                #Modified with get_button to support joystick
                elif event.key == K_SPACE:
                    movingDown = False
                    movingLeft = False
                    movingRight = False
                    for i in range(1, BOARDHEIGHT):
                        if not isValidPosition(board, fallingPiece, adjY=i):
                            break
                    fallingPiece['y'] += i - 1

        # handle moving the piece because of user input
        if (movingLeft or movingRight) and time.time() - lastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if movingLeft and isValidPosition(board, fallingPiece, adjX=-1):
                fallingPiece['x'] -= 1
            elif movingRight and isValidPosition(board, fallingPiece, adjX=1):
                fallingPiece['x'] += 1
            lastMoveSidewaysTime = time.time()

        if movingDown and time.time() - lastMoveDownTime > MOVEDOWNFREQ and isValidPosition(board, fallingPiece, adjY=1):
            fallingPiece['y'] += 1
            lastMoveDownTime = time.time()

        # let the piece fall if it is time to fall
        if time.time() - lastFallTime > fallFreq:
            # see if the piece has landed
            if not isValidPosition(board, fallingPiece, adjY=1):
                # falling piece has landed, set it on the board
                addToBoard(board, fallingPiece)
                score += removeCompleteLines(board)
                level, fallFreq = calculateLevelAndFallFreq(score)
                fallingPiece = None
            else:
                # piece did not land, just move the piece down
                fallingPiece['y'] += 1
                lastFallTime = time.time()

        # drawing everything on the screen
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(board)
        drawStatus(score, level)
        drawNextPiece(nextPiece)
        if fallingPiece != None:
            drawPiece(fallingPiece)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


def terminate():
    pygame.quit()
    sys.exit()



def checkForKeyPress():
    # Go through event queue looking for a KEYUP event.
    # Grab KEYDOWN events to remove them from the event queue.
    checkForQuit()

    #TODO FIX THE FUCKING PAUSE JOYSTICK BUTTON, ISN'T WORKING CORRECTLY
    for event in pygame.event.get([KEYDOWN, KEYUP,JOYBUTTONDOWN,JOYBUTTONUP]):
        #Check any
        if event.type == KEYDOWN or event.type == JOYBUTTONDOWN:
            continue
        return K_SPACE
        # event.key
    return None


def showTextScreen(text):
    # This function displays large text in the
    # center of the screen until a key is pressed.
    # Draw the text drop shadow
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
    titleRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
    DISPLAYSURF.blit(titleSurf, titleRect)

    # Draw the text
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
    titleRect.center = (int(WINDOWWIDTH / 2) - 3, int(WINDOWHEIGHT / 2) - 3)
    DISPLAYSURF.blit(titleSurf, titleRect)

    # Draw the additional "Press a key to play." text.
    pressKeySurf, pressKeyRect = makeTextObjs('Presiona una tecla para jugar >:D', ALERTFONT, TEXTCOLOR)
    pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()
        FPSCLOCK.tick()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


def calculateLevelAndFallFreq(score):
    # Based on the score, return the level the player is on and
    # how many seconds pass until a falling piece falls one space.
    level = int(score / 10) + 1
    fallFreq = 0.27 - (level * 0.02)
    return level, fallFreq

def getNewPiece():
    # return a random new piece in a random rotation and color
    shape = random.choice(list(PIECES.keys()))
    newPiece = {'shape': shape,
                'rotation': random.randint(0, len(PIECES[shape]) - 1),
                'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
                'y': -2, # start it above the board (i.e. less than 0)
                'color': random.randint(0, len(COLORS)-1)}
    return newPiece


def addToBoard(board, piece):
    # fill in the board based on piece's location, shape, and rotation
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']


def getBlankBoard():
    # create and return a new blank board data structure
    board = []
    for i in range(BOARDWIDTH):
        board.append([BLANK] * BOARDHEIGHT)
    return board


def isOnBoard(x, y):
    return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT


def isValidPosition(board, piece, adjX=0, adjY=0):
    # Return True if the piece is within the board and not colliding
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            isAboveBoard = y + piece['y'] + adjY < 0
            if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue
            if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                return False
            if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                return False
    return True

def isCompleteLine(board, y):
    # Return True if the line filled with boxes with no gaps.
    for x in range(BOARDWIDTH):
        if board[x][y] == BLANK:
            return False
    return True


def removeCompleteLines(board):
    # Remove any completed lines on the board, move everything above them down, and return the number of complete lines.
    numLinesRemoved = 0
    y = BOARDHEIGHT - 1 # start y at the bottom of the board
    while y >= 0:
        if isCompleteLine(board, y):
            # Remove the line and pull boxes down by one line.
            for pullDownY in range(y, 0, -1):
                for x in range(BOARDWIDTH):
                    board[x][pullDownY] = board[x][pullDownY-1]
            # Set very top line to blank.
            for x in range(BOARDWIDTH):
                board[x][0] = BLANK
            numLinesRemoved += 1
            # Note on the next iteration of the loop, y is the same.
            # This is so that if the line that was pulled down is also
            # complete, it will be removed.
        else:
            y -= 1 # move on to check next row up
    return numLinesRemoved


def convertToPixelCoords(boxx, boxy):
    # Convert the given xy coordinates of the board to xy
    # coordinates of the location on the screen.
    return (XMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))


def drawBox(boxx, boxy, color, pixelx=None, pixely=None):
    # draw a single box (each tetromino piece has four boxes)
    # at xy coordinates on the board. Or, if pixelx & pixely
    # are specified, draw to the pixel coordinates stored in
    # pixelx & pixely (this is used for the "Next" piece).
    if color == BLANK:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertToPixelCoords(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
    pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))


def drawBoard(board):
    # draw the border around the board
    pygame.draw.rect(DISPLAYSURF, BGCOLOR, (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)

    # fill the background of the board
    pygame.draw.rect(DISPLAYSURF, BGCOLOR, (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
    # draw the individual boxes on the board
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            drawBox(x, y, board[x][y])


def drawStatus(score, level):
    # draw the score text
    scoreSurf = BASICFONT.render('Puntuacion: %s' % score, True, TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 230, 20)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

    # draw the level text
    levelSurf = BASICFONT.render('Nivel: %s' % level, True, TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (WINDOWWIDTH - 230, 50)
    DISPLAYSURF.blit(levelSurf, levelRect)


def drawPiece(piece, pixelx=None, pixely=None):
    shapeToDraw = PIECES[piece['shape']][piece['rotation']]
    if pixelx == None and pixely == None:
        # if pixelx & pixely hasn't been specified, use the location stored in the piece data structure
        pixelx, pixely = convertToPixelCoords(piece['x'], piece['y'])

    # draw each of the boxes that make up the piece
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if shapeToDraw[y][x] != BLANK:
                drawBox(None, None, piece['color'], pixelx + (x * BOXSIZE), pixely + (y * BOXSIZE))


def drawNextPiece(piece):
    # draw the "next" text
    nextSurf = BASICFONT.render('Siguiente:', True, TEXTCOLOR)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (WINDOWWIDTH - 200, 80)
    DISPLAYSURF.blit(nextSurf, nextRect)
    # draw the "next" piece
    drawPiece(piece, pixelx=WINDOWWIDTH-120, pixely=100)


if __name__ == '__main__':
    main()
