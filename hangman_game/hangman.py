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


def play():
  text = 'Hello world'.upper()
  chances = 6
  game = transform_into_unders(text)
  hits = 0

  while chances > 0:

    print(game)
    user_input = input('Which letter do you think is part of the text: ')

    occurrences, game = find_letter(user_input.upper(), text, game)
    if occurrences == 0 :
      chances -= 1
    else:
      hits += occurrences
    
    if hits == len(text.strip()): break


  if chances == 0:
    print(f'Sorry you lose, the sentense was: {text}')
  else:
    print(f'Congrats! you won in your {6 - chances} try')


if __name__ == '__main__':
  play()
