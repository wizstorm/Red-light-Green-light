"""
Red_lightGreen_light2

Description:
"""
m=""
import pygame
import random
pygame.init()

#window
w=pygame.display.set_mode([400,400])
m=""


print("Welcome to redlight green light")
m=input("(s)singleplayer or (m)mulitiplayer: ")
if m=="s":
    print("Press space to move.")
    
    #vairable
    light=1
    yards=400
    lightc=100
    #loop
    while yards>=0:
        light=random.randint(1,2)
        lightc=random.randint(100,500)
        while lightc>0:
            if light==1:
                w.fill((0, 255, 0))
            else:
                w.fill((255, 129, 94))
            
            pygame.draw.circle(w,(198, 134, 66),(200,yards),20)
            pygame.draw.circle(w,(255,255,255),(195,yards-12),4)
            pygame.draw.circle(w,(255,255,255),(205,yards-12),4)
            pygame.draw.circle(w,(0,0,0),(195,yards-14),1)
            pygame.draw.circle(w,(0,0,0),(205,yards-14),1)
            rect = pygame.Rect(182,yards-8, 36,27 )
            pygame.draw.ellipse(w, (0,0,0), rect)    
                
            if light==1:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    yards-=1
                    
            if light==2:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    break
            pygame.event.pump()
            pygame.display.flip()
            pygame.time.wait(10)
            lightc-=1
        if light==2:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                w.fill((255, 129, 94))
                break
    if yards<=0:
        print("You beat the game")
if m=="m":
    print("Player Red: press w to move ")
    print("Player Blue: press o to move ")
    
    
    #vairable
    light=1
    yards1=400
    yards2=400
    lightc=100
    d1=False
    d2=False
    #loop
    while yards1>0 and yards2>0:
        light=random.randint(1,2)
        lightc=random.randint(100,500)
        while lightc>0:
            if light==1:
                w.fill((0, 255, 0))
            else:
                w.fill((255, 129, 94))
            #player1
            if not d1:    
                pygame.draw.circle(w,(255,0,0),(100,yards1),20)
            
                pygame.draw.circle(w,(255,255,255),(95,yards1-12),4)
                pygame.draw.circle(w,(255,255,255),(105,yards1-12),4)
                pygame.draw.circle(w,(0,0,0),(95,yards1-14),1)
                pygame.draw.circle(w,(0,0,0),(105,yards1-14),1)
                rect = pygame.Rect(82,yards1-8, 36,27 )
                pygame.draw.ellipse(w, (0,0,0), rect)
            
                
            if not d1:
                if light==1:
                    if pygame.key.get_pressed()[pygame.K_w]:
                        yards1-=1
                if light==2:
                    if pygame.key.get_pressed()[pygame.K_w]:
                        d1=not d1
            #player2
            if not d2:    
                pygame.draw.circle(w,(0,0,255),(300,yards2),20)
            
                pygame.draw.circle(w,(255,255,255),(295,yards2-12),4)
                pygame.draw.circle(w,(255,255,255),(305,yards2-12),4)
                pygame.draw.circle(w,(0,0,0),(295,yards2-14),1)
                pygame.draw.circle(w,(0,0,0),(305,yards2-14),1)
                rect = pygame.Rect(282,yards2-8, 36,27 )
                pygame.draw.ellipse(w, (0,0,0), rect)

                

            if not d2:
                if light==1:
                    if pygame.key.get_pressed()[pygame.K_o]:
                        yards2-=1
                if light==2:
                    if pygame.key.get_pressed()[pygame.K_o]:
                        d2=not d2
            
            
            pygame.event.pump()
            pygame.display.flip()
            pygame.time.wait(10)
            lightc-=1
        if d1 and d2:
            break
    if yards1<=0:
        print("Red won the game")
    if yards2<=0:
        print("Blue won the game")
    if yards1<yards2:
        print("Red got farther on the game")
    if yards1>yards2:
        print("Blue got farther on the game") 
    if yards1==yards2:
        print("You both got eliminated at the same spot")


