import random, sys, pygame
pygame.init()
size = width, height = 1020, 1020
tileWidth=34
a,b,c,d,e,f,sx,sy = 3,3,3,3,3,3,4,4
screen = pygame.display.set_mode(size)
tileColour = 144,144,144
openColour = 100,100,100
markColour = 111,55,111
block=pygame.Surface((10,10))
recs=[]
sx,sy=(width-tileWidth*27-52)/2,4
bombs=100
closedTiles=a*b*c*d*e*f


Matrix = [[[[[[0 for x in range(a)] for y in range(b)]for z in range(c)]for g in range(d)]for h in range(e)]for i in range(f)]
openTiles = [[[[[[-1 for x in range(a)] for y in range(b)]for z in range(c)]for g in range(d)]for h in range(e)]for i in range(f)]

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 20)
myfont.set_bold(1)

def printNum(x1,x2,x3,x4,x5,x6):
    new_game_text = myfont.render(str(openTiles[x1][x2][x3][x4][x5][x6]), False, (30, 170, 30))
    new_game_rect = new_game_text.get_rect(center=recs[x1][x2][x3][x4][x5][x6].center)
    screen.blit(new_game_text, new_game_rect)

def putBomb():
    newBomb=[random.randint(0,2) for x in range(6)]
    if Matrix[newBomb[0]][newBomb[1]][newBomb[2]][newBomb[3]][newBomb[4]][newBomb[5]]==1:
        putBomb()
    else:
        Matrix[newBomb[0]][newBomb[1]][newBomb[2]][newBomb[3]][newBomb[4]][newBomb[5]]=1

def printBombs():
    for a1 in range(0,a):
        for a2 in range(0,b):
            for a3 in range(0,c):
                print(openTiles[a1][a2][a3])

def countBombs(x1,x2,x3,x4,x5,x6):
    n = 0
    if x1<a-1:
        if Matrix[x1+1][x2][x3][x4][x5][x6]==1:
            n=n+1
    if x1>0:
        if Matrix[x1-1][x2][x3][x4][x5][x6]==1:
            n=n+1
    if x2<b-1:
        if Matrix[x1][x2+1][x3][x4][x5][x6]==1:
            n=n+1
    if x2>0:
        if Matrix[x1][x2-1][x3][x4][x5][x6]==1:
            n=n+1
    if x3<c-1:
        if Matrix[x1][x2][x3+1][x4][x5][x6]==1:
            n=n+1
    if x3>0:
        if Matrix[x1][x2][x3-1][x4][x5][x6]==1:
            n=n+1
    if x4<d-1:
        if Matrix[x1][x2][x3][x4+1][x5][x6]==1:
            n=n+1
    if x4>0:
        if Matrix[x1][x2][x3][x4-1][x5][x6]==1:
            n=n+1
    if x5<e-1:
        if Matrix[x1][x2][x3][x4][x5+1][x6]==1:
            n=n+1
    if x5>0:
        if Matrix[x1][x2][x3][x4][x5-1][x6]==1:
            n=n+1
    if x6<f-1:
        if Matrix[x1][x2][x3][x4][x5][x6+1]==1:
            n=n+1
    if x6>0:
        if Matrix[x1][x2][x3][x4][x5][x6-1]==1:
            n=n+1
    return n

def openTile(x1,x2,x3,x4,x5,x6):
    openTiles[x1][x2][x3][x4][x5][x6]=countBombs(x1,x2,x3,x4,x5,x6)
    global closedTiles
    closedTiles=closedTiles-1
    pygame.draw.rect(screen,openColour,(recs[x1][x2][x3][x4][x5][x6].left,recs[x1][x2][x3][x4][x5][x6].top,tileWidth,tileWidth))
    if countBombs(x1,x2,x3,x4,x5,x6)==0:
        if x1<a-1 and openTiles[x1+1][x2][x3][x4][x5][x6]==-1:
            openTile(x1+1,x2,x3,x4,x5,x6)
        if x1>0 and openTiles[x1-1][x2][x3][x4][x5][x6]==-1:
            openTile(x1-1,x2,x3,x4,x5,x6)
        if x2<b-1 and openTiles[x1][x2+1][x3][x4][x5][x6]==-1:
            openTile(x1,x2+1,x3,x4,x5,x6)
        if x2>0 and openTiles[x1][x2-1][x3][x4][x5][x6]==-1:
            openTile(x1,x2-1,x3,x4,x5,x6)
        if x3<c-1 and openTiles[x1][x2][x3+1][x4][x5][x6]==-1:
            openTile(x1,x2,x3+1,x4,x5,x6)
        if x3>0 and openTiles[x1][x2][x3-1][x4][x5][x6]==-1:
            openTile(x1,x2,x3-1,x4,x5,x6)
        if x4<d-1 and openTiles[x1][x2][x3][x4+1][x5][x6]==-1:
            openTile(x1,x2,x3,x4+1,x5,x6)
        if x4>0 and openTiles[x1][x2][x3][x4-1][x5][x6]==-1:
            openTile(x1,x2,x3,x4-1,x5,x6)
        if x5<e-1 and openTiles[x1][x2][x3][x4][x5+1][x6]==-1:
            openTile(x1,x2,x3,x4,x5+1,x6)
        if x5>0 and openTiles[x1][x2][x3][x4][x5-1][x6]==-1:
            openTile(x1,x2,x3,x4,x5-1,x6)
        if x6<f-1 and openTiles[x1][x2][x3][x4][x5][x6+1]==-1:
            openTile(x1,x2,x3,x4,x5,x6+1)
        if x6>0 and openTiles[x1][x2][x3][x4][x5][x6-1]==-1:
            openTile(x1,x2,x3,x4,x5,x6-1)
    else:
        printNum(x1,x2,x3,x4,x5,x6)

def mark(x1,x2,x3,x4,x5,x6):
    pygame.draw.rect(screen,markColour,(recs[x1][x2][x3][x4][x5][x6].left,recs[x1][x2][x3][x4][x5][x6].top,tileWidth,tileWidth))

def unmark(x1,x2,x3,x4,x5,x6):
    pygame.draw.rect(screen,tileColour,(recs[x1][x2][x3][x4][x5][x6].left,recs[x1][x2][x3][x4][x5][x6].top,tileWidth,tileWidth))

random.seed()
for j in range(0,bombs):
    putBomb()

for a1 in range(0,a):
    recs5=[]
    for a2 in range(0,b):
        recs4=[]
        for a3 in range(0,c):
            recs3=[]
            for a4 in range(0,d):
                recs2=[]
                for a5 in range(0,e):
                    recs1=[]
                    for a6 in range(0,f):
                        y=pygame.Rect(sx,sy,tileWidth,tileWidth)
                        recs1.append(y)
                        pygame.draw.rect(screen,tileColour,(sx,sy,tileWidth,tileWidth))
                        sx=sx+tileWidth+1
                    recs2.append(recs1)
                    sx=sx+2
                recs3.append(recs2)
                sx=sx+3
            recs4.append(recs3)
            sx=(width-tileWidth*27-52)/2
            sy=sy+tileWidth+1
        recs5.append(recs4)
        sy=sy+2
    recs.append(recs5)
    sy=sy+3
pygame.display.flip()

pygame.display.set_caption("Epic 6D minesweeper")
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1 or event.button==2 or event.button==3:
                clil,clih=event.pos
                for x1 in range(0,a):
                    for x2 in range(0,b):
                        for x3 in range(0,c):
                            for x4 in range(0,d):
                                for x5 in range(0,e):
                                    for x6 in range(0,f):
                                        if recs[x1][x2][x3][x4][x5][x6].left<=clil and clil<recs[x1][x2][x3][x4][x5][x6].left+tileWidth and recs[x1][x2][x3][x4][x5][x6].top<=clih and clih<recs[x1][x2][x3][x4][x5][x6].top+tileWidth and openTiles[x1][x2][x3][x4][x5][x6]==-1:
                                            if event.button==1:
                                                if Matrix[x1][x2][x3][x4][x5][x6]==1:
                                                    print('You lose!')
                                                    sys.exit()
                                                else:
                                                    openTile(x1,x2,x3,x4,x5,x6)
                                                    if closedTiles==bombs:
                                                        print('You won!')
                                                        sys.exit()
                                                    pygame.display.flip()
                                            elif event.button==3:
                                                mark(x1,x2,x3,x4,x5,x6)
                                                pygame.display.flip()
                                            else:
                                                unmark(x1,x2,x3,x4,x5,x6)
                                                pygame.display.flip()
