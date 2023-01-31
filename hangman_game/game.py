from more_itertools import locate
from draws import draws
from levels import choose_levels as chlvl

class Hangman:
    
  def __init__(self):
    self.__draws = draws
    self.__underscores = []
    self.__text_game = 'this is a text'.upper()
    self.errors = 0


  # Getter Properties
  @property
  def draw(self):
    if self.errors > 6:
      raise ValueError(f'Error {self.errors} is out of range of hangman game')
    
    return self.__draws

  @property
  def underscores(self):
    return self.__underscores

  # General Methods
  def transform_text(self):
    text = self.__text_game.split()
    letters = []

    for word in text:
      for letter in word:
        letters.append(letter)
      letters.append(" ")

    letters.pop() # delete last space.
    self.__underscores = [ '_' if char != ' ' else ' ' for char in letters]

  def find_letter(self, letter):
    indexes = list(locate(self.__text_game, lambda char: char == letter))

    if len(indexes) > 0:
      for idx in indexes:
        self.underscores[idx] = letter

    return len(indexes)

  def choose_level(self):
    choose = chlvl.Choose()
    self.__text_game = choose.choose_game('Welcome to the game "The Hangman", before to start you need to select a level from the list below')
    print(self.__text_game)

  def print_game(self):
    idx = str(self.errors)
    print(draws[idx])
    print(' '.join(self.underscores), '\n')


if __name__ == '__main__':
  game = Hangman()
  game.choose_level()
  # game.transform_text()
  # game.print_game()
