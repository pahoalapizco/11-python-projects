# Welcome to 11 python projects :snake:

In this repo you'll find eleven basic projects that I crerated to improve my coding skills using python.  

I hope you like them as well as I did, in case you have feedback on any project please tell me by DM or make a pull request.

## Project #1 `Odd numbers`
In this little project has two functions 

`is_odd(num: int)`: Evaluate if a number is odd or not.
<br/>
`play()`: It asks the user to type a number between 1 and 1000 and then evaluate if that number is odd or not.

### **Run this project:**
```
python3 odd_numers.py
```

**Output**
```
Type a number between 1 and 1000 to evaluate if is an odd number: 1001
Type a number between 1 and 1000 to evaluate if is an odd number: hello
Type a number between 1 and 1000 to evaluate if is an odd number: 8
8 is not an odd number
```

## Project #2 `Words counter`
`word_counter(text: str)`: It takes a string and count the total of words on it.
<br/>
`play()`: It asks the user to type some text with its thoughts and then show how many words have been found in that text.
### **Run this project:**
```
python3 words_counter.py
```

**Output**
```
Hey there :D how are you?, tell me, what are you thinking about? 
>>> Hi, now I'm thinking and practicing how to improve my coding skills with python
Wow you wrote your thoughts in 14 words, that is amazing :D
```

## Project #3 `Acronym`
`acronym(text: str)`: It takes the first letter of each word that the text contains.
<br/>

`play()`: It asks the user to type some phrase to transform into an acronym.

### **Run this project:**
```
python3 acronym.py
```

**Output**
```
Which phrase do you want to transform into an acronym? As soon As posible
The acronym of "As soon As posible" is "ASAP"
```

## Project #4 `Guess the number`
In this little game, the user has to try to guess a number between 1 and 50 in three opportunities.
Each try could have a clue to help the user wins the game, only if the user want it.

`get_user_number()`: This function asks the user for a number and evaluates if the answer is a number and belongs to the range 1-50.
<br/>

`guess_number(user_number: int)`: This functions evaluates if the user's number is equal to the secrert number.
<br/>

`play()`: It starts a new game, in case the user loses a try, the game shows a menu with the following options:
```
  - If you want to continue with a clue type: y
  - If you want to continue without a clue type: n
  - If you want to finish the game type any key
```

### **Run this project:**
```
python3 guess_the_number.py
```

**Output**
```
Hello, you have 3 opportunities to guess the secret number.
Try # 1
Try to guess the number, type a number between 1 and 50: 5
Sorry, 5 is not the secret number.

  - If you want to continue with a clue type: y
  - If you want to continue without a clue type: n
  - If you want to finish the game type any key

...
```

## Project #5 `Tips Calculator`
This project can help to calculate the total tips you want to pay for a service

Main functions:
`calculate(subtotal: float, tip: float)`: This functiones execute the calculos `subtotal * tips`, first of all transform the tips into percent value (tips/100)
<br/>

`validate_float_input(value: str)`: It Evaluates if the value is float.
<br/>

Test function:
`run()`: Ask the user the amount of subtotal and tips, then shows the total amount.

### **Run this project:**
```
python3 tip-calculator.py
```

**Output**
```
How mush is on your check? $100
How many perfent of tip do you want to pay? 10
 
  This is your total check:
    Sub total: $ 100.0
         tips: $ 10.0  10.0%
    _________________________
        total: $ 110.0
```

## Project 6 - The Hangman Game
This project is the traditional game "The Hangman" where you have to guess a word or sentence with only 6 chances to make a mistake, 
each mistake draws a body part of "The Hangman" until it will be completed.
<br />

This game has three leves: Easy, Mid and Hard.
<br />
Each level has two types of game: Songs and Movies.
<br />

#### `How levels are represented in code`:
```
levels = {
  'easy': {
    'songs': (),
    'movies': (),
  }
  ...
}
```
This project uses a cutom module to get leves and types of game. 
<br />
The module's name is: level, it contains the folowing functions:

`levels`: Dictionary with the lavels and types of game
<br />

`get_level_options()`: Returns all levels in the dictionary
<br />

`get_type_of_game(level)`: Returns all types of game of the selected level.
<br />

`get_name(level, game_type)`: Returns an aleatory name of the level and type of game selected.
<br />

The main code contains the folowing functinos:
<br />

`transform_into_unders(text)`: Takes a text and transforms each letter of it into an underscore.
<br />

`find_letter(letter, text, game)`: Takes the original text and validates if a letter exists on it, also validates if the letter is already in the game.
<br />

`draw(errors)`: This functions draws "The Hangman.
<br />

`select_level()` and `select_type(level)`: They ask to the user for a level and type of game. Each one validates if the user intput is correct. 
<br />

`get_secret_name()`: Returns the name of a song or movie that the user has to guess.
<br />

`play()`: Starts the game.
<br />

### Create virtual env and install dependencies before start the game
```
cd hangman_game
python3 -m venv env
source env/bin/activate

pip install -r requirements.txt
```

### **Run this project:**
```
python3 hangman.py  
```

**Output**
```
Welcome to the game "The Hangman", before to start you need to select a level from the list below
easy   
mid   
hard
```
**Intput**
```
==> easy
```

**Output**
```
Select a type of game from level easy
songs   
movies
```
**Intput**
```
==> songs
```
**Output**
```
|----------
|         |
|          
|          
|          
|          

_ _ _ _ _ _ _
Which letter do you think is part of the text: 
```
```
Which letter do you think is part of the text: a
|----------
|         |
|         O
|          
|          
|          

_ _ _ _ _ _ _
```
```
Which letter do you think is part of the text: e
|----------
|         |
|         O
|          
|          
|          

_ _ _ _ E _ _
Which letter do you think is part of the text: 

...
```