#!/usr/bin/python

import sys,pygame,pygame.mixer
from pygame.locals import *
pygame.init()
size = width,height = 800,500
screen = pygame.display.set_mode(size)
sound = pygame.mixer.Sound('song.mp3')
clock = pygame.time.Clock()
x=10
y=10
r=0
g=0
b=0
x1=0
y1=0
mx,my=pygame.mouse.get_pos()
direction = "right"
screen.fill((0,0,255))
rocket = pygame.image.load("rocket.png").convert_alpha()
#rock = rocket1

#rocket1 = pygame.transform.flip(rocket1,1,0)
bg = pygame.image.load("sprite.png").convert_alpha()
bullet = pygame.image.load("bullet.png").convert_alpha()
#bg = pygame.transform.scale(bg,size)
bg1 = bg
bgx = 0 
bgx1 = +1600

by=0
while 1:

  rocket_rect = rocket.get_rect()
  
  print rocket_rect.x, rocket_rect.y, 
  print rocket_rect.centerx, rocket_rect.centery, 
  print rocket_rect.center
  print rocket_rect.left, rocket_rect.right
  print rocket_rect.top, rocket_rect.bottom
  print rocket_rect.topleft, rocket_rect.bottomright
  print rocket_rect.width, rocket_rect.height




  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == KEYDOWN and event.key == K_q:
      sys.exit() 
  screen.fill((0,0,0)) 
  jx,jy = pygame.mouse.get_pos()
  screen.blit(bg,(bgx,0))
  screen.blit(bg1,(bgx1,0))
  bgx = bgx - 5
  bgx1 = bgx1 - 5  
  if bgx1 == 0 :
    bgx = +1600 
    #bgx = 0
  if bgx == 0 :
    bgx1 = +1600
  screen.blit(rocket,(mx,my))  
  #print pygame.PixelArray(rocket)
 # screen.blit(rocket,(jx,jy))  
  screen.blit(bullet,(jx,jy))  
  pygame.display.update()
  clock.tick(120)
  
  if event.type == KEYDOWN and event.key == K_SPACE:
    while jx < 800:
      jx=jx+1 
      screen.blit(bullet,(jx,0))  
  if event.type == MOUSEBUTTONDOWN:
    mx,my=pygame.mouse.get_pos() 
  if event.type == KEYDOWN and event.key == K_RIGHT:
    mx=mx+6
  if event.type == KEYDOWN and event.key == K_LEFT:
    mx=mx-6
  if event.type == KEYDOWN and event.key == K_DOWN:
    my=my+6
  if event.type == KEYDOWN and event.key == K_UP:
    my=my-6
  """if r == 255:
    a = -1
  elif r == 0:
    a = 1
  r=r+a
  #b=b+a"""
     
