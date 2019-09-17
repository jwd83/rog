"""

R.o.G. Game Client

Built with care upon the official Arcade reference template found at
http://arcade.academy/examples/starting_template.html#starting-template

"""
import time

import arcade

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

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.frames = 0
        self.last_fps_time = int(time.time())
        self.last_fps_frames = 0
        self.fps = 0

        self.fps_x = 0
        self.fps_y = 0

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Process frame rate data
        # Increment our frame counter
        self.frames += 1

        # Record the current time in seconds
        time_new = int(time.time())

        # If the second have changed update the last FPS
        if time_new != self.last_fps_time:
            self.last_fps_time = time_new
            self.fps = self.frames - self.last_fps_frames
            self.last_fps_frames = self.frames

        # Draw our framerate data
        arcade.draw_text("FPS: " + str(self.fps) + "\nFrames: " + str(self.frames), self.fps_x, self.fps_y, arcade.color.BLACK, 12)

        # Call draw() on all your sprite lists below

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

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
        self.fps_x = x
        self.fps_y = y
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


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
