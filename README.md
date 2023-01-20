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

## Project #3 `Guess the number`
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