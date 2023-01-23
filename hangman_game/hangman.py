from more_itertools import locate 
from levels import levels as lvl

def transform_into_unders(text):
  text = text.split()
  letters = []

  for word in text:
    for letter in word:
      letters.append(letter)
    letters.append(" ")


  letters.pop() # delete last space.
  return [ '_' if char != ' ' else ' ' for char in letters]


def find_letter(letter, text, game):
  indexes = list(locate(text, lambda char: char == letter))

  if len(indexes) > 0:
    for idx in indexes:
      game[idx] = letter

  return len(indexes), game


def draw(errors):
  hangman_draw = [
    ['|','-','-','-','-','-','-','-','-','-','-',''],
    ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ', '|',''],
    ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ',''],
    ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ',''],
    ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ',''],
    ['|',' ',' ',' ',' ',' ',' ',' ',' ',' ', ' ','']
  ]

  drawing = ''

  if errors > 0:
    for error_num in range(1, errors+1):
      if error_num == 1:
        hangman_draw[2][10] = 'O'
      elif error_num == 2:
        hangman_draw[3][10] = '|'
      elif error_num == 3:
        hangman_draw[3][9] = '/'
      elif error_num == 4:
        hangman_draw[3][11] = '\\'
      elif error_num == 5:
        hangman_draw[4][9] = '/'
      elif error_num == 6:
        hangman_draw[4][11] = '\\'

  for row in hangman_draw:
    drawing += ''.join(row)
    drawing += '\n'

  print(drawing)

def select_level():
  text = ''
  level_options = lvl.get_level_options()
  print('Welcome to the game "The Hangman", before to start you need to select a level from the list below')
  
  while True:
    user_level = input('   \n'.join(level_options) + '\n==> ')
    
    if user_level.lower() not in level_options:
      print(f'{user_level} is not in level optios, please trye again')
    else:
      text = user_level
      break

  return text

def select_type(level):
  text = ''
  type_options = lvl.get_type_of_game(level)

  print(f'Select a type of game from level {level}')
  
  while True:
    user_type = input('   \n'.join(type_options) + '\n==> ')
    
    if user_type.lower() not in type_options:
      print(f'{user_type} is not in type optios from level {level}, please trye again')
    else:
      text = user_type
      break
    
  return text

def get_secret_name():
  level = select_level()
  user_type = select_type(level)

  secret_name = lvl.get_name(level, user_type)

  return secret_name

def play():
  text = get_secret_name().upper()
  chances = 6
  game = transform_into_unders(text)
  hits = 0

  while chances > 0:
    draw(6 - chances)
    print(' '.join(game))
    user_input = input('Which letter do you think is part of the text: ').upper()

    if user_input in game:
      continue

    occurrences, game = find_letter(user_input, text, game)
    if occurrences == 0 :
      chances -= 1
    else:
      hits += occurrences
    
    if hits == len(text.strip()): break


  draw(6 - chances)
  if chances == 0:
    print(f'Sorry you lose, the sentense was: {text}')
  else:
    print(f'Congrats! you won in your {6 - chances} try')


if __name__ == '__main__':
  play()
