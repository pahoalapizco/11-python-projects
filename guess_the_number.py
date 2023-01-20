"""
In this little game, the user has to try to guess a number between 1 and 50 in three opportunities.
Each try could hace a clue to helps the user win the game.
"""
import random

# get a random number between 1 and 50
SECRET_NUMBER = random.randint(1, 50)
CLUE_MENU = """
  - If you want to continue with a clue type: y
  - If you want to continue without a clue type: n
  - If you want to finish the game type any key
"""

def get_user_number() -> int:    
  while True:
    user_number = input('Try to guess the number, type a number between 1 and 50: ')
    
    if user_number.isdigit():
      user_number = int(user_number)
      if user_number in range(1, 51):
        break
  
  return user_number


def guess_number(user_number: int) -> bool:
  win = False

  if user_number == SECRET_NUMBER:
    print('Congratulations!, you win the game :D')
    win = True

  return win


def play():
  finished = False
  counter = 0
  print('Hello, you have 3 opportunities to guess the secret number.')

  while counter < 3 and not finished:
    counter +=1
    print(f'Try # {counter}')
    user_number = get_user_number()
    finished = guess_number(user_number)

    if counter == 3: break

    if not finished:
      print(f'Sorry, {user_number} is not the secret number.')
      clue = input(CLUE_MENU)
      if clue.lower() == 'y':
        if user_number > SECRET_NUMBER:
          print(f'The secret number is under that you typed ({user_number})')
        else:
          print(f'The secret number is over that you typed ({user_number})')
      elif clue.lower() == 'n':        
        continue
      else:
        break
  
  
  if finished:
    print(f'You win the game in your try # {counter}')
  else:
    print(f'Sorry :( you lose the game, the secret number was {SECRET_NUMBER}')


if __name__ == "__main__":
  play()