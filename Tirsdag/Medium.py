import random as rn
from time import sleep
import pygame as pg

## Oppgave 1##

def shape():
  a = rn.randint(0,250)
  aa = rn.randint(10,250)
  b = rn.randint(0,250)
  bb = rn.randint(10,250)
  c = rn.randint(0,250)
  cc = rn.randint(10,250)
  d = rn.randint(0,250)
  dd = rn.randint(10,250)
  e = rn.randint(0,250)
  ee = rn.randint(10,250)
  f = rn.randint(0,250)
  ff = rn.randint(10,250)


  lineAmount = rn.randint(3,6)

  gamer = pg.display.set_mode((250,250))

  pg.draw.line(gamer, start_pos=(a,aa), end_pos=(b,bb), color="red")
  pg.draw.line(gamer, start_pos=(b,bb), end_pos=(c,cc), color="red")

  while True:
    if lineAmount == 3:
      pg.draw.line(gamer, start_pos=(c,cc), end_pos=(a,aa), color="red")
      break
    else:
      pg.draw.line(gamer, start_pos=(c,cc), end_pos=(d,dd), color="red")
    if lineAmount == 4:
      pg.draw.line(gamer, start_pos=(d,dd), end_pos=(a,aa), color="red")
      break
    else:
      pg.draw.line(gamer, start_pos=(d,dd), end_pos=(e,ee), color="red")
    if lineAmount == 5:
      pg.draw.line(gamer, start_pos=(e,ee), end_pos=(a,aa), color="red")
      break
    else:
      pg.draw.line(gamer, start_pos=(e,ee), end_pos=(f,ff), color="red")
      pg.draw.line(gamer, start_pos=(f,ff), end_pos=(a,aa), color="red")
    break

  pg.init()
  pg.display.flip()

shape()

running = True
while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
    if event.type == pg.KEYDOWN:
      shape()

