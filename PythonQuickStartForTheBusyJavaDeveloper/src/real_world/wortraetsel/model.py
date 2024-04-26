import random

from src.real_world.wortraetsel.direction import Direction
from src.real_world.wortraetsel.position import Position


class Model:
    MAX_TRYS = 5

    def __init__(self, words_to_use, words_to_place):
        self.all_possible_words = []
        self.words_to_search = []
        self.board = []

        print(words_to_use)
        self.all_possible_words += words_to_use
        self.prepare_board(words_to_place)

    def prepare_board(self, words_to_place):
        self.initialize_empty_board()
        self.place_words(words_to_place)
        self.fill_up_with_random_chars()

    def initialize_empty_board(self):
        self.board = [[' ' for x in range(self.get_board_width())]
                      for y in range(self.get_board_height())]

    def get_words_to_search(self):
        return self.words_to_search

    def get_at(self, x, y):
        return self.board[y][x]

    def get_board_width(self):
        return 20

    def get_board_height(self):
        return 10

    def choose_random_direction(self):
        return random.choice(list(Direction))

    def choose_random_position(self):
        random_x = random.randint(0, self.get_board_width())
        random_y = random.randint(0, self.get_board_height())

        return Position(random_x, random_y)

    def choose_random_word(self):
        return random.choice(self.all_possible_words)

    def random_char(self):
        return chr(random.randrange(65, 65 + 26))

    def place_words(self, words_to_place):
        impossible_to_place = 0
        while words_to_place > 0:
            if self.place_single_word():
               words_to_place -= 1
            else:
                # So verhindert man Endlosschleife
                impossible_to_place += 1
                if impossible_to_place > 5:
                    break

    def place_single_word(self):
        word_fits = False
        word = self.choose_random_word()

        current_try = 0
        while current_try < self.MAX_TRYS and not word_fits:
            pos = self.choose_random_position()
            direction = self.choose_random_direction()

            word_fits = self.word_fits_on_board(word, pos, direction)
            if word_fits:
                self.put_word_on_board(word, pos, direction)
                self.all_possible_words.remove(word)
                self.words_to_search.append(word)

            current_try += 1

        return word_fits

    def word_fits_on_board(self, word, startPos, direction):
        pos = startPos

        for ch in word:
            if self.is_on_board(pos) and self.is_empty_cell_pos(pos):
                pos = pos.adjust_to_dir(direction)
            else:
                return False

        return True

    def put_word_on_board(self, word, startPos, direction):
        pos = startPos

        for ch in word:
            self.board[pos.y][pos.x] = ch
            pos = pos.adjust_to_dir(direction)

    def is_on_board(self, pos):
        return 0 <= pos.y < self.get_board_height() and \
               0 <= pos.x < self.get_board_width()

    def is_empty_cell_pos(self, pos):
        return self.is_empty_cell(pos.x, pos.y)

    def is_empty_cell(self, x, y):
        return self.board[y][x] == ' '

    def fill_up_with_random_chars(self):
        for y in range(self.get_board_height()):
            for x in range(self.get_board_width()):
                if self.is_empty_cell(x, y):
                    self.board[y][x] = self.random_char()
