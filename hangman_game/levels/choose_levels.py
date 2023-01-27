import random

class Choose:
   
  def __init__(self):
     self.__usr_level = ''
     self.__usr_typeof_game = ''
     self.__secret_name = ''
     self.__levels = {
        'easy': {
          'songs': ('Imagine', 'Hey Jude', 'One', 'Unholy', 'Flowers'),
          'movies': ('The menu', 'John Wick', 'Transcendence', 'Matrix', 'Gravity')      
        },

        'mid': {
          'songs': ('Poker face', 'Call me maybe', 'A sky full of stars', 'The foundations of decay', 'Misery business'),
          'movies': ('The Pale Blue Eye','Blade Runner', 'Manchester by the Sea', 'King Richard', 'The martian')      
        },
                    
        'hard': {
          'songs': ('I Can not Get No Satisfaction','Smells Like Teen Spirit', 'Hymn for the weekend', 'Every teardrop is a waterfall', 'Welcome to the black parade'),
          'movies': ('Everything Everywhere All At Once', 'Glass Onion A Knives Out Mystery', 'Fantastic Beasts and Where to Find Them', 'The devil wears prada', 'The Curious Case of Benjamin Button')      
        }
      }

  # Getter propeties
  @property
  def user_level(self):
    return self.__usr_level
  
  @property
  def user_typeof_game(self):
    return self.__usr_typeof_game
  
  @property
  def secret_name(self):
    return self.__secret_name
  

  # General Methods
  def choose_game(self, message):
    print(message)
    self._choose_level()
    self._choose_typeof_game()
    self._get_secret_name()

    return self.secret_name

  def _choose_level(self):
    level_options = self.__levels.keys()
    

    while True:
      user_level = input('   \n'.join(level_options) + '\n==> ')
      
      if user_level.lower() not in level_options:
        print(f'{user_level} is not in level optios, please trye again')
      else:
        self.__usr_level = user_level
        break
  
  def _choose_typeof_game(self):
    level = self.user_level
    type_options = self.__levels[level].keys()

    print(f'Select a type of game from level {level}')
    
    while True:
      user_type = input('   \n'.join(type_options) + '\n==> ')
      
      if user_type.lower() not in type_options:
        print(f'{user_type} is not in type optios from level {level}, please trye again')
      else:
        self.__usr_typeof_game = user_type
        break

  def _get_secret_name(self):
    level = self.user_level
    typeof_game = self.user_typeof_game

    tuple_of_types = self.__levels[level][typeof_game]
    random_choice = random.randint(0, len(tuple_of_types)-1)

    self.__secret_name = tuple_of_types[random_choice]


if __name__ == "__main__":
  choose = Choose()
  secrete = choose.choose_game("Select a level")
  print(secrete)
