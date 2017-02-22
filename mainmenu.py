import pygame, time, random, showdata, login
from pygame.locals import *

pygame.init()

displayWidth = 480
displayHeight = 640
menuImg = pygame.image.load('images/menu.png')
skorImg = pygame.image.load('images/skor.png')
guessImg = pygame.image.load('images/guess.png')
charImg = pygame.image.load('images/char.png')
collImg = pygame.image.load('images/collect.png')
selectSound = pygame.mixer.Sound("sounds/select.wav")
correctSound = pygame.mixer.Sound("sounds/correct.wav")
falseSound = pygame.mixer.Sound("sounds/false.wav")
timeoutSound = pygame.mixer.Sound("sounds/timeout.ogg")
cdSound = pygame.mixer.Sound("sounds/countdown.wav")
char1 = pygame.image.load('images/ayah.png')
char2 = pygame.image.load('images/dokter.png')
char3 = pygame.image.load('images/ilmuan.png')

black = (0,0,0)
white = (255,255,255)
grey = (240,240,240)
red = (255,0,0)
green = (0,255,0)
limeGreen = (50,205,50)
darkGreen = (45,168,4)
lightBlue = (33,150,243)
hoverBlue = (23,147,201)
darkBlue = (39,77,165)

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Tebak Lagu Kita')
clock = pygame.time.Clock()

def textObjects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def menuButton(text, x, y, h, w, c, sc, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+50 > mouse[1] > y:
        pygame.draw.rect(gameDisplay, sc, (x,y,w,h))
        if click[0] == 1 and action != None:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(selectSound)
            action()
            
    else:
        pygame.draw.rect(gameDisplay, c, (x,y,w,h))
        
    buttonText = pygame.font.Font("fonts/Roboto-Bold.ttf",20)
    textSurf, textRect = textObjects(text, buttonText, white)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def gameMenu():
    menu = True

    while menu:
        gameDisplay.blit(menuImg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                pygame.quit()
                quit()

            menuButton("Skor", 80, 513, 45, 100, lightBlue, hoverBlue, skorDisplay)
            menuButton("Main", 195, 513, 45, 100, lightBlue, hoverBlue, selectChar)
            menuButton("Koleksi", 307, 513, 45, 100, lightBlue, hoverBlue, collection)
            menuButton("Credits", 195, 575, 45, 100, lightBlue, hoverBlue, login.CreditsWindow)

            pygame.display.update()
            clock.tick(30)

def skorDisplay():
    skor = True

    while skor:
        gameDisplay.blit(skorImg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                skor = False
                pygame.quit()
                quit()

            menuButton("<", 12, 10, 33, 32, lightBlue, hoverBlue, gameMenu)

            scoreText = pygame.font.Font("fonts/Roboto-Medium.ttf",100)
            textSurf, textRect = textObjects(str(showdata.getScore()), scoreText, black)
            textRect.center = (230, 420)
            gameDisplay.blit(textSurf, textRect)

            scoreText = pygame.font.Font("fonts/Pusab.otf",28)
            textSurf, textRect = textObjects(str(showdata.getLevel()), scoreText, darkBlue)
            textRect.center = (368, 230)
            gameDisplay.blit(textSurf, textRect)

            pygame.display.update()
            clock.tick(30)

def collection():
    collect = True
    while collect:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                collect = False
                pygame.quit()
                quit()

            gameDisplay.blit(collImg, (0,0))
            char1stat = int(showdata.readCharStat(1))
            char2stat = int(showdata.readCharStat(2))
            char3stat = int(showdata.readCharStat(3))
            
            if char1stat == 1:
                char1 = pygame.image.load(showdata.readCCharLoc(1)).convert_alpha()
            else:
                char1 = pygame.image.load(showdata.readBWCharLoc(1)).convert_alpha()

            if char2stat == 1:
                char2 = pygame.image.load(showdata.readCCharLoc(2)).convert_alpha()
            else:
                char2 = pygame.image.load(showdata.readBWCharLoc(2)).convert_alpha()

            if char3stat == 1:
                char3 = pygame.image.load(showdata.readCCharLoc(3)).convert_alpha()
            else:
                char3 = pygame.image.load(showdata.readBWCharLoc(3)).convert_alpha()
                    
            gameDisplay.blit(char1, (20,400))
            gameDisplay.blit(char2, (170,400))
            gameDisplay.blit(char3, (320,400))
            menuButton("<", 12, 10, 33, 32, lightBlue, hoverBlue, gameMenu)
            
            pygame.display.update()
            clock.tick(30)

def multipleChoice(text, x, y, h, w, c, sc, fontcolor, sfontcolor, title, key, keySong, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+50 > mouse[1] > y:
        pygame.draw.rect(gameDisplay, sc, (x,y,w,h))
        fontcolor = sfontcolor
        if click[0] == 1 and action != None:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(selectSound)
            action(text, key, title, keySong)
            
    else:
        pygame.draw.rect(gameDisplay, c, (x,y,w,h))
        
    buttonText = pygame.font.Font("fonts/Roboto-Medium.ttf",20)
    textSurf, textRect = textObjects(text, buttonText, fontcolor)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)

def selectChar():
    selchar = True
    while selchar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                selchar = False
                pygame.quit()
                quit()

            gameDisplay.blit(charImg, (0,0))
            char1stat = int(showdata.readCharStat(1))
            char2stat = int(showdata.readCharStat(2))
            char3stat = int(showdata.readCharStat(3))
            
            if char1stat == 1:
                char1 = pygame.image.load(showdata.readCCharLoc(1)).convert_alpha()
                char1title = showdata.readCharTitle(1)
                showdata.chooseChar(1)
                menuButton(char1title, 18, 480, 40, 140, lightBlue, hoverBlue, countdown)
            else:
                char1 = pygame.image.load(showdata.readBWCharLoc(1)).convert_alpha()
                char1title = "Terkunci"
                menuButton(char1title, 18, 480, 40, 140, lightBlue, lightBlue)

            if char2stat == 1:
                char2 = pygame.image.load(showdata.readCCharLoc(2)).convert_alpha()
                char2title = showdata.readCharTitle(2)
                showdata.chooseChar(2)
                menuButton(char2title, 169, 480, 40, 140, lightBlue, hoverBlue, countdown)
            else:
                char2 = pygame.image.load(showdata.readBWCharLoc(2)).convert_alpha()
                char2title = "Terkunci"
                menuButton(char2title, 169, 480, 40, 140, lightBlue, lightBlue)

            if char3stat == 1:
                char3 = pygame.image.load(showdata.readCCharLoc(3)).convert_alpha()
                char3title = showdata.readCharTitle(3)
                showdata.chooseChar(3)
                menuButton(char3title, 321, 480, 40, 140, lightBlue, hoverBlue, countdown)
            else:
                char3 = pygame.image.load(showdata.readBWCharLoc(3)).convert_alpha()
                char3title = "Terkunci"
                menuButton(char3title, 321, 480, 40, 140, lightBlue, lightBlue)
                    
            gameDisplay.blit(char1, (20,330))
            gameDisplay.blit(char2, (170,330))
            gameDisplay.blit(char3, (320,330))
            menuButton("<", 12, 10, 33, 32, lightBlue, hoverBlue, gameMenu)
            
            pygame.display.update()
            clock.tick(30)

def countdown():
    cd = True
    time = 4 
    pygame.time.set_timer(USEREVENT + 1, 1000)
    gameDisplay.blit(pygame.image.load("images/3.png"), (0,0))
    countImg = ["images/0.png","images/0.png","images/1.png","images/2.png"]
    pygame.mixer.Sound.play(cdSound)
    while cd:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                cd = False
                pygame.quit()
                quit()
                
            if event.type == USEREVENT + 1:
                time -= 1
                gameDisplay.blit(pygame.image.load(str(countImg[time])), (0,0))

            if time == 0:
                cd = False
                guessDisplay()

            pygame.display.update()
            clock.tick(30)

def timeOut(keySong):
    timeWarn = True
    gameDisplay.blit(pygame.image.load('images/timeout.png'), (0,0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(timeoutSound)
    while timeWarn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    timeWarn = False
                    pygame.quit()
                    quit()

            scoreText = pygame.font.Font("fonts/Roboto-Medium.ttf",20)    
            textSurf, textRect = textObjects(showdata.readTitle(keySong), scoreText, white)
            textRect.center = (238, 400)
            gameDisplay.blit(textSurf, textRect)
            menuButton("Main Lagi!", 170, 428, 40, 140, limeGreen, darkGreen, guessDisplay)
            menuButton("Berhenti", 170, 488, 40, 140, lightBlue, hoverBlue, gameMenu)
            pygame.display.update()
            clock.tick(30)

def generateQuestion():
    question = random.sample(range(1,13), 4)
    keySong = random.choice(question)
    key = question.index(keySong)
    songLoc = showdata.readLoc(keySong)

    i = 0
    for x in question:
        question[i] = showdata.readTitle(x)
        i += 1
        
    pygame.mixer.music.load(songLoc)
    pygame.mixer.music.play(1)
    return question, key, keySong

def checkAnswer(answer, key, title, keySong):
    checkAns = True
    if title.index(answer) == key:
        gameDisplay.blit(pygame.image.load('images/true.png'), (0,0))
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(correctSound)
        showdata.addScore(str(10))
        
        scoreText = pygame.font.Font("fonts/Roboto-Medium.ttf",18)
        textSurf, textRect = textObjects(str(showdata.getScore()), scoreText, white)
        textRect.center = (300, 390)
        gameDisplay.blit(textSurf, textRect)
        
    else:
        gameDisplay.blit(pygame.image.load('images/false.png'), (0,0))
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(falseSound)
        
        scoreText = pygame.font.Font("fonts/Roboto-Medium.ttf",20)
        textSurf, textRect = textObjects(showdata.readTitle(keySong), scoreText, white)
        textRect.center = (238, 400)
        gameDisplay.blit(textSurf, textRect)

    while checkAns:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    checkAns = False
                    pygame.quit()
                    quit()
            menuButton("Main Lagi!", 170, 428, 40, 140, limeGreen, darkGreen, guessDisplay)
            menuButton("Berhenti", 170, 488, 40, 140, lightBlue, hoverBlue, gameMenu)
            pygame.display.update()
            clock.tick(30)
             
def guessDisplay():
    guess = True
    time = 10 
    pygame.time.set_timer(USEREVENT + 1, 1000)
    title, key, keySong = generateQuestion()
    gameDisplay.blit(guessImg, (0,0))
    selectedChar = int(showdata.retrieveChar())
    if selectedChar == 1:
        gameDisplay.blit(char1.convert_alpha(), (335,430))
    elif selectedChar == 2:
        gameDisplay.blit(char2.convert_alpha(), (335,430))
    else:
        gameDisplay.blit(char3.convert_alpha(), (335,430))

    while guess:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    guess = False
                    pygame.quit()
                    quit()

            if event.type == USEREVENT + 1:
                time -= 1

            if time == 0:
                guess = False
                timeOut(keySong)
                
            multipleChoice(title[0], 20, 310, 45, 275, grey, white, black, limeGreen, title, key, keySong, checkAnswer)
            multipleChoice(title[1], 20, 370, 45, 275, grey, white, black, limeGreen, title, key, keySong, checkAnswer)
            multipleChoice(title[2], 20, 430, 45, 275, grey, white, black, limeGreen, title, key, keySong, checkAnswer)
            multipleChoice(title[3], 20, 490, 45, 275, grey, white, black, limeGreen, title, key, keySong, checkAnswer)
            
            pygame.display.update()
            clock.tick(30)

gameMenu()
pygame.quit()
quit()
