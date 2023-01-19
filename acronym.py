"""
Function that recives a text and return the acronym of that text.
Exameple:
Input: As Soon As Possible
Output: ASAP

Input: World Health Organization
Output: WHO
"""

def acronym(text: str) -> str:
  splited_text = text.split(' ')
  firt_letters = [word[0].upper() for word in splited_text]
  result = ''.join(firt_letters)
  return result

  

def play():
  text = input('Which phrase do you want to transform into an acronym? ')
  acronym_text = acronym(text)
  print(f'The acronym of "{text}" is "{acronym_text}"')


if __name__ == "__main__":
  play()