import pygame
pygame.init()
import random
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080,520))
screen.fill("black")

pygame.display.set_caption("המירוץ למבצר")

pygame.display.set_icon(pygame.image.load("pics/game_Icon.png"))

    
y_1 = -520
y_2 = 0
lives = 3
matsCount = 0
matsSpawned = 0



def exit_game():
    pygame.quit()  # Quit the game
    exit()  # Exit the program
    
def game_over_screen():
    font = pygame.font.Font("ganclm_bold-webfont.woff", 300)
    gameOverText = font.render("תלספנ", True, "darkred")
    screen.blit(gameOverText, (50, 120))  # Display "You Lose" at a position
    pygame.display.flip()
    
    pygame.time.delay(4000)  # Show the "You Lose" text for 2 seconds

    exit_game()  # Call function to exit or restart game
    
def beforeRun():
    font = pygame.font.Font("ganclm_bold-webfont.woff", 50)
    runBackground1= pygame.image.load("pics/Run_Screen_Background.jpg")
    runBackground1 = pygame.transform.scale(runBackground1, (1080,520))
    paths1 = pygame.image.load("pics/paths.png")
    paths1 = pygame.transform.scale(paths1, (595,520))
    screen.blit(runBackground1,(0,0))
    screen.blit(paths1,(260,0))
    window = pygame.image.load("pics/beforeRunPage.png")
    window = pygame.transform.scale(window,(1080,500))
    screen.blit(window, (0,0))
    
    btn0 = pygame.draw.rect(screen, "orange", (300,380, 200,50),0,100)
    btn1 = pygame.draw.rect(screen, "orange", (580,380, 200,50),0,100)
    textBoy = font.render("ןב", True, "white")
    textGirl = font.render("תב", True, "white")
    screen.blit(textBoy, (370,380))
    screen.blit(textGirl, (650,380))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if btn0.collidepoint(mouse_pos):
                    runScreen(0)
                if btn1.collidepoint(mouse_pos):
                    runScreen(1)
        pygame.display.flip()
        
def runScreen(gen):
    go = pygame.mixer.Sound("sounds/GO.mp3")
    go.play()
    bgMusic = pygame.mixer.Sound("sounds/Running_Background_Music.mp3")
    bgMusic.play(-1)
    lose = pygame.mixer.Sound("sounds/Lose_Sound.mp3")
    collectSound = pygame.mixer.Sound("sounds/Collect.mp3")
    hitSound = pygame.mixer.Sound("sounds/Hit_Sound.mp3")
    
    font = pygame.font.Font("ganclm_bold-webfont.woff", 50)




    global y_1, y_2, lives, matsSpawned, matsCount

    
    item_images = [
        (pygame.image.load("pics/needs/life/food1.png"), "food"),
        (pygame.image.load("pics/needs/life/food2.png"), "food"),
        (pygame.image.load("pics/needs/life/food3.png"), "food"),
        (pygame.image.load("pics/needs/life/food4.png"), "food"),
        (pygame.image.load("pics/needs/life/food5.png"), "food"),
        (pygame.image.load("pics/needs/life/food6.png"), "food"),
        (pygame.image.load("pics/needs/life/food7.png"), "food"),
        (pygame.image.load("pics/needs/life/water.png"), "food"),
        
        (pygame.image.load("pics/needs/mats/bricks.png"), "mats"),
        (pygame.image.load("pics/needs/mats/metal.png"), "mats"),
        (pygame.image.load("pics/needs/mats/wood.png"), "mats"),
        (pygame.image.load("pics/needs/mats/bricks.png"), "mats"),
        (pygame.image.load("pics/needs/mats/metal.png"), "mats"),
        (pygame.image.load("pics/needs/mats/wood.png"), "mats"),
        
        (pygame.image.load("pics/obstacles/clothes_obsticle.png"),"obs"),
        (pygame.image.load("pics/obstacles/sand_obsticle.png"),"obs"),
        (pygame.image.load("pics/obstacles/stone_obsticle.png"),"obs"),
        (pygame.image.load("pics/obstacles/clothes_obsticle.png"),"obs"),
        (pygame.image.load("pics/obstacles/sand_obsticle.png"),"obs"),
        (pygame.image.load("pics/obstacles/stone_obsticle.png"),"obs"),
        
    ]

    item_images = [(pygame.transform.scale(image[0], (120, 120)), image[1]) for image in item_images]
        
    # Store items' properties
    items_pos = []
    add_interval = 1000  # 1000 milliseconds = 1 second
    last_add_time = 0

    def add_new_item():
        global matsSpawned
        # Randomize the x position between 0 and 500 so items don't all fall from the same place
        item_x = random.choice([300,495,690])
        item_y = -100  # Starting from the top of the screen
        item_image = random.choice(item_images)  # Randomly choose an item image
        items_pos.append((item_x, item_y, item_image))
        if item_image[1] == "mats":
            matsSpawned += 1


    x_player = 495
    path = "Mid"


    runBackground1= pygame.image.load("pics/Run_Screen_Background.jpg")
    runBackground1 = pygame.transform.scale(runBackground1, (1080,520))
    runBackground2= pygame.image.load("pics/Run_Screen_Background.jpg")
    runBackground2 = pygame.transform.scale(runBackground2, (1080,520))

    paths1 = pygame.image.load("pics/paths.png")
    paths1 = pygame.transform.scale(paths1, (595,520))
    paths2 = pygame.image.load("pics/paths.png")
    paths2 = pygame.transform.scale(paths2, (600,520))

    player1 = pygame.image.load("pics/Runner1.png")
    player1 = pygame.transform.scale(player1, (130,170))
    player2 = pygame.image.load("pics/Runner2.png")
    player2 = pygame.transform.scale(player2, (130,170))

    players = [player1,player2]
    time = 0

    # side1 = pygame.image.load("pics/sides.png")
    # side1 = pygame.transform.scale(side1, (100,520))
    # side2 = pygame.image.load("pics/sides.png")
    # side2 = pygame.transform.scale(side2, (100,520))
    # side2 = pygame.transform.flip(side2, True, False)
    
    
    def colideHappen(rightX):
        global lives, matsCount
        for item in items_pos:
            if item[0] == rightX and item[1] < 480 and item[1] > 520 - 250:
                print(lives)
                items_pos.remove(item)                             
                if item[2][1] == "mats":
                    collectSound.play()
                    matsCount+=1
                if item[2][1] == "obs":
                    hitSound.play()
                    lives-=1
                if item[2][1] == "food" and lives<3:
                    collectSound.play()
                    lives+=1    
    
    while True:
        time+=1
        screen.blit(runBackground1,(0,y_1))
        screen.blit(runBackground2,(0,y_2))
        screen.blit(paths1,(260,y_1))
        screen.blit(paths2,(257,y_2))
        needs = font.render(f"10/{matsCount} םירמוח", True, "white")
        livesCheck = font.render(f"{lives} :םייח רפסמ", True, "white")
        screen.blit(needs, (750,0))
        screen.blit(livesCheck, (750,50))
        y_1+=2
        y_2+=2
        if y_1>=520:
            y_1=-520
        if y_2>=520:
            y_2=-520
        if path == "Mid":
            x_player=495
        elif path == "Left":
            x_player = 300
        else:
            x_player = 690

        
        

        
        screen.blit(players[gen],(x_player,320))
        if time%35==0:
            players[gen] = pygame.transform.flip(players[gen], True, False)


        # screen.blit(side1, (0,0))
        # screen.blit(side2, (1080,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if path == "Right":                        
                    path = "Mid"
                elif path == "Mid":
                    path = "Left"
            elif keys[pygame.K_RIGHT]:
                if path == "Left":
                    path = "Mid"
                elif path == "Mid":
                    path = "Right"

        clock.tick(600)
 
 # Add new item every 'add_interval' milliseconds
        current_time = pygame.time.get_ticks()
        if current_time - last_add_time > add_interval:
            add_new_item()
            last_add_time = current_time  # Update the last add time

        # Update the position of each item and remove items that have gone off-
        
        for i in range(len(items_pos)):
            items_pos[i] = (items_pos[i][0], items_pos[i][1] + 2, items_pos[i][2])  # Move down
            
        items_pos = [item for item in items_pos if item[1] < 520]  # Keep only items still visible

        # Draw the items
        if matsSpawned<12:
            for pos in items_pos:
                screen.blit(pos[2][0], (pos[0], pos[1]))  # Draw the item with dynamic image
        else:
            bgMusic.stop()
            baseScreen()
        
        if lives == 0:
            bgMusic.stop()
            lose.play()
            game_over_screen()  # Show the game over screen and pause
        
        if x_player == 300:
            colideHappen(300)
        elif x_player == 495:
            colideHappen(495)
        else:
            colideHappen(690)
                           
        pygame.display.flip()
        

def build(persentage):
    base = pygame.image.load(f"pics/Building_{persentage}%.png")
    base = pygame.transform.scale(base, (450,450))
    return base
    
    
def baseScreen():
    drama = pygame.mixer.Sound("sounds/Enough_Mats_Check.mp3")
    drama.play()
    Win = pygame.mixer.Sound("sounds/Win_Sound.mp3")
    lose = pygame.mixer.Sound("sounds/Lose_Sound.mp3")
    p = 25 if 0 <= matsCount < 3 else 50 if 2 < matsCount < 6 else 75 if 5 < matsCount < 10 else 100
    font = pygame.font.Font("ganclm_bold-webfont.woff",20)
    text1 = font.render(f"םלש {p}% אוה ךלש רצבמה", True, "darkred")
    ans = "תחצינ!" if p >=75 else "...תדספה"
    text2 = font.render(ans, True, "darkred")

    pygame.time.delay(1000)
    bgPic = pygame.image.load("pics/Fortres_Background.jpg")
    bgPic = pygame.transform.scale(bgPic, (1080,520))
    current_base = build(p)
    dust = pygame.image.load("pics/Bluilding_Dust.png")
    dust = pygame.transform.scale(dust, (600,600))
    buildSound = pygame.mixer.Sound("sounds/Building_Sound.mp3")
    buildSound.play()
    for i in range(11):
        screen.blit(bgPic,(0,0))
        dust = pygame.transform.scale(dust, (600,600))
        screen.blit(dust,(220,-20))
        pygame.time.delay(300)
        pygame.display.flip()     
        screen.blit(bgPic,(0,0))
        dust = pygame.transform.scale(dust, (650,650))
        screen.blit(dust,(200,-35))
        pygame.time.delay(300)
        pygame.display.flip()
    if p>=75:
        Win.play()
    else:
        lose.play()
      
    while True:
        screen.blit(bgPic,(0,0))
        screen.blit(current_base, (325, 30))
        screen.blit(text1, (750,40))
        screen.blit(text2, (250,40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.flip()
        

btnRect = pygame.Rect(400,350, 300,100)
def startScreen():

    #background pic
    startBackground = pygame.image.load("pics/Start_Screen_Background.jpg")
    startBackground = pygame.transform.scale(startBackground, (1080,520))
    screen.blit(startBackground,(0,0))

    #background music
    bgMuisc = pygame.mixer.Sound("sounds/Start_Screen_Background_Muisc.mp3")
    bgMuisc.play(-1)

    #fonts
    font1 = pygame.font.Font("ganclm_bold-webfont.woff", 50)
    font2Border = pygame.font.Font("ganclm_bold-webfont.woff", 155)
    font2 = pygame.font.Font("ganclm_bold-webfont.woff", 150)
    font3Border = pygame.font.Font("ganclm_bold-webfont.woff", 205)
    font3 = pygame.font.Font("ganclm_bold-webfont.woff", 200)

    #gmae title
    titleText1Border = font2Border.render("ץורימה", True, "white")
    titleText1 = font2.render("ץורימה", True, "orange")
    titleText2Border = font3Border.render("רצבמל", True, "brown")
    titleText2 = font3.render("רצבמל", True, "orange")

    #start button
    startBtnText = font1.render("לחתה", True, "brown")
    startBtnTextShadow = font1.render("לחתה", True, "black")
    pygame.draw.rect(screen,"orange", btnRect,0,100)
    pygame.draw.rect(screen,"brown", (400,350, 300,100),5,100)

    #print text's
    screen.blit(titleText1Border, (275,0))
    screen.blit(titleText1, (285,3))
    screen.blit(titleText2Border, (200,100))
    screen.blit(titleText2, (207,103))
    screen.blit(startBtnTextShadow,(479,375))
    screen.blit(startBtnText,(477,372))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btnRect.collidepoint(event.pos):
                    bgMuisc.stop()
                    beforeRun()
        pygame.display.flip()

startScreen()


