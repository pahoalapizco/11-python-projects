# Function that evaluate if a number is odd

def is_odd(num: int) -> bool:
    return num % 2 != 0

def play():
  num = ''
  while True:
    num = input('Type a number between 1 and 1000 to evaluate if is an odd number: ')

    if num.isdigit():
      num = int(num)
      if num in range(1, 1001):
        break


  if is_odd(num):
     print(f'{num} is an odd number')
  else:
     print(f'{num} is not an odd number')


if __name__ == '__main__':
    play()