import turtle
import random
import time
import os

print ('Read the intructions :D')

scr = turtle.Screen()
scr.setup(500,400)

fire = turtle.Turtle()
water = turtle.Turtle()
fb = turtle.Turtle()
wb = turtle.Turtle()


scr.bgcolor('dark slate blue')
scr.addshape('Water (1).png')
scr.addshape('Water Punch (1).png')
scr.addshape('Water Projectile (1).png')
scr.addshape('Tsunami (1).png')
scr.addshape('Fire (1).png')
scr.addshape('Fire Punch (1).png')
scr.addshape('Fire Ball (1).png')
scr.addshape('Wildfire (3).png')
scr.addshape('New Piskel')
scr.addshape('New Piskel (1)')

whp = 100
fhp = 100

fire.shape('Fire (1).png')
water.shape('Water (1).png')
wb.shape('Water Projectile (1).png')
fb.shape('Fire Ball (1).png')

fire.penup()
water.penup()
wb.penup()
fb.penup()
fb.hideturtle()
wb.hideturtle()
fire.goto(80,8)
water.goto(-160,0)
wb.goto(-160,20)
fb.goto(80,0)

def wp():
  global fhp
  global whp
  water.goto(50,0)
  water.shape('Water Punch (1).png')
  time.sleep(.5)
  water.shape('Water (1).png')
  water.goto(-160,0)
  fhp -= 10
  
def fp():
  global fhp
  global whp
  fire.goto(-97,8)
  fire.shape('Fire Punch (1).png')
  time.sleep(.5)
  fire.shape('Fire (1).png')
  fire.goto(80,8)
  whp -= 10
  
def wb1():
  global fhp
  global whp
  wb.showturtle()
  wb.goto(80,8)
  wb.hideturtle()
  wb.goto(-160,20)
  fhp -= 20

def fb1():
  global fhp
  global whp
  fb.showturtle()
  fb.goto(-160,8)
  fb.hideturtle()
  fb.goto(80,20)
  whp -= 20
  
def wildfire():
  global fhp
  global whp
  fire.shape('Wildfire (3).png')
  time.sleep(.7)
  fire.shape('Fire (1).png')
  whp /= 2
  
def tsunami():
  global fhp
  global whp
  water.shape('Tsunami (1).png')
  time.sleep(.7)
  water.shape('Water (1).png')
  fhp /= 2

def wa():
  global fhp 
  global whp
  if whp > 0 and fhp > 0:
    print ('Fire HP:' + str(fhp))
    print ('Water HP:' + str(whp))
    print ('Input the attck number that you wish to use.')
    print ('''Atacks:
      1. Punch
      2. Wave
      3. Tsunami''')
    attack = input()
    prob = random.randint(1,100)
    
    if attack == '1':
      wp()
      os.system("clear")
    if attack == '2' and prob >= 50:
      wb1()
      os.system("clear")
    if attack == '2' and prob < 50 or attack == '3' and prob > 20:
      print ('Water Attack Failed\n')
      time.sleep(1)
      os.system("clear")
    if attack == '3' and prob <= 20:
      tsunami()
      os.system("clear")
    
def fa():
  global fhp
  global whp 
  if whp > 0 and fhp > 0:
    attack = random.randint(1,3)
    prob = random.randint (1,100)
    if attack == 1:
      fp()
    if attack == 2 and prob >= 50:
      fb1()
    if attack == 2 and prob < 50 or attack == 3 and prob > 20:
      print ('Fire Attack Failed\n')
      time.sleep(1)
      os.system("clear")
    if attack == 3 and prob <= 20:
      wildfire()

def fdc():
  global fhp
  global fire
  if fhp <=0:
    print ("Water Won!")
    fire.goto (1000,1000)
    
def wdc():
  global whp
  global water
  if whp <=0:
    print ("Fire Won!")
    water.goto (-1000,-1000)

while fhp>0 and whp>0:
  wa()
  fdc()
  fa()
  wdc()
  