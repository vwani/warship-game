# import modules
import pygame
import sys
import math

# initialise pygame
pygame.init()

# screen dimensions
res = (600, 375)

# create screen
screen = pygame.display.set_mode(res)

# icon
icon = pygame.image.load('F:\\Vinaya\\Python Projects\\War Ship\\Media\\icon.png') 
pygame.display.set_icon(icon)

# title
pygame.display.set_caption('SPACE ATTACK')

# background
background = pygame.image.load('F:\\Vinaya\\Python Projects\\War Ship\\Media\\background.png')

# music

''' background music '''
pygame.mixer.music.load('F:\\Vinaya\\Python Projects\\War Ship\\Media\\background.mp3')
pygame.mixer.music.play(-1)

''' sound effects '''
shoot = pygame.mixer.Sound('F:\\Vinaya\\Python Projects\\War Ship\\Media\\shoot.wav')
explosion = pygame.mixer.Sound('F:\\Vinaya\\Python Projects\\War Ship\\Media\\explosion.wav')
gameover = pygame.mixer.Sound('F:\\Vinaya\\Python Projects\\War Ship\\Media\\gameover.wav')

# font
healthfont = pygame.font.Font('freesansbold.ttf', 24)
endfont = pygame.font.Font('freesansbold.ttf', 50)

# player1
Player1Img = pygame.image.load('F:\\Vinaya\\Python Projects\\War Ship\\Media\\player1.png')

''' player1 movement coordinates '''

Player1X = 0
Player1Y = 187.5
Player1ChangeX = 0
Player1ChangeY = 0

Player1Health = 5

def player1(x, y):
    screen.blit(Player1Img, (x, y))

# health 1
def health1(health, x, y):
    Health1 = healthfont.render('Health : '+str(health), True, (225, 225, 225))
    screen.blit(Health1, (x, y))

# player2
Player2Img = pygame.image.load('F:\\Vinaya\\Python Projects\\War Ship\\Media\\player2.png')

''' player2 movement coordinates '''

Player2X = 536
Player2Y = 187.5
Player2ChangeX = 0
Player2ChangeY = 0

Player2Health = 5

def player2(x, y):
    screen.blit(Player2Img, (x, y))

# health 2
def health2(health, x, y):
    Health2 = healthfont.render('Health : '+str(health), True, (225, 225, 225))
    screen.blit(health, (x, y))

# bullet1
Bullet1Img = pygame.image.load('F:\\Vinaya\\Python Projects\\War Ship\\Media\\bullet1.png')

''' bullet1 movement coordinates '''

Bullet1X = -1000
Bullet1Y = -1000
Bullet1ChangeX = 0
Bullet1ChangeY = 0

Bullet1State = False

def bullet1(x, y):
    if Bullet1State == True:
     screen.blit(Bullet1Img, (x+36, y+15))

# bullet2
Bullet2Img = pygame.image.load('F:\\Vinaya\\Python Projects\\War Ship\\Media\\bullet2.png')

''' bullet2 movement coordinates '''

Bullet2X = -1000
Bullet2Y = -1000
Bullet2ChangeX = 0
Bullet2ChangeY = 0

Bullet2State = False

def bullet2(x, y):
    if Bullet2State == True:
        screen.blit(Bullet2Img, (x, y+15))

# winner, loser
def end(status1, status2):
    screen.blit(endfont.render('You '+status1, True, (225, 0, 0)), (30, 175))
    screen.blit(endfont.render('You '+status2, True, (225, 0, 0)), (325, 175))  

# collision
def collision(PlayerX, PlayerY, BulletX, BulletY):
    dist = math.hypot(PlayerX - BulletX, PlayerY - BulletY)
    
    if dist < 45:
        return True
    else:
        return False

# main loop
running = True

while running:

    # event check
    for event in pygame.event.get():

        # exit loop
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # key press 
        if event.type == pygame.KEYDOWN:
            
            # player movement
            
            # player 1
            if event.key == pygame.K_w:
                Player1ChangeY = -0.1
                Player1ChangeX = 0

            elif event.key == pygame.K_s:
                Player1ChangeY = 0.1
                Player1ChangeX = 0

            if event.key == pygame.K_d:
                Player1ChangeX = 0.1
                Player1ChangeY = 0

            elif event.key == pygame.K_a:
                Player1ChangeX = -0.1
                Player1ChangeY = 0

            # player 2
            if event.key == pygame.K_UP:
                Player2ChangeY = -0.1
                Player2ChangeX = 0

            elif event.key == pygame.K_DOWN:
                Player2ChangeY = 0.1
                Player2ChangeX = 0

            if event.key == pygame.K_RIGHT:
                Player2ChangeX = 0.1
                Player2ChangeY = 0

            elif event.key == pygame.K_LEFT:
                Player2ChangeX = -0.1
                Player2ChangeY = 0

            # bullet movement

            # bullet 1
            if Bullet1State == False:
                if event.key == pygame.K_SPACE:
                    Bullet1X = Player1X
                    Bullet1Y = Player1Y
                    Bullet1ChangeX = 0.2
                    Bullet1State = True
                    shoot.play()

            # bullet 2
            if Bullet2State == False:
                if event.key == pygame.K_KP0:
                    Bullet2X = Player2X
                    Bullet2Y = Player2Y
                    Bullet2ChangeX = -0.2
                    Bullet2State = True
                    shoot.play()

    # background
    
    ''' background color '''
    screen.fill((0, 0, 225))
    
    ''' background image '''
    screen.blit(background, (0, 0))

    # player 1 movement
    Player1X += Player1ChangeX
    Player1Y += Player1ChangeY

    ''' establishing boundary '''
    
    if Player1X <= 0:
        Player1X = 0

    elif Player1X >= 236:
        Player1X = 236

    if Player1Y <= 25:
        Player1Y = 25   

    elif Player1Y >= 311:
        Player1Y = 311
        
    # player 2 movement
    Player2X += Player2ChangeX
    Player2Y += Player2ChangeY

    ''' establishing boundary '''
    
    if Player2X >= 536:
        Player2X = 536

    elif Player2X <= 300:
        Player2X = 300

    if Player2Y <= 25:
        Player2Y = 25

    elif Player2Y >= 311:
        Player2Y = 311

    # bullet 1 movement
    Bullet1X += Bullet1ChangeX

    ''' establishing boundary '''
    
    if Bullet1X >= 576:
        Bullet1State = False

    # bullet 2 movement
    Bullet2X += Bullet2ChangeX
    
    ''' establishing boundary '''
    
    if Bullet2X <= 0:
        Bullet2State = False

    # collision
    collide1 = collision(Player1X, Player1Y, Bullet2X, Bullet2Y)
    collide2 = collision(Player2X, Player2Y, Bullet1X, Bullet1Y)
    
    if collide1:
        Bullet2State = False
        Bullet2X = -1000
        Bullet2Y = -1000
        Player1Health -= 1
        explosion.play()
    
    elif collide2:
        Bullet1State = False
        Bullet1X = -1000
        Bullet1Y = -1000
        Player2Health -= 1
        explosion.play()
   
    # zero health
    if Player1Health == 0:
        Playert1X = -1000
        Player1Y = -1000
        Playert2X = -1000
        Player2Y = -1000
        end('Lose..', 'Win!!')
        pygame.mixer.music.fadeout(2000)
        gameover.play()
        running = False

    elif Player2Health == 0:
        Playert1X = -1000
        Player1Y = -1000
        Playert2X = -1000
        Player2Y = -1000
        end('Win!!', 'Lose..')
        pygame.mixer.music.fadeout(2000)
        gameover.play()
        running = False

    # text
    health1(Player1Health, 10, 0)
    health1(Player2Health, 475, 0)

    # motion
    player1(Player1X, Player1Y)
    player2(Player2X, Player2Y)
    bullet1(Bullet1X, Bullet1Y)
    bullet2(Bullet2X, Bullet2Y)

    # update screen
    pygame.display.update()

# loop to quit game after end
while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
