import random

levels = {
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

def get_level_options():
    return levels.keys()

def get_type_of_game(level):
    return levels[level].keys()

def get_name(level, game_type):
  tuple_of_types = levels[level][game_type]
  random_choice = random.randint(0, len(tuple_of_types)-1)

  return tuple_of_types[random_choice]

if __name__ == "__main__":
  pass
