from more_itertools import locate
from draws import draws
class Hangman:
    
  def __init__(self):
    self.__draws = draws
    self.__underscores = []
    self.errors = 0
    self.text_game = ""

  @property
  def draw(self):
    if self.errors > 6:
      raise ValueError(f'Error {self.errors} is out of range of hangman game')
    
    return self.__draws

  @property
  def underscores(self):
    return self.__underscores
  
  @underscores.setter
  def underscores(self, value):
    self.__underscores = value

  def transform_text(self):
    text = self.text_game.split()
    letters = []

    for word in text:
      for letter in word:
        letters.append(letter)
      letters.append(" ")

    letters.pop() # delete last space.
    self.underscores = [ '_' if char != ' ' else ' ' for char in letters]

  def find_letter(self, letter):
    indexes = list(locate(self.text_game, lambda char: char == letter))

    if len(indexes) > 0:
      for idx in indexes:
        self.underscores[idx] = letter

    return len(indexes), self.underscores
  
  def print_game(self):
    idx = str(self.errors)
    print(draws[idx])
    print(' '.join(self.underscores), '\n')


if __name__ == '__main__':
  game = Hangman()
  game.text_game = "this is a text"
  game.transform_text()
  game.print_game()
  print(game.find_letter("a"))
 