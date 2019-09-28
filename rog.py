"""

R.o.G. Game Client

Built with care upon the official Arcade reference template found at
http://arcade.academy/examples/starting_template.html#starting-template

"""

# standard libraries in alphabetical order
import math
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
THRUST_MAX = 400
THRUST_MIN = -50
THRUST_ACCELERATION = 250
SPIN_RATE = 125


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
        self.world_map_list = None
        self.player_list = None
        self.star_list = None
        self.enemy_list = None

        self.world_map_sprite = None
        self.player_sprite = None

        self.player_location_x = 0
        self.player_location_y = 0
        self.player_thrust_value = 0
        self.player_thrust_angle = 0
        self.player_thrust_x = 0
        self.player_thrust_y = 0

        self.frames = 0
        self.last_fps_time = int(time.time())
        self.last_fps_frames = 0
        self.fps = 0
        self.fps_x = 0
        self.fps_y = 0

        self.target_x = 0
        self.target_y = 0

        # Create control flags to track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.b_pressed = False

    def setup(self):
        # Create your sprites and sprite lists here
        self.world_map_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        # create the player sprite and append it to the player list
        # self.player_sprite = arcade.Sprite("images/marauder.png", 1)
        self.player_sprite = arcade.Sprite("images/bio-tier1.png", 0.5)
        self.player_sprite.center_x = int(SCREEN_WIDTH / 2)
        self.player_sprite.center_y = int(SCREEN_HEIGHT / 2)
        self.player_list.append(self.player_sprite)

        # create the world map sprite and append it to the world map list
        self.world_map_sprite = arcade.Sprite("images/jupiter.jpg")
        self.world_map_sprite.scale = 1
        self.world_map_list.append(self.world_map_sprite)
        
        for i in range(15):
            star = arcade.Sprite("images/star_red.png", random.uniform(0.01, 0.06))
            star.center_y = random.randrange(0, SCREEN_HEIGHT)
            star.center_x = random.randrange(0, SCREEN_WIDTH)
            self.star_list.append(star)
        
        # for i in range(15):
        #     star = arcade.Sprite("images/star_black.png", random.uniform(0.03, 0.15))
        #     star.center_y = random.randrange(0, SCREEN_HEIGHT)
        #     star.center_x = random.randrange(0, SCREEN_WIDTH)
        #     self.star_list.append(star)

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
        self.world_map_list.draw()
        self.star_list.draw()
        self.enemy_list.draw()
        self.player_list.draw()

        if self.player_thrust_x != 0 or self.player_thrust_y != 0:
            arcade.draw_line(
                self.player_sprite.center_x, 
                self.player_sprite.center_y, 
                self.player_sprite.center_x - self.player_thrust_x, 
                self.player_sprite.center_y + self.player_thrust_y,
                arcade.color.RED,
                5
            )

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
        # self.player_sprite.angle += 1
        # self.player_sprite.scale *= 0.999

        # for star in self.star_list:
        #     star.center_y -= star.scale * 100
        #
        #     if star.center_y < -100:
        #         star.center_y = SCREEN_HEIGHT + 100
        #         star.center_x = random.randrange(0, SCREEN_WIDTH)

        # re-angle ship and constrain the angle as 0-360
        if self.left_pressed:
            self.player_sprite.angle += delta_time * SPIN_RATE
        if self.right_pressed:
            self.player_sprite.angle -= delta_time * SPIN_RATE
        if self.player_sprite.angle < 0:
            self.player_sprite.angle += 360
        if self.player_sprite.angle > 360:
            self.player_sprite.angle -= 360

        if self.b_pressed:
            self.world_map_sprite.center_x = 0
            self.world_map_sprite.center_y = 0
            self.player_thrust_x = 0
            self.player_thrust_y = 0

        # calculate new thrust contribution
        if self.up_pressed or self.down_pressed:
            thrust_contribution = THRUST_ACCELERATION * delta_time
            if self.down_pressed:
                thrust_contribution *= -1
            thrust_angle = self.player_sprite.angle + 90
            if thrust_angle < 0:
                thrust_angle += 360
            if thrust_angle > 360:
                thrust_angle -= 360

            thrust_component_x = math.cos(math.radians(180 - thrust_angle)) * thrust_contribution
            thrust_component_y = math.sin(math.radians(180 - thrust_angle)) * thrust_contribution

            self.player_thrust_x += thrust_component_x
            self.player_thrust_y += thrust_component_y

        self.world_map_sprite.center_x += self.player_thrust_x * delta_time
        self.world_map_sprite.center_y -= self.player_thrust_y * delta_time

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.B:
            self.b_pressed = True

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
        elif key == arcade.key.B:
            self.b_pressed = False

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
        arcade.draw_text(
            # Text
            # "Coordinates: " + str(self.world_map_sprite.center_x) + ", " + str(0 - self.world_map_sprite.center_y) +
            # "\nThrust X: " + str(self.player_thrust_x) +
            # "\nThrust Y: " + str(self.player_thrust_y) +
            # "\nTotal Thrust: " + str(math.sqrt(self.player_thrust_y *  self.player_thrust_y + self.player_thrust_x * self.player_thrust_x )) +
            # "\nShip Angle: " + str(self.player_sprite.angle) +
            "\nFPS: " + str(self.fps) +
            "\nFrames: " + str(self.frames),
            # Location, color & size
            self.fps_x, self.fps_y,
            arcade.color.WHITE,
            14
        )

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

