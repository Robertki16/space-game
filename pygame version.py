import pygame, os, random
from pygame.locals import *
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def game(life =3, time = 0):
    
    class Settings():
        def __init__(self):
            self.SCREEN_WIDTH = 1024
            self.SCREEN_HEIGHT = 720
            self.scorefont = pygame.font.Font(resource_path('images/arcadeclassic.ttf'),20)
            self.text_colour = (255,255,0)
            self.started = False
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.image.load(resource_path('images/'+random.choice(['star1.png','star2.png','star3.png','star4.png','star5.png','star6.png']))).convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            if settings.started:
                self.rect = self.surf.get_rect(center=(random.randint(-500, settings.SCREEN_WIDTH+500),random.randint(-500, -100)))
            else:
                self.rect = self.surf.get_rect(center=(random.randint(-500, settings.SCREEN_WIDTH+500),random.randint(0, settings.SCREEN_HEIGHT-(settings.SCREEN_HEIGHT/4))))
            self.speed = random.randint(2, 5)
            
        def update(self, pressed_keys):
            self.rect.move_ip(0, self.speed)
            if self.rect.top > settings.SCREEN_HEIGHT:
                self.kill()
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(0.5*self.speed, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(-0.5*self.speed, 0)
            if player.angle != 10 and pressed_keys[K_LEFT] == True:
                rot_angle = (player.angle - 10) *-1
                player.rotate(10)
                player.angle = 10
            if player.angle != -10 and pressed_keys[K_RIGHT] == True:
                rot_angle = (player.angle + 10) *-1
                player.rotate(rot_angle)
                player.angle = -10
            if pressed_keys[K_RIGHT] == False and pressed_keys[K_LEFT] == False:
                rot_angle = (player.angle) *-1
                player.rotate(rot_angle)
                player.angle = 0
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            self.surf = pygame.image.load(resource_path('images/cropped_ship.png')).convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect(center=(settings.SCREEN_WIDTH/2,settings.SCREEN_HEIGHT-5))
            self.angle = 0
        def rotate(self, angle):
            self.surf = pygame.transform.rotate(self.surf, angle)
            self.rect = self.surf.get_rect(center=(settings.SCREEN_WIDTH/2,settings.SCREEN_HEIGHT-5))
    class Score():
        def __init__(self):
            super(Score, self).__init__()
            self.score = 0
            self.score_text = settings.scorefont.render('Score '+ str(self.score) , True , settings.text_colour) 
            self.score_text_rect = self.score_text.get_rect(topleft = (20,20))
        def update(self, time):
            self.score = (str(int(round(((round(time,2))*10000),2))))
            self.score_text = settings.scorefont.render('Score '+ str(self.score) , True , settings.text_colour) 
            self.score_text_rect = self.score_text.get_rect(topleft = (20,20))
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), pygame.FULLSCREEN) 
          
    pygame.display.set_icon(pygame.image.load(resource_path('images/ship.png')))
    pygame.display.set_caption("Space Game")
    pygame.display.get_active()
    screen.fill((0, 0, 0))

    player = Player()
    score = Score()
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    for i in range(50):
        new_enemy = Enemy()
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
    #time = 0
    running = True
    clock = pygame.time.Clock()
    

    while running:
        settings.started = True
        if len(enemies.sprites()) < 50:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            elif event.type == QUIT:
                running = False
        score.update(time)
 
        pressed_keys = pygame.key.get_pressed()
        enemies.update(pressed_keys)
        screen.fill((0, 0, 0))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        screen.blit(player.surf, player.rect)
        screen.blit(score.score_text ,score.score_text_rect)
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False
        pygame.display.flip()
        time += clock.tick(55)/1000
    if life > 0:
        game(life-1, time)
''' End of Game section '''
def instructions_page():
    class Settings():
        def __init__(self):
            self.text = ['Use/the/arrow/keys/to/turn/to/the/left/or/right','Use/the/ESC/key/to/quit','Good/Luck!']
            self.SCREEN_WIDTH = 1024
            self.SCREEN_HEIGHT = 720
            self.text_colour = (255,255,0)
            self.black = (0,0,0)
            self.smallfontsize = 30
            self.smallfont = pygame.font.Font(resource_path('images/arcadeclassic.ttf'),self.smallfontsize)
            self.bigfont = pygame.font.Font(resource_path('images/arcadeclassic.ttf'),60)

    settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT), pygame.FULLSCREEN) 
    pygame.display.set_icon(pygame.image.load(resource_path('images/ship.png')))
    pygame.display.set_caption("Space Game")
    pygame.display.get_active()
    screen.fill((0,0,0))
    text = settings.bigfont.render('Instructions', True, settings.text_colour)
    text_rect = text.get_rect(center=(settings.SCREEN_WIDTH/2,settings.SCREEN_HEIGHT/2))
    screen.blit(text, text_rect)
    for i, l in enumerate(settings.text):
        l = l.replace('/', '  ')
        text = settings.smallfont.render(l, True, settings.text_colour)
        text_rect = text.get_rect(center=(settings.SCREEN_WIDTH/2,settings.SCREEN_HEIGHT/2 + settings.smallfontsize*(i+1)+15))
        screen.blit(text, text_rect)
    running = True
    exit = False
    while running:
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: 
                running = False
            if ev.type == KEYDOWN and ev.key == K_ESCAPE:
                running = False
            #if ev.type == pygame.MOUSEBUTTONDOWN: 
            #    if play_text_rect.collidepoint(mouse):
        mouse = pygame.mouse.get_pos()
        
        pygame.display.flip()
    menu()

def menu():
    pygame.init() 

    res = (720,720)
    screen = pygame.display.set_mode(res, pygame.FULLSCREEN) 
    pygame.display.set_icon(pygame.image.load(resource_path('images/ship.png')))
    pygame.display.set_caption("Space Game")
    pygame.display.get_active()  
    #hover_colour = (170, 170, 0)
    text_colour = (255,255,0)
    black = (0,0,0)
  
    width = screen.get_width() 
    height = screen.get_height() 
  
    smallfont = pygame.font.Font(resource_path('images/arcadeclassic.ttf'),60)
    bigfont = pygame.font.Font(resource_path('images/arcadeclassic.ttf'),90)

    title_text = bigfont.render('Main Menu' , True , text_colour) 
    title_text_rect = title_text.get_rect(center=(width/2, (height/2)-105))
    play_text = smallfont.render('Play!' , True , text_colour) 
    play_text_rect = play_text.get_rect(center=(width/2, (height/2)-30))
    instructions_text = smallfont.render('Instructions' , True , text_colour) 
    instructions_text_rect = play_text.get_rect(center=(width/2, (height/2)+30))
    quit_text = smallfont.render('Quit' , True , text_colour)
    quit_text_rect = play_text.get_rect(center=(width/2, (height/2)+90))
    running = True
    play = False
    instructions = False
    while running: 
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: 
                running = False
            if ev.type == KEYDOWN and ev.key == K_ESCAPE:
                running = False
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if play_text_rect.collidepoint(mouse):
                    running = False
                    play = True
                elif quit_text_rect.collidepoint(mouse):
                    running = False
                elif instructions_text_rect.collidepoint(mouse):
                    running = False
                    instructions = True

        screen.fill((0,0,0)) 
        mouse = pygame.mouse.get_pos() 

        if play_text_rect.collidepoint(mouse): 
            play_text = smallfont.render('Play!' , True , black, text_colour)
        else:
            play_text = smallfont.render('Play!' , True , text_colour) 
        
    
        if quit_text_rect.collidepoint(mouse): 
            quit_text = smallfont.render('Quit' , True , black, text_colour)
        else:
            quit_text = smallfont.render('Quit' , True , text_colour)
        if instructions_text_rect.collidepoint(mouse): 
            instructions_text = smallfont.render('Instructions' , True , black, text_colour)
        else:
            instructions_text = smallfont.render('Instructions' , True , text_colour) 
        
        screen.blit(play_text ,play_text_rect)    
        screen.blit(instructions_text, instructions_text_rect) 
        screen.blit(quit_text ,quit_text_rect) 
        screen.blit(title_text ,title_text_rect) 

        pygame.display.flip()
    if play:
        game()
    if instructions:
        instructions_page()
menu()