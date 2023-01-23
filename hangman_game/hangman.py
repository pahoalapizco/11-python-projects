from more_itertools import locate 

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


def play():
  text = 'Hello world'.upper()
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
    print(chances)


  draw(6 - chances)
  if chances == 0:
    print(f'Sorry you lose, the sentense was: {text}')
  else:
    print(f'Congrats! you won in your {6 - chances} try')


if __name__ == '__main__':
  play()
