import arcade
import time
import random

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 480
SCREEN_TITLE = "PONG"
MOVEMENT_SPEED = 3
MOVEMENT_SPEEDL = 3
BALL_SPEED = 3
COMPUTER_SCORE = 0
PLAYER_SCORE = 0
class Ball:

    
    def __init__(self, position_x, position_y, balldirection_x, balldirection_y, height, width):
        self.position_x = position_x
        self.position_y = position_y
        self.balldirection_x = balldirection_x
        self.balldirection_y = balldirection_y
        self.height = height
        self.width = width
    def draw(self):
        
        arcade.draw_circle_filled(320, 240, 10,
                              arcade.color.WHITE)
    def update(self):
        global COMPUTER_SCORE
        global PLAYER_SCORE
        global BALL_SPEED

        hitdirection = random.randint(0, 2)
        
        if self.position_y - self.height/2 < 80 or self.position_y + self.height/2 > SCREEN_HEIGHT-80:
            
            self.balldirection_y = -self.balldirection_y

        if self.position_x < 0 or self.position_x > SCREEN_WIDTH:

            if self.position_x < 0:
                COMPUTER_SCORE += 1
            else:
                PLAYER_SCORE += 1

            self.position_x = SCREEN_WIDTH/2
            self.position_y = SCREEN_HEIGHT/2

            if hitdirection == 1:
                self.balldirection_x = -self.balldirection_x
            else :
                self.balldirection_y = -self.balldirection_y

            BALL_SPEED = 1
            

            


        self.position_x += self.balldirection_x * BALL_SPEED
        self.position_y += self.balldirection_y * BALL_SPEED
class Paddle:
    def __init__(self, position_x, position_y, change_x, change_y, width, height, color):

       
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)

    def update(self):
        
        self.position_y += self.change_y
     

        
       
        if self.position_y < self.width:
            self.position_y = self.width

        if self.position_y > SCREEN_HEIGHT - self.width:
            self.position_y = SCREEN_HEIGHT - self.width


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

        # Create our Paddle
        self.Paddle = Paddle(50, 50, 0, 0, 15, 60, arcade.color.WHITE)
        self.PaddleL = Paddle(590, 50, 0, 0, 15, 60, arcade.color.WHITE)
        self.Ball = Ball(320, 240, 5, 2, 10, 10)

    def on_draw(self):

        arcade.start_render()
        self.Paddle.draw()
        self.PaddleL.draw()
        self.Ball.draw()

    def update(self, delta_time):
        self.Paddle.update()
        self.PaddleL.update()
        self.Ball.update()
    def on_key_press(self, key, modifiers):


        if key == arcade.key.W:
            self.Paddle.change_y = MOVEMENT_SPEED
        if key == arcade.key.UP:
            self.PaddleL.change_y = MOVEMENT_SPEEDL
        elif key == arcade.key.DOWN:
            self.PaddleL.change_y = -MOVEMENT_SPEEDL
        elif key == arcade.key.S:
            self.Paddle.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.W or key == arcade.key.S:
            self.Paddle.change_y = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.PaddleL.change_y =0

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()