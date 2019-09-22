"""

R.o.G. Game Client

Built with care upon the official Arcade reference template found at
http://arcade.academy/examples/starting_template.html#starting-template

"""

# standard libraries in alphabetical order
import random
import time

# external libraries in alphabetical order
import arcade

# my local libraries in alphabetical order
# import something

# global constants

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "R.o.G."


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        # If you have sprite lists, you should create them here,
        # and set them to None

        # sprite lists
        self.player_list = None
        self.star_list = None
        self.enemy_list = None

        self.player_sprite = None
        self.player_x = 0
        self.player_y = 0

        self.frames = 0
        self.last_fps_time = int(time.time())
        self.last_fps_frames = 0
        self.fps = 0
        self.fps_x = 0
        self.fps_y = 0

        self.target_x = 0
        self.target_y = 0

    def setup(self):
        # Create your sprites and sprite lists here
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("images/marauder.png", 1)
        self.player_sprite.center_x = int(SCREEN_WIDTH / 2)
        self.player_sprite.center_y = int(SCREEN_HEIGHT / 2)

        self.player_list.append(self.player_sprite)

        for i in range(15):
            star = arcade.Sprite("images/star_red.png", random.uniform(0.01, 0.06))
            star.center_y = random.randrange(0, SCREEN_HEIGHT)
            star.center_x = random.randrange(0, SCREEN_WIDTH)
            self.star_list.append(star)

        for i in range(15):
            star = arcade.Sprite("images/star_black.png", random.uniform(0.03, 0.15))
            star.center_y = random.randrange(0, SCREEN_HEIGHT)
            star.center_x = random.randrange(0, SCREEN_WIDTH)
            self.star_list.append(star)

        # for i in range(15):
        #     star = arcade.Sprite("images/star_blue.png", random.uniform(0.01, 0.02))
        #     star.center_y = random.randrange(0, SCREEN_HEIGHT)
        #     star.center_x = random.randrange(0, SCREEN_WIDTH)
        #     self.star_list.append(star)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Draw our sprite lists from bottom to top
        self.star_list.draw()
        self.enemy_list.draw()
        self.player_list.draw()

        # Increment our frame counter and draw FPS data
        self.frames += 1
        self.draw_fps()

    def draw_player(self):
        pass

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.player_sprite.angle += 1
        # self.player_sprite.scale *= 0.999

        for star in self.star_list:
            star.center_y -= star.scale * 100

            if star.center_y < -100:
                star.center_y = SCREEN_HEIGHT + 100
                star.center_x = random.randrange(0, SCREEN_WIDTH)

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.target_x = x
        self.target_y = y
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def draw_fps(self):
        """
        Draw the FPS counter

        """

        # Record the current time in seconds
        time_new = int(time.time())

        # If the second have changed update the last FPS
        if time_new != self.last_fps_time:
            self.last_fps_time = time_new
            self.fps = self.frames - self.last_fps_frames
            self.last_fps_frames = self.frames

        # Draw our FPS data
        arcade.draw_text("FPS: " + str(self.fps) + "\nFrames: " + str(self.frames), self.fps_x, self.fps_y,
                         arcade.color.WHITE, 12)

    def draw_reticle(self):
        # Draw a point at the target
        arcade.draw_line(self.target_x - 32, self.target_y, self.target_x + 32, self.target_y, arcade.color.RED, 4)
        arcade.draw_point(self.target_x, self.target_y, arcade.color.RED, 20)


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
