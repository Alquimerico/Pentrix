#Autores Ecab & Fanny :D
bR=ImportError
bs=True
bO=False
bh=int
bk=len
bu=None
bU=range
bw=list
# Tetrix
try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except bR:
    pass

import pygame.locals
from time import *
import random, time, pygame, sys
bq=pygame.mixer
be=pygame.JOYBUTTONDOWN
bI=pygame.time
bS=random.randint
bE=pygame.init
bz=pygame.display
bT=pygame.draw
bf=pygame.quit
bD=pygame.event
bF=time.time
bc=pygame.locals
bX=time.clock
bW=pygame.joystick
bn=sys.exit
bB=pygame.font
bY=random.choice
KEYUP = pygame.KEYUP
KEYDOWN = pygame.KEYDOWN
JOYBUTTONDOWN = pygame.JOYBUTTONDOWN
JOYBUTTONUP = pygame.JOYBUTTONUP
K_ESCAPE = pygame.K_ESCAPE
K_SPACE = pygame.K_SPACE
#Esto es usado para crear el binario, no?
try:
    from distutils.core import setup
    import py2exe
except bR:
    pass


bE()

    #Code used to init the joystick
    #Commit joystick?

try:
    j1 = bW.Joystick(0)
    j1.init()
    N = bs
except:
    N = bO

b = 25
C = 720
v = 550
r = 20
P = 15
i = 20
Q = '.'

p = 0.15
J = 0.1

M = bh((C - P * r) / 2)
g = v - (i * r) - 5



#               R    G    B
L       = (255, 255, 255)
l        = (247, 232, 232)
t       = (  0,   0,   0)
Y         = (232,  45,  54)
S    = (175,  20,  20)
X       = (  0, 150, 136)
F  = (  1, 255, 134)
c        = ( 40,  86, 182)
E   = ( 79, 181, 203)
W      = (234, 199,  97)
I = (175, 175,  20)
z        = (154,  82,  88)
B      = ( 61,  48,  83)
q      = (255,  49,  83)
D      = (112, 160, 136)

def Ny():
    e=[L, l, t, Y, S, X,F,c,E,W,I,z,B]
    f = bY(e)
    return f

f=Ny()

T = W

n = t
R = l
s      = (     c,      X,      Y,      W)
O = (E, F, S, I)
assert bk(s) == bk(O) # each color must have light color

h = 5
k = 5

u = [['.....',
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

U =                    [['.....',
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

w =                    [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '..O..'],
                    ['.....',
                     '.....',
                     'OOOOO',
                     '.....',
                     '.....']]

j =                    [['.....',
                     '..O..',
                     '.OOO.',
                     '..O..',
                     '.....']
                    ]

m =                    [['.....',
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

A =                    [['.....',
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

o = [['.....',
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
y = [['.....',
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


V = [['.....',
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


x = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

d = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

H = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

K = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

a = [['.....',
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

G = [['.....',
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

Nb = [['.....',
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

NC = [['.....',
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
Nv = [['.....',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.....',
                     '.....']]



Nr = {
    #Tetraminos
        'S': x,
          'Z': d,
          'J': a,
          'L': G,
          'I': H,
          'O': K,
          'T': Nb,
          #Pentaminos
          'DI': u,
          'DD': U,
          'LI': w,
          'FI': j,
          'AR': m,
          'DE': A,
          'MA': o,
          'M2': y,
          'LL': V,
          #Triminos
          'LM': NC,
          'IM': Nv
          }


def NV():
    global NP, Ni, Np, NQ, NJ
    NP = pygame.time.Clock()
    
    #print(pygame.joystick.get_init())
    #print(pygame.joystick.get_count())

    Ni = bz.set_mode((C, v))
    NQ = bB.Font('freesansbold.ttf', 20)
    Np = bB.Font('hetero.ttf', 20)
    NJ = bB.Font('pepperoni_pizza.ttf', 100)
    bz.set_caption('Pentrix')
    f=Ny()

    Na('Pentrix')
    while bs: # game loop
        if bS(0, 1) == 0:
            bq.music.load("Video_Game_Themes_-_Crash_Bandicoot_Warped.mid")
        else:
            bq.music.load("djwill96_-_Day_'n'_Nite_v2.mid")
        bq.music.play(-1, 0.0)
        Nx()
        bq.music.stop()
        Na('Perdiste')


def Nx():
    # setup variables for the start of the game
    f=Ny()
    NM = br()
    Ng = bF()
    NL = bF()
    Nl = bF()
    Nt = bO # note: there is no movingUp variable
    NY = bO
    NS = bO
    NX = 0
    NF, Nc = bN(NX)

    NE = bC()
    NW = bC()

    while bs: # game loop
        if NE == bu:
            # No falling piece in play, so start a new piece at the top
            f=Ny()
            NE = NW
            NW = bC()
            Nl = bF() # reset lastFallTime

            if not bi(NM, NE):
                return # can't fit a new piece on the board, so game over

        NG()
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

        for NI in bD.get(): # event handling loop
            #Derecha
            if N:
                if j1.get_hat(0)[0] == 1 and bi(NM, NE, adjX=1):
                    NE['x'] += 1
                    NS = bs
                    NY = bO
                    NL = bF()
                if j1.get_hat(0)[0] == 0:
                    NS = bO
                    NY = bO

                #Izquierda
                if j1.get_hat(0)[0] == -1 and bi(NM, NE, adjX=-1):
                    NE['x'] -= 1
                    NY = bs
                    NS = bO
                    NL = bF()
                #Abajo, acelerar caida
                if j1.get_hat(0)[1] == -1:
                    Nt = bs
                    if bi(NM, NE, adjY=1):
                        NE['y'] += 1
                    Ng = bF()
                if j1.get_hat(0)[1] == 0:
                    Nt = bO


            #TODO: Terminar eventos de botones pausa, rotacion inversa y down
            if NI.type == be:
                #El boton 2 equivale a X en xinput -> Rota la pieza
                if N:
                    if j1.get_button(2) == 1:
                        NE['rotation'] = (NE['rotation'] + 1) % bk(Nr[NE['shape']])
                        if not bi(NM, NE):
                            NE['rotation'] = (NE['rotation'] - 1) % bk(Nr[NE['shape']])
                    #El boton 1 equivale a A en xinput -> Suela fuerte la pieza
                    if j1.get_button(0) == 1:
                        Nt = bO
                        NY = bO
                        NS = bO
                        for i in bU(1, i):
                            if not bi(NM, NE, adjY=i):
                                 break
                        NE['y'] += i - 1

                    #TODO: This isn't correctly bind to the start button in xinput protocol
                    #TODO Correct this when F710 is avaliable
                    if j1.get_button(9) == 1:
                        Ni.fill(f)
                        bq.music.stop()
                        Na('Pausa :D')  # pause until a key press
                        bq.music.play(-1, 0.0)
                        Nl = bF()
                        Ng = bF()
                        NL = bF()
            
            if NI.type == KEYUP:
                if (NI.key == K_p):
                    # Pausing the game
                    Ni.fill(f)
                    bq.music.stop()
                    Na('Pausa :D') # pause until a key press
                    bq.music.play(-1, 0.0)
                    Nl = bF()
                    Ng = bF()
                    NL = bF()
                elif (NI.key == K_LEFT or NI.key == K_a):
                    NY = bO
                elif (NI.key == K_RIGHT or NI.key == K_d):
                    NS = bO
                elif (NI.key == K_DOWN or NI.key == K_s):
                    Nt = bO

            elif NI.type == KEYDOWN:
                # moving the piece sideways
                if (NI.key == K_LEFT or NI.key == K_a) and bi(NM, NE, adjX=-1):
                    NE['x'] -= 1
                    NY = bs
                    NS = bO
                    NL = bF()

                elif (NI.key == K_RIGHT or NI.key == K_d) and bi(NM, NE, adjX=1):
                    NE['x'] += 1
                    NS = bs
                    NY = bO
                    NL = bF()

                # rotating the piece (if there is room to rotate)
                elif (NI.key == K_UP or NI.key == K_w):
                    NE['rotation'] = (NE['rotation'] + 1) % bk(Nr[NE['shape']])
                    if not bi(NM, NE):
                        NE['rotation'] = (NE['rotation'] - 1) % bk(Nr[NE['shape']])
                elif (NI.key == K_q): # rotate the other direction
                    NE['rotation'] = (NE['rotation'] - 1) % bk(Nr[NE['shape']])
                    if not bi(NM, NE):
                        NE['rotation'] = (NE['rotation'] + 1) % bk(Nr[NE['shape']])

                # making the piece fall faster with the down key
                elif (NI.key == K_DOWN or NI.key == K_s):
                    Nt = bs
                    if bi(NM, NE, adjY=1):
                        NE['y'] += 1
                    Ng = bF()

                # move the current piece all the way down
                #Modified with get_button to support joystick
                elif NI.key == K_SPACE:
                    Nt = bO
                    NY = bO
                    NS = bO
                    for i in bU(1, i):
                        if not bi(NM, NE, adjY=i):
                            break
                    NE['y'] += i - 1

        # handle moving the piece because of user input
        if (NY or NS) and bF() - NL > p:
            if NY and bi(NM, NE, adjX=-1):
                NE['x'] -= 1
            elif NS and bi(NM, NE, adjX=1):
                NE['x'] += 1
            NL = bF()

        if Nt and bF() - Ng > J and bi(NM, NE, adjY=1):
            NE['y'] += 1
            Ng = bF()

        # let the piece fall if it is time to fall
        if bF() - Nl > Nc:
            # see if the piece has landed
            if not bi(NM, NE, adjY=1):
                # falling piece has landed, set it on the board
                bv(NM, NE)
                NX += bp(NM)
                NF, Nc = bN(NX)
                NE = bu
            else:
                # piece did not land, just move the piece down
                NE['y'] += 1
                Nl = bF()

        # drawing everything on the screen
        Ni.fill(f)
        bg(NM)
        bL(NX, NF)
        bt(NW)
        if NE != bu:
            bl(NE)

        bz.update()
        NP.tick(b)


def Nd(text, font, Ny):
    Nz = font.render(text, bs, Ny)
    return Nz, Nz.get_rect()


def NH():
    bf()
    bn()



def NK():
    # Go through event queue looking for a KEYUP event.
    # Grab KEYDOWN events to remove them from the event queue.
    NG()

    #TODO FIX THE FUCKING PAUSE JOYSTICK BUTTON, ISN'T WORKING CORRECTLY
    for NI in bD.get([KEYDOWN, KEYUP,JOYBUTTONDOWN,JOYBUTTONUP]):
        #Check any
        if NI.type == KEYDOWN or NI.type == JOYBUTTONDOWN:
            continue
        return K_SPACE
        # event.key
    return bu


def Na(text):
    # This function displays large text in the
    # center of the screen until a key is pressed.
    # Draw the text drop shadow
    NB, Nq = Nd(text, NJ, R)
    Nq.center = (bh(C / 2), bh(v / 2))
    Ni.blit(NB, Nq)

    # Draw the text
    NB, Nq = Nd(text, NJ, n)
    Nq.center = (bh(C / 2) - 3, bh(v / 2) - 3)
    Ni.blit(NB, Nq)

    # Draw the additional "Press a key to play." text.
    ND, Ne = Nd('Presiona una tecla para jugar >:D', NQ, n)
    Ne.center = (bh(C / 2), bh(v / 2) + 100)
    Ni.blit(ND, Ne)

    while NK() == bu:
        bz.update()
        NP.tick()


def NG():
    for NI in pygame.event.get(pygame.QUIT): # get all the QUIT events
        NH() # terminate if any QUIT events are present
    for NI in bD.get(KEYUP): # get all the KEYUP events
        if NI.key == K_ESCAPE:
            NH() # terminate if the KEYUP event was for the Esc key
        bD.post(NI) # put the other KEYUP event objects back


def bN(NX):
    # Based on the score, return the level the player is on and
    # how many seconds pass until a falling piece falls one space.
    NF = bh(NX / 10) + 1
    Nc = 0.27 - (NF * 0.02)
    return NF, Nc

def bC():
    # return a random new piece in a random rotation and color
    Nf = bY(bw(Nr.keys()))
    NT = {'shape': Nf,
                'rotation': bS(0, bk(Nr[Nf]) - 1),
                'x': bh(P / 2) - bh(h / 2),
                'y': -2, # start it above the board (i.e. less than 0)
                'color': bS(0, bk(s)-1)}
    return NT


def bv(NM, Nn):
    # fill in the board based on piece's location, shape, and rotation
    for x in bU(h):
        for y in bU(k):
            if Nr[Nn['shape']][Nn['rotation']][y][x] != Q:
                NM[x + Nn['x']][y + Nn['y']] = Nn['color']


def br():
    # create and return a new blank board data structure
    NM = []
    for i in bU(P):
        NM.append([Q] * i)
    return NM


def bP(x, y):
    return x >= 0 and x < P and y < i


def bi(NM, Nn, adjX=0, adjY=0):
    # Return True if the piece is within the board and not colliding
    for x in bU(h):
        for y in bU(k):
            NR = y + Nn['y'] + adjY < 0
            if NR or Nr[Nn['shape']][Nn['rotation']][y][x] == Q:
                continue
            if not bP(x + Nn['x'] + adjX, y + Nn['y'] + adjY):
                return bO
            if NM[x + Nn['x'] + adjX][y + Nn['y'] + adjY] != Q:
                return bO
    return bs

def bQ(NM, y):
    # Return True if the line filled with boxes with no gaps.
    for x in bU(P):
        if NM[x][y] == Q:
            return bO
    return bs


def bp(NM):
    # Remove any completed lines on the board, move everything above them down, and return the number of complete lines.
    Ns = 0
    y = i - 1 # start y at the bottom of the board
    while y >= 0:
        if bQ(NM, y):
            # Remove the line and pull boxes down by one line.
            for NO in bU(y, 0, -1):
                for x in bU(P):
                    NM[x][NO] = NM[x][NO-1]
            # Set very top line to blank.
            for x in bU(P):
                NM[x][0] = Q
            Ns += 1
            # Note on the next iteration of the loop, y is the same.
            # This is so that if the line that was pulled down is also
            # complete, it will be removed.
        else:
            y -= 1 # move on to check next row up
    return Ns


def bJ(boxx, boxy):
    # Convert the given xy coordinates of the board to xy
    # coordinates of the location on the screen.
    return (M + (boxx * r)), (g + (boxy * r))


def bM(boxx, boxy, Ny, pixelx=bu, pixely=bu):
    # draw a single box (each tetromino piece has four boxes)
    # at xy coordinates on the board. Or, if pixelx & pixely
    # are specified, draw to the pixel coordinates stored in
    # pixelx & pixely (this is used for the "Next" piece).
    if Ny == Q:
        return
    if pixelx == bu and pixely == bu:
        pixelx, pixely = bJ(boxx, boxy)
    bT.rect(Ni, s[Ny], (pixelx + 1, pixely + 1, r - 1, r - 1))
    bT.rect(Ni, O[Ny], (pixelx + 1, pixely + 1, r - 4, r - 4))


def bg(NM):
    # draw the border around the board
    bT.rect(Ni, f, (M - 3, g - 7, (P * r) + 8, (i * r) + 8), 5)

    # fill the background of the board
    bT.rect(Ni, f, (M, g, r * P, r * i))
    # draw the individual boxes on the board
    for x in bU(P):
        for y in bU(i):
            bM(x, y, NM[x][y])


def bL(NX, NF):
    # draw the score text
    Nu = Np.render('Puntuacion: %s' % NX, bs, n)
    NU = Nu.get_rect()
    NU.topleft = (C - 230, 20)
    Ni.blit(Nu, NU)

    # draw the level text
    Nw = Np.render('Nivel: %s' % NF, bs, n)
    Nj = Nw.get_rect()
    Nj.topleft = (C - 230, 50)
    Ni.blit(Nw, Nj)


def bl(Nn, pixelx=bu, pixely=bu):
    Nm = Nr[Nn['shape']][Nn['rotation']]
    if pixelx == bu and pixely == bu:
        # if pixelx & pixely hasn't been specified, use the location stored in the piece data structure
        pixelx, pixely = bJ(Nn['x'], Nn['y'])

    # draw each of the boxes that make up the piece
    for x in bU(h):
        for y in bU(k):
            if Nm[y][x] != Q:
                bM(bu, bu, Nn['color'], pixelx + (x * r), pixely + (y * r))


def bt(Nn):
    # draw the "next" text
    NA = Np.render('Siguiente:', bs, n)
    No = NA.get_rect()
    No.topleft = (C - 200, 80)
    Ni.blit(NA, No)
    # draw the "next" piece
    bl(Nn, pixelx=C-120, pixely=100)


if __name__ == '__main__':
    NV()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
