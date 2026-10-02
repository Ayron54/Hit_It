from turtle import *
print('Ходьба: W,A,S,D')
class Sprite(Turtle):
    def __init__(self, x, y, step = 10, shape = 'circle', color = 'yellow'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True
        else:
            return False
    def set_move(self,x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(self.x_end, self.y_end))
    def make_step(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())  
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor()) 
player = Sprite(0, -100)
square1 = Sprite(-200, -10, 100, 'square', 'red')
square1.set_move(-200, -10, 200, -10)
square2 = Sprite(200, 70, 100, 'square', 'red')
square2.set_move(200, 70, -200, 70)
end = Sprite(0, 120, 5000, 'triangle', 'green')

scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'w')
scr.onkey(player.move_right, 'd')
scr.onkey(player.move_down, 's')
scr.onkey(player.move_left, 'a')
hideturtle()
penup()
goto(0, 200)
total_score = 0
write(f'Попаданий: {total_score}', font = ('Arial', 10, 'bold'))
while total_score < 3:
    square1.make_step()
    square2.make_step()
    if player.is_collide(end):
        total_score += 1
        clear()
        write(f'Попаданий: {total_score}', font = ('Arial', 10, 'bold'))
        player.goto(0, -100)
        
    if player.is_collide(square1) or player.is_collide(square2):
        square1.hideturtle()
        square2.hideturtle()
        end.hideturtle()
        player.hideturtle()
        break
if total_score == 3:
    square1.hideturtle()
    square2.hideturtle()
    end.hideturtle()
    player.hideturtle()
