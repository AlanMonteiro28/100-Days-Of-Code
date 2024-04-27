import turtle
import random
#tamanho da janela
width = 500
height = 500
#espaço entre cada pintada
spacing = 50
#posição inicial da tartaruga
start_x = -width/2 + 20
start_y = -height/2 + 20
#contador de quantas linhas foram desenhadas
line_painted = 0

timmy = turtle.Turtle(shape="turtle", visible=False)  #declara que terá forma de tartaruga e que não será visivel inicialmente
screen = turtle.Screen()
screen.setup(width, height)     #define o tamanho da janela

#configurando a tartaruga
timmy.speed("fastest")  #velocidade para pintar
turtle.colormode(255)  #definindo qual o modo de cor
timmy.pensize(10)  #definindo o tamanho do pincel
color_list = [(235, 234, 234), (233, 234, 238), (237, 240, 238), (210, 163, 107), (235, 220, 227), (20, 28, 57), (142, 60, 93), (227, 208, 127), (208, 129, 144), (213, 77, 103), (83, 116, 97), (59, 92, 140), (127, 152, 141), (68, 21, 41), (127, 33, 55), (40, 52, 105), (143, 72, 55), (226, 181, 164), (230, 162, 178), (138, 155, 177), (92, 126, 173), (113, 135, 122), (178, 110, 94), (183, 188, 205), (185, 199, 180), (37, 85, 62), (208, 122, 41), (34, 71, 53), (44, 70, 78), (111, 47, 35)]

# code
timmy.penup()   #para que não vá pintando até o ponto inical desejado
timmy.goto(start_x, start_y)


def painting(num_paint):    #função para pintar sendo num_paint a quantidade de vezes já pintada definida por um loop for
    timmy.showturtle()
    timmy.pencolor(random.choice(color_list))
    timmy.pendown()
    timmy.circle(5)
    timmy.penup()
    if num_paint < 9:
        timmy.forward(spacing)


while True:
    for i in range(10):
        painting(num_paint=i)
    line_painted += 1
    start_y += spacing
    timmy.hideturtle()
    timmy.goto(start_x, start_y)
    if line_painted == 10:
        break

screen.exitonclick()
