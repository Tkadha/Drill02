from pico2d import *
import math

open_canvas()

# fill here

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400,30)
character.draw_now(400,90)

change=1
x = 400
y = 90
circle=0
while(1):
    clear_canvas_now()
    while(x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+5
        delay(0.01)
    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y+5
        delay(0.01)
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-5
        delay(0.01)
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-5
        delay(0.01)
    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+5
        delay(0.01)
    while(circle<360):
        clear_canvas_now()
        x=x+math.cos(circle/360*2*math.pi)*5
        y=y+math.sin(circle/360*2*math.pi)*5
        grass.draw_now(400,30)
        character.draw_now(x,y)
        circle=circle+1
        delay(0.01)
    circle=0
    
close_canvas()
