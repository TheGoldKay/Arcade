import arcade

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, center_window=True)

    def on_draw(self):
        arcade.start_render()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.exit()


def main():
    window = Game(1000, 500, "Dino")
    arcade.run()


if __name__ == "__main__":
    main()