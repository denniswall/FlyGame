""" flyGame.py
    game complete

    build intro screen
    add state management
"""
    
import pygame, random, gameEngine
pygame.init()

screen = pygame.display.set_mode((640, 700))

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ship.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        
        
        
        if not pygame.mixer:
            print ("problem with sound")
        else:
            pygame.mixer.init()
            self.sndYays = pygame.mixer.Sound("yays.ogg")
            self.sndThunders = pygame.mixer.Sound("thunders.ogg")
            self.sndEngines = pygame.mixer.Sound("music.ogg")
            
            self.sndEngines.play()
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, mousey)
EAST=0
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("schiff 10000.bmp")
        self.image=self.image.convert()
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        self.rect=self.image.get_rect()
        self.rect.center=(320,280)
        self.img=[]
        self.loadImages()
        EAST=0
        self.frame=0
        self.delay=3
        self.pause=0
        self.dx=5
    def update(self):
        self.pause -=1
        if self.pause < 0:
            self.pause=self.delay
            self.frame +=1
            if self.frame > 15:
                self.frame=0
            self.image=self.img[self.frame]
    def loadImages(self):
        for i in range(10):
            imgName="schiff 1000%d.bmp" %i
            tmpImg=pygame.image.load(imgName)
            tmpImg.convert()
            transColor=tmpImg.get_at((1,1))
            tmpImg.set_colorkey(transColor)
            self.img.append(tmpImg)
        for i in range(6):
            imgName2="schiff 1001%d.bmp" %i
            tmpImg2=pygame.image.load(imgName2)
            tmpImg2.convert()
            transColor=tmpImg2.get_at((1,1))
            tmpImg2.set_colorkey(transColor)
            self.img.append(tmpImg2)

class Small(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("smallship.gif")
        self.image=self.image.convert()
        self.rect=self.image.get_rect()
        self.dy=-8
        self.reset()
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery -= self.dy
        if self.rect.top < 0:
            self.reset()
    def reset(self):
        self.rect.bottom=screen.get_height()
        self.rect.centerx=random.randrange(0,screen.get_width())
        self.dy=random.randrange(5,10)
        self.dx=random.randrange(-2,6)

class Building(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("TSbuildings.BMP")
        self.image=self.image.convert()
        self.rect=self.image.get_rect()
        self.image=pygame.transform.scale(self.image,(680,750))

class Place(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("place.gif")
        self.image=self.image.convert()
        self.rect=self.image.get_rect()
        self.image=pygame.transform.scale(self.image,(640,700))
        
        

class Ships(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("ship.gif")
        self.image=self.image.convert()
        self.rect=self.image.get_rect()
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        if not pygame.mixer:
            print ("problem with the sound!")
        else:
            pygame.mixer.init()
            self.sndYays=pygame.mixer.Sound("yays.ogg")
            self.sndThunders=pygame.mixer.Sound("thunderss.ogg")
            self.sndEngines=pygame.mixer.Sound("music.ogg")
            self.sndEngines.play()
    def update(self):
        mousex,mousey=pygame.mouse.get_pos()
        self.rect.center=(mousex,520)




class Scoreboard2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives=5
        self.score=0
        self.font=pygame.font.Font("freesansbold.ttf",30)
    def update(self):
        self.text="planes: %d score: %d second level" %(self.lives,self.score)
        self.image=self.font.render(self.text,1,(0,255,0))
        self.rect=self.image.get_rect()
WEST=4
class Chopper(pygame.sprite.Sprite):
    def __init__(self,screen):
        self.screen=screen
        pygame.sprite.Sprite.__init__(self)
        self.STANDING=0
        self.ANIMATION=1
        self.loadImages()
        self.image=self.imageStand
        self.rect=self.image.get_rect()
        self.rect.center=(320,220)
        self.frame=0
        self.delay=3
        self.pause=0
        self.dir=WEST
        self.lives=6
        self.state=self.STANDING
    def update(self):
        if self.state == self.STANDING:
            self.image=self.imageStand
        else:
            self.pause += 1
            if self.pause >= self.delay:
                self.pause=0
                self.frame += 1
                if self.frame > 4:
                    self.frame=0
                    self.state=self.STANDING
                    self.image=self.imageStand
                else:
                    self.image=self.chopperImages[self.frame]
        
    def loadImages(self):
        self.imageStand=pygame.image.load("heli0000.gif")
        self.imageStand=self.imageStand.convert()
        transColor=self.imageStand.get_at((1,1))
        self.imageStand.set_colorkey(transColor)
        self.chopperImages=[]
        for i in range(5):
            imgName="heli000%d.gif" % i
            tmpImage=pygame.image.load(imgName)
            tmpImage=tmpImage.convert()
            transColor=tmpImage.get_at((1,1))
            tmpImage.set_colorkey(transColor)
            self.chopperImages.append(tmpImage)

class Bang(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.STANDING=0
        self.ANIMATION=1
        self.loadImages()
        self.image=self.imageStand
        self.rect=self.image.get_rect()
        self.rect.center=(320,220)
        self.frame=0
        self.delay=3
        self.pause=0
        self.state=self.STANDING
        self.reset()
    def update(self):
        if self.state == self.STANDING:
            self.image=self.imageStand
        else:
            self.pause += 1
            if self.pause > self.delay:
                self.pause=0
                self.frame += 1
                if self.frame >= 3:
                    self.rect.center=(-100,-100)
                    self.frame=0
                    self.state=self.STANDING
                    self.image=self.imageStand
                else:
                    self.image=self.bangImages[self.frame]
    def loadImages(self):
        self.imageStand=pygame.image.load("myFont0000.gif")
        self.imageStand=self.imageStand.convert()
        transColor=self.imageStand.get_at((1,1))
        self.imageStand.set_colorkey(transColor)
        self.bangImages=[]
        for i in range(4):
            imgName="myFont000%d.gif" % i
            tmpImage=pygame.image.load(imgName)
            tmpImage=tmpImage.convert()
            transColor=tmpImage.get_at((1,1))
            tmpImage.set_colorkey(transColor)
            self.bangImages.append(tmpImage)
    def reset(self):
        self.rect.center=(-100,-100)
    def appear(self):
        self.rect.center=(320,220)

class Blast(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("blast.gif")
        self.image=self.image.convert()
        self.rect=self.image.get_rect()
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        self.rect.centerx=320
        self.rect.centery=220
        self.dx=0
        self.dy=10
    def update(self):
        self.rect.centery += self.dy
        if self.rect.centery > screen.get_height():
            self.reset()
            
            
            
    def reset(self):
        self.rect.centerx=320
        self.rect.centery=220
    def appear(self):
        self.rect.centerx=300
        self.rect.centery=240
                
        
            
        
        
class Scoreboard3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives=3
        self.score=0
        self.font=pygame.font.Font("freesansbold.ttf",30)
    def update(self):
        self.text="lives: %d score: %d Avoid the bullets! " %(self.lives,self.score)
        self.image=self.font.render(self.text,1,(255,0,0))
        self.rect=self.image.get_rect()

class Scoreboard4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives=4
        self.score=0
        self.time=600
        self.font=pygame.font.Font("freesansbold.ttf",30)
    def update(self):
        self.text="lives:%d score:%d time:%d goal:1000 points" %(self.lives,self.score,self.time)
        self.image=self.font.render(self.text,1,(255,0,0))
        self.rect=self.image.get_rect()
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self,screen):
        self.screen=screen
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("bullet.gif")
        self.image=self.image.convert()
        self.rect=self.image.get_rect()
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        self.rect.centerx=100
        self.rect.centery=200
        self.dx=7
        self.dy=6
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.centerx > self.screen.get_width():
            self.dx *= -1
        if self.rect.centerx < 0:
            self.dx *= -1
        if self.rect.centery > self.screen.get_height():
            self.dy *= -1
        if self.rect.centery < 0:
            self.dy *= -1
    def reset(self):
        self.rect.centerx=400
        self.rect.centery=500
    def reset2(self):
        self.rect.centerx=200
        self.rect.centery=400

class Bullets(pygame.sprite.Sprite):
    def __init__(self,screen):
        self.screen=screen
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("bullets.gif")
        self.image=self.image.convert()
        self.rect=self.image.get_rect()
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        self.rect.centerx=320
        self.rect.centery=260
        self.dx=-9
        self.dy=9
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.centerx < 0:
            self.reset()
        if self.rect.centerx >self.screen.get_width():
            self.reset()
        if self.rect.centerx > self.screen.get_height():
            self.reset()
    def reset(self):
        self.rect.centerx=320
        self.rect.centery=260
    def reset2(self):
        self.rect.centerx=320
        self.rect.centery=250

class Bulletss(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.image=pygame.image.load("bulletss.gif")
        self.image=self.image.convert()
        self.rect=self.image.get_rect()
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        self.rect.centerx=340
        self.rect.centery=250
        self.dy=-8
        self.dx=7
    def update(self):
        self.rect.centery += self.dy
        self.rect.centerx += self.dx
        if self.rect.centery < 0:
            self.reset()
        if self.rect.centerx < 0:
            self.reset()
    def reset(self):
        self.rect.centerx=340
        self.rect.centery=250
    def reset2(self):
        self.rect.centerx=250
        self.rect.centery=220
        
        

            

class Label(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font=pygame.font.Font("freesansbold.ttf",20)
        self.text=""
        self.center=(320,240)
    def update(self):
        self.image=self.font.render(self.text,1,(255,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=self.center

class Beachs(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("beachs.gif")
        self.image=self.image.convert()
        self.rect=self.image.get_rect()
        self.image=pygame.transform.scale(self.image,(640,700))
        
        

class Boat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("boat.gif")
        self.image=self.image.convert()
        self.rect=self.image.get_rect()
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        self.reset()
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()
    def reset(self):
        self.rect.bottom=0
        self.rect.centerx=random.randrange(0,screen.get_width())
        self.dy=random.randrange(5,10)
        self.dx=random.randrange(-2,2)

EAST=0

class Missile(pygame.sprite.Sprite):
    def __init__(self,screen):
        self.screen=screen
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("missile 0000.gif")
        self.image=self.image.convert()
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        self.rect=self.image.get_rect()
        self.rect.center=(0,300)
        self.img=[]
        self.loadPics()
        self.dir=EAST
        self.frame=0
        self.delay=3
        self.pause=self.delay
        self.dx=9
    def reset(self):
        self.rect.center=(0,300)
    def reset2(self):
        self.rect.center=(0,500)
    def reset3(self):
        self.rect.center=(0,100)
    def reset4(self):
        self.rect.center=(0,600)
        
    def update(self):
        self.pause -=9
        if self.pause < 0:
            self.pause=self.delay
            self.frame +=1
            if self.frame >= 4:
                self.frame=4
            self.image=self.img[self.frame]
            self.rect.centerx +=self.dx
            if self.rect.centerx > self.screen.get_width():
                self.rect.centerx=0
                self.frame=0
    def loadPics(self):
        for i in range(5):
            imgName="missile 000%d.gif" %i
            tmpImg=pygame.image.load(imgName)
            tmpImg.convert()
            transColor=tmpImg.get_at((1,1))
            tmpImg.set_colorkey(transColor)
            self.img.append(tmpImg)
            
   

        
        
class Base(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("base.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dy = 17
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
    
    def update(self):
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()
            
    def reset(self):
        self.rect.top = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
      
class Jet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("jet.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()
        if self.rect.right > screen.get_width():
            self.dx *= -1
        if self.rect.left < 0:
            self.dx *= -1
    
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.dy = random.randrange(8, 10)
        self.dx = random.randrange(-6, 7)
    
class Stages(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("stages.gif")
        self.image=self.image.convert()
        self.rect = self.image.get_rect()
        self.dy = 3
        self.reset()
        
        
    def update(self):
        self.rect.bottom += self.dy
        if self.rect.top >= 0:
            self.reset() 
    
    def reset(self):
        self.rect.bottom = screen.get_height()

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 4
        self.score = 0
        self.font = pygame.font.Font("freesansbold.ttf", 50)
        
    def update(self):
        self.text = "planes: %d, score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()

class Fuel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image=pygame.image.load("fuel.gif")
        self.rect=self.image.get_rect()
        self.reset()
        self.dy=16
        transColor=self.image.get_at((1,1))
        self.image.set_colorkey(transColor)
        
    def update(self):
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()
        
    def reset(self):
        self.rect.top=0
        self.rect.centerx=random.randrange(0,screen.get_width())
    def hide(self):
        self.rect.center=(-100,-100)
    
        
            

            
        
     
        
        
        
    
    


    
def games():
    pygame.display.set_caption("Mail Pilot Game. Let's Go!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    stages=Stages()
    fuel=Fuel()
    ship = Ship()
    base = Base()
    
    jet1 = Jet()
    jet2 = Jet()
    jet3 = Jet()
    jet4= Jet()
    jet5= Jet()
    jet6= Jet()
    jet7= Jet()
    
    scoreboard = Scoreboard()

    friendSprites = pygame.sprite.Group(stages,base,fuel, ship)
    jetSprites = pygame.sprite.Group(jet1, jet2, jet3,jet4,jet5,jet6,jet7)
    scoreSprite = pygame.sprite.Group(scoreboard)

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        
        if ship.rect.colliderect(fuel.rect):
            ship.sndYays.play()
            fuel.reset()
            scoreboard.lives += 1
        if scoreboard.score == 1100:
            keepGoing=False
            scoreboard.score=0
            scoreboard.lives=0
            level()
            ship.sndEngines.stop()
        
            
            
        
        
            
                
        #check collisions
        
        if ship.rect.colliderect(base.rect):
            ship.sndYays.play()
            base.reset()
            scoreboard.score += 100
        if scoreboard.lives == 8:
            fuel.hide()
        
            

        hitJets = pygame.sprite.spritecollide(ship, jetSprites, False)
        if hitJets:
            ship.sndThunders.play()
            scoreboard.lives -= 4
            scoreboard.score -= 200
            if scoreboard.lives <= 0:
                keepGoing = False
                ship.sndEngines.stop()
            for theJet in hitJets:
                theJet.reset()
        
        friendSprites.update()
        jetSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        jetSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    
    
    #show mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score

def level():
    pygame.display.set_caption("second level pilot!")
    background=pygame.Surface(screen.get_size())
    background.fill((0,0,255))
    screen.blit(background,(0,0))
    ship=Ship()
    base=Base()
    beachs=Beachs()
    missile=Missile(screen)
    missile2=Missile(screen)
    missile3=Missile(screen)
    missile4=Missile(screen)
    missile2.rect.center=(250,500)
    missile3.rect.center=(0,100)
    missile4.rect.center=(350,600)
    
    boat=Boat()
    boat2=Boat()
    boat3=Boat()
    boat4=Boat()
    scoreboard2=Scoreboard2()
    friendSprites=pygame.sprite.Group(beachs,base,ship)
    enemySprites=pygame.sprite.Group(boat,boat2,boat3,boat4,missile,missile2,missile3,missile4)
    scoreSprites=pygame.sprite.Group(scoreboard2)
    clock=pygame.time.Clock()
    keepGoing=True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing=False
            
        pygame.mouse.set_visible(False)
        if ship.rect.colliderect(base.rect):
            scoreboard2.score += 200
            base.reset()
            ship.sndYays.play()
        
        if ship.rect.colliderect(boat.rect):
            boat.reset()
            scoreboard2.lives -= 1
            ship.sndThunders.play()
            scoreboard2.score -=200
        if ship.rect.colliderect(boat2.rect):
            boat2.reset()
            scoreboard2.lives -= 1
            ship.sndThunders.play()
            scoreboard2.score -=200
        if ship.rect.colliderect(boat3.rect):
            boat3.reset()
            scoreboard2.lives -= 1
            ship.sndThunders.play()
            scoreboard2.score -=200
        if ship.rect.colliderect(boat4.rect):
            boat4.reset()
            scoreboard2.lives -=1
            ship.sndThunders.play()
            scoreboard2.score -=200
        if scoreboard2.score == 2000:
            keepGoing=False
            scoreboard2.score=0
            scoreboard2.lives=0
            final()
            ship.sndEngines.stop()
        if ship.rect.colliderect(missile.rect):
            ship.sndThunders.play()
            missile.reset()
            scoreboard2.lives -=1
            
        if ship.rect.colliderect(missile2.rect):
            ship.sndThunders.play()
            missile2.reset2()
            scoreboard2.lives -=1
        if ship.rect.colliderect(missile3.rect):
            ship.sndThunders.play()
            missile3.reset3()
            scoreboard2.lives -=1
        if ship.rect.colliderect(missile4.rect):
            ship.sndThunders.play()
            missile4.reset4()
            scoreboard2.lives -=1
        if scoreboard2.lives == 0:
            keepGoing=False
            ship.sndEngines.stop()
        if scoreboard2.score == 0:
            ship.sndEngines.stop()
            
        
        
        
    
        friendSprites.update()
        enemySprites.update()
        scoreSprites.update()
        friendSprites.draw(screen)
        enemySprites.draw(screen)
        scoreSprites.draw(screen)
        pygame.display.flip()
    return scoreboard2.score


def final():
    pygame.display.set_caption("avoid the bullets and let them hit the red chopper instead!")
    background=pygame.Surface(screen.get_size())
    background.fill((0,0,255))
    screen.blit(background,(0,0))
    ships=Ships()
    bang=Bang()
    bullets=Bullets(screen)
    bullets2=Bullets(screen)
    bullets.dx=9
    bullets.rect.centerx=320
    bullets.rect.centery=250
    bulletss=Bulletss(screen)
    bulletss2=Bulletss(screen)
    bulletss2.dx=-9
    bulletss2.rect.centerx=250
    bulletss2.rect.centery=220
    blast=Blast()
    blast2=Blast()
    blast2.rect.centerx=300
    blast2.rect.centery=240
    bullet=Bullet(screen)
    bullet2=Bullet(screen)
    bullet2.rect.centerx=200
    bullet2.rect.centery=350
    chopper=Chopper(screen)
    place=Place()
    scoreboard3=Scoreboard3()
    friendSprites=pygame.sprite.Group(place,ships)
    enemySprites=pygame.sprite.Group(chopper,bullet,bullet2,bang,blast,blast2)
    bulletsSprites=pygame.sprite.Group(bullets,bullets2,bulletss,bulletss2)
    #placeSprites=pygame.sprite.Group(place)
    scoreSprites=pygame.sprite.Group(scoreboard3)
    clock=pygame.time.Clock()
    keepGoing=True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing=False
        pygame.mouse.set_visible(False)
        chopper.state=chopper.ANIMATION
        if bullet.rect.colliderect(ships.rect):
            scoreboard3.lives -= 1
            bullet.reset()
            ships.sndThunders.play()
        if bullet2.rect.colliderect(ships.rect):
            scoreboard3.lives -= 1
            bullet2.reset2()
            ships.sndThunders.play()
        if ships.rect.colliderect(chopper.rect):
            scoreboard3.lives -= 3
            ships.sndThunders.play()
        if bullet.rect.colliderect(chopper.rect):
            chopper.lives -= 1
            bullet.reset()
            bang.state=bang.ANIMATION
            bang.appear()
            ships.sndYays.play()
        if bullet2.rect.colliderect(chopper.rect):
            chopper.lives -= 1
            bullet2.reset2()
            bang.state=bang.ANIMATION
            bang.appear()
            ships.sndYays.play()
        if bullets.rect.colliderect(ships.rect):
            scoreboard3.lives -= 1
            bullets.reset()
            ships.sndThunders.play()
        if bullets2.rect.colliderect(ships.rect):
            scoreboard3.lives -= 1
            bullets2.reset2()
            ships.sndThunders.play()
        if bulletss.rect.colliderect(ships.rect):
            scoreboard3.lives -= 1
            bulletss.reset()
            ships.sndThunders.play()
        if bulletss2.rect.colliderect(ships.rect):
            scoreboard3.lives -= 1
            bulletss2.reset2()
            ship.sndThunders.play()
        if blast.rect.colliderect(ships.rect):
            scoreboard3.lives -= 1
            blast.reset()
            ships.sndThunders.play()
        if blast2.rect.colliderect(ships.rect):
            blast2.appear()
            scoreboard3.lives -= 1
            ships.sndThunders.play()
        if chopper.lives == 0:
            keepGoing=False
            scoreboard3.score=0
            scoreboard3.lives=0
            final2()
            ships.sndEngines.stop()
        if scoreboard3.lives < 0:
            keepGoing=False
            ships.sndEngines.stop()
        if scoreboard3.score == 0:
            ships.sndEngines.stop()
        friendSprites.update()
        enemySprites.update()
        bulletsSprites.update()
        #placeSprites.update()
        scoreSprites.update()
        friendSprites.draw(screen)
        enemySprites.draw(screen)
        bulletsSprites.draw(screen)
        #placeSprites.draw(screen)
        scoreSprites.draw(screen)
        pygame.display.flip()
    return scoreboard3.score

def final2():
    pygame.display.set_caption("acquire 1000 points before time runs out!")
    background=pygame.Surface(screen.get_size())
    background.fill((255,255,255))
    screen.blit(background,(0,0))
    ship=Ship()
    fuel=Fuel()
    jet1=Jet()
    jet2=Jet()
    jet3=Jet()
    jet4=Jet()
    base=Base()
    small1=Small()
    small2=Small()
    small3=Small()
    building=Building()
    scoreboard4=Scoreboard4()
    friendSprites=pygame.sprite.Group(building,ship,base,fuel)
    enemySprites=pygame.sprite.Group(jet1,jet2,jet3,jet4,small1,small2,small3)
    scoreSprites=pygame.sprite.Group(scoreboard4)
    clock=pygame.time.Clock()
    keepGoing=True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing=False
        pygame.mouse.set_visible(False)
        if small1.rect.colliderect(ship.rect):
            scoreboard4.lives -= 1
            small1.reset()
            ship.sndThunders.play()
            scoreboard4.score -=100

        if small2.rect.colliderect(ship.rect):
            scoreboard4.lives -=1
            small2.reset()
            ship.sndThunders.play()
            scoreboard4.score -=100
        if fuel.rect.colliderect(ship.rect):
            fuel.reset()
            scoreboard4.lives +=1
            scoreboard4.time += 100
            ship.sndYays.play()
        if scoreboard4.lives == 4:
            fuel.hide()
        if scoreboard4.lives == 5:
            fuel.hide()

        if small3.rect.colliderect(ship.rect):
            small3.reset()
            scoreboard4.lives -=1
            ship.sndThunders.play()
            scoreboard4.score -=100

        if jet1.rect.colliderect(ship.rect):
            jet1.reset()
            scoreboard4.lives -=1
            ship.sndThunders.play()
            scoreboard4.score -=100

        if jet2.rect.colliderect(ship.rect):
            jet2.reset()
            scoreboard4.lives -=1
            ship.sndThunders.play()
            scoreboard4.score -=100

        if jet3.rect.colliderect(ship.rect):
            ship.sndThunders.play()
            jet3.reset()
            scoreboard4.score -=100
            scoreboard4.lives -=1
        if jet4.rect.colliderect(ship.rect):
            ship.sndThunders.play()
            jet4.reset()
            scoreboard4.score -=100
            scoreboard4.lives -=1
        if base.rect.colliderect(ship.rect):
            scoreboard4.score +=100
            base.reset()
            ship.sndYays.play()

        if scoreboard4.score == 0:
            ship.sndEngines.stop()
        if scoreboard4.score == 1000:
            keepGoing=False
            ship.sndEngines.stop()
            credit()
        if scoreboard4.lives < 0:
            keepGoing=False
            ship.sndEngines.stop()
        scoreboard4.time -=1
        if scoreboard4.time < 0:
            keepGoing=False
            ship.sndEngines.stop()

        friendSprites.update()
        enemySprites.update()
        scoreSprites.update()
        friendSprites.draw(screen)
        enemySprites.draw(screen)
        scoreSprites.draw(screen)
        pygame.display.flip()
                           
    
def instructions():
    
    stages=Stages()
    
    
    
    
    
    
    allSprites = pygame.sprite.Group(stages)
    insFont = pygame.font.Font("acmesa.TTF", 20)

    instructions = (
    "Ultimate Ship game! Music: Ninja Tuna!",
    "Instructions:  You are an army pilot,",
    "delivering food to the bases.",
    "Fly over bases to drop the food,",
    "but be careful not to fly too close",    
    "to the jets. Your ship will fall ",
    "apart if it is hit by jets too",
    "many times.",
    "You retrieve life or time by powerups.",
    "",
    "Good Luck!",
    "",
    "Click to start,Escape twice to quit"
    )

    insLabels = []    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
        
                    
        
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (30, 30*i))

        pygame.display.flip()
        
    
    pygame.mouse.set_visible(True)
    return donePlaying



def credit():
    pygame.display.set_caption("credits!")
    background=pygame.Surface(screen.get_size())
    background.fill((0,0,255))
    screen.blit(background,(0,0))
    spaceship=Spaceship()
    spaceship2=Spaceship()
    spaceship2.rect.center=(100,280)
    label=Label()
    label2=Label()
    allSprites=pygame.sprite.Group(label,label2,spaceship,spaceship2)
    label.text="Mission Complete!"
    label2.center=(400,400)
    label2.text="Click on the x at the top to exit!"
    clock=pygame.time.Clock()
    keepGoing=True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing=False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing=False
        allSprites.clear(screen,background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()
        
def main():
    donePlaying = False
    while not donePlaying:
        donePlaying = instructions()
        if not donePlaying:
            games()

class Game(gameEngine.Scene):
    def __init__(self):
        gameEngine.Scene.__init__(self)
        self.background.fill((0,0,255))
        big=gameEngine.SuperSprite(self)
        big.setImage("big.gif")
        big.x=320
        big.y=280
        self.addLabels()
        self.addButton()
        self.sprites=[self.lblTitle,self.label,
                      self.button,big]
    def addLabels(self):
        self.lblTitle=gameEngine.Label()
        self.lblTitle.text="plane demo"
        self.lblTitle.center=((-200,-200))
        self.lblTitle.size=((100,100))
        self.label=gameEngine.Label()
        self.label.font=pygame.font.Font("acmesa.TTF",20)
        self.label.text="Plane Game"
        self.fgColor=(0,0,255)
        self.bgColor=(0,255,0)
        self.label.center=((200,100))
        self.label.size=((200,100))
    def addButton(self):
        self.button=gameEngine.Button()
        self.button.text="Start game"
        self.button.center=((450,180))
    def update(self):
        if self.button.clicked:
            self.stop()
            main()
            
        
        
            
        
            
        
                
            
            

game=Game()
game.start()
        
    



if __name__ == "__main__":
    main()
    
    
