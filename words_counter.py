# Function that recives a string an return the total of words on it.bool

def word_counter(text: str)  -> int:
  words_list = text.split(' ')
  return len(words_list)

def play():
  user_text = input('Hey there :D how are you?, tell me, what are you thinking about? \n>>> ')
  total_words = word_counter(user_text)

  print(f'Wow you wrote your thoughts in {total_words} words, that is amazing :D')

if __name__ == '__main__':
  play()
    