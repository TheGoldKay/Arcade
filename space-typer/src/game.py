import os
import sys
import random
import shelve
from enum import Enum

import arcade
import pygame

import src.word
import src.star

sys.path.append("/home/goldkay/Code/Arcade")
from helper.keys import code2char, char2code

class GameStates(Enum):
    GAME_OVER = 0
    RUNNING = 1

class Game(arcade.Window):
    def __init__(self, width, height, words, word_rows_count=20):
        super().__init__(width, height, title="Space Typer")
        arcade.set_background_color((5, 2, 27))

        self.screen_width = width
        self.screen_height = height
        self.words = words
        self.word_rows_count = word_rows_count

        self.high_score = int()

        self.score = int()
        self.lives = int()
        self.state = None
        self.focus_word = None # The word that is currently being focused on / typed

        self.word_list = set()
        self.star_list = set()
        
        # Initialize pygame mixer
        pygame.mixer.init()

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.score = 0
        self.lives = 3
        self.state = GameStates.RUNNING
        self.focus_word = None
        
        self.type_sound = pygame.mixer.Sound("assets/blocky.wav")

        self.star_list = set()
        self.word_list = set()

        for _ in range(5):
            self.create_word()
        for _ in range(25):
            self.create_star()
            
    def _typing_sound(self):
        self.type_sound.stop()
        self.type_sound.set_volume(0.5)
        self.type_sound.play()
    
    def draw_game_over(self):
        arcade.draw_text("Game Over",
            self.screen_width / 2, (self.screen_height / 2) + 68,
            arcade.color.WHITE, 54,
            align="center", anchor_x="center", anchor_y="center"
        )

        arcade.draw_text("Press SPACE to restart",
            self.screen_width / 2, (self.screen_height / 2),
            arcade.color.WHITE, 24,
            align="center", anchor_x="center", anchor_y="center"
        )

        arcade.draw_text("q to quit",
                         self.screen_width / 2, (self.screen_height / 2) - 35,
                         arcade.color.WHITE, 24,
                         align="center", anchor_x="center", anchor_y="center"
                         )

        arcade.draw_text(f"Current score : {self.score}", 15, 15,arcade.color.WHITE, 14,)
        arcade.draw_text(f"High score : {self.high_score}", self.screen_width - 15, 15, arcade.color.WHITE, 14,
            align="right", anchor_x="right", anchor_y="baseline"
        )
    
    def draw_game(self):
        for word in self.word_list:
            word.draw()
        
        arcade.draw_text(f"Score : {self.score}", 15, 15, arcade.color.WHITE, 14)
        arcade.draw_text(f"Lives : {self.lives}", self.screen_width - 15, 15, arcade.color.WHITE, 14, align="right", anchor_x="right", anchor_y="baseline")

    def on_draw(self):
        arcade.start_render()

        for star in self.star_list:
            star.draw()

        if self.state == GameStates.RUNNING:
            self.draw_game()
        else:
            self.draw_game_over()
    
    def create_word(self):
        # Find a row that's currently not occupied by another word.
        row = int()
        occupied_rows = set()
        while True:
            row = random.randrange(self.word_rows_count)
            for word in self.word_list:
                occupied_rows.add(word.row)
            if row not in occupied_rows:
                break
        
        # Find a word that starts with a character that is not the first
        # character of another word.
        occupied_chars = set()
        for word in self.word_list:
            occupied_chars.add(word.word[0])
        rand_word = str()
        while True:
            rand_word = random.choice(self.words)
            if rand_word[0] not in occupied_chars:
                break
        
        self.word_list.add(src.word.Word(rand_word, row, self.screen_width, self.screen_height, self.word_rows_count))

    def create_star(self):
        self.star_list.add(src.star.Star(self.screen_width, self.screen_height))
    
    def update(self, delta_time):
        """ Movement and game logic """
        for star in self.star_list:
            star.x -= star.speed * delta_time
            if star.x < 0:
                star.reset_pos(self.screen_width, self.screen_height)

        if self.state == GameStates.RUNNING:
            for word in self.word_list:
                word.x -= 100 * delta_time
                if word.x < 0:
                    if self.focus_word == word:
                        self.focus_word = None

                    self.lives -= 1

                    self.word_list.discard(word)
                    self.create_word()
            
            if self.lives <= 0:
                path = os.path.join(os.path.abspath(".space-typer"))
                score_file = shelve.open(path)
                new_high_score = int()
                if score_file.get("high_score") == None:
                    new_high_score = self.score
                else:
                    new_high_score = max([self.score, score_file["high_score"]])
                score_file["high_score"] = new_high_score
                self.high_score = new_high_score
                score_file.close() # always splicitly close a shelve file
                self.state = GameStates.GAME_OVER

    def _get_leftmost_word_starting_with(self, character):
        words_starting_with_given_character = []
        for word in self.word_list:
            if word.word[0].lower() == character:
                words_starting_with_given_character.append(word)
        if len(words_starting_with_given_character) == 0:
            return None
        else:
            leftmost_word = min(words_starting_with_given_character, key=lambda word: word.x)
            return leftmost_word

    def on_key_press(self, key_code, modifiers):
        if key_code == arcade.key.ESCAPE:
            sys.exit()
        
        if self.state == GameStates.GAME_OVER:
            if key_code == arcade.key.SPACE:
                self.setup()
                self.state = GameStates.RUNNING
                return
            elif key_code == arcade.key.Q:
                sys.exit()

        key_char = code2char(key_code)
        if self.focus_word == None:
            self.focus_word = self._get_leftmost_word_starting_with(key_char)
            if self.focus_word != None:
                self.focus_word.in_focus = True
                self.focus_word.attack()
                self._typing_sound()
        else:
            if self.focus_word.word[0].lower() == key_char:
                self.focus_word.attack()
                self._typing_sound()

        if self.focus_word != None:
            if self.focus_word.word == "":
                self.word_list.discard(self.focus_word)
                self.focus_word = None
                self.score += 1
                self.create_word()
