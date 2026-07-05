# Write your code here.
#Task1
################################
def hello():
    return "Hello!"
#print(hello())

#Task 2: Greet with a Formatted String
################################
def greet(name):
    return f"Hello, {name}!"
#print(greet("James"))

#Task 3: Calculator
# Write a calc function. It takes three arguments.
#  The default value for the third argument is "multiply". 
# The first two arguments are values that are to be combined using the operation 
# requested by the third argument, a string that is one of the following add,
#  subtract, multiply, divide, modulo, int_divide (for integer division) and power.
#  The function returns the result.
# Error handling: When the function is called, it could ask you to divide by 0.

def calc(number1, number2, operation = "multiply"):
   
   

    if operation == "multiply":
        try:
            result = number1*number2
        except TypeError: 
            result = "You can't multiply those values!"
        return result
    elif operation =="add":
        result = number1 + number2
        return result
    elif operation == "divide":
        try:
            result = number1/number2
         
        except ZeroDivisionError:
            result=("You can't divide by 0!")
        return result   
        
    elif operation == "subtract":
        result = number1-number2
        return result
    elif operation == "modulo":
        result = number1%number2
        return result
    elif operation == "power":
        result = number1**number2
        return result
    elif operation == "int_divide":
        result= number1//number2
        return result
    
    #Task 4: Data Type Conversion
# Create a function called data_type_conversion. 
# It takes two parameters, the value and the name of the data type requested, 
# one of float, str, or int. Return the converted value.
# Error handling: The function might be called with a bad parameter. 

def data_type_conversion(value, type):
    try:
        if type == "float":
            result = float(value)
            return result
        elif type == "str":
            result = str(value)
            return result
        elif type == "int":
            result = int(value)
            return result
    except ValueError:
        result = f"You can't convert {value} into a {type}."
        return result
    

#print(data_type_conversion("banana", "int"))
    
    #Task 5: Grading System, Using *args
# Create a grade function. \
# It should collect an arbitrary number of parameters, 
# compute the average, and return the grade. 
# based on the following scale, popular in American schools:
# A: 90 and above
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
#

def grade(*args):
    try:
        average = sum(args)/len(args)
        if average >= 90:
            grade = "A"
        elif average>=80:
            grade = "B"
        elif average>=70:
            grade = "C"
        elif average>=60:
            grade = "D"
        elif average<60:
            grade = "F"
        return grade
    except :
        grade = "Invalid data was provided."
    return grade

    #Task 6: Use a For Loop with a Range
# Create a function called repeat. It takes two parameters, 
# a string and a count, and returns a new string that is the old one repeated
#  count times.
# You could return string * count to pass the test — but for this task,
#   use a for loop and a range.
def repeat(string, count):
    str=""
    for i in range (1, count+1):
        str = str +string
    return str

    #Task 7: Student Scores, Using **kwargs
# Create a function called student_scores. 
# It takes one positional parameter and an arbitrary 
# number of keyword parameters. 
# The positional parameter is either "best" or "mean". 
# If it is "best", the name of the student with the highest score is returned. 
# If it is "mean", the average score is returned.
#

def student_scores(param, **kwargs):
    if param == "best":
        max=0
        k_max=""
        for k, v in kwargs.items():
           if max < v:
               max = v
               k_max=k
        return k_max
    
    elif param == "mean":
        avg=0
        sum =0
        for v in kwargs.values():
            sum = sum+v
        avg=sum/len(kwargs)
        return avg 
    
#print(student_scores("best", Tom=75, Dick=89, Angela=91))
#print(student_scores("mean", Tom=75, Dick=89, Angela=91))


#Task 8: Titleize, with String and List Operations
# Create a function called titleize. It accepts one parameter, a string.
#  The function returns a new string, where the parameter string is capitalized
#  as if it were a book title.
# The rules for title capitalization are:
#  (1) The first word is always capitalized.
#  (2) The last word is always capitalized. 
# (3) All the other words are capitalized, except little words. 
# For the purposes of this task, the little words are 
# "a", "on", "an", "the", "of", "and", "is", and "in".


def titleize(string):
    little_words=["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split(" ")
    #print(words)
    result=[]
   
    first_word = words[0].capitalize()
    if len(words)==1:
        result=first_word
        return result
   # print(first_word)
    last_word = words[-1].capitalize()
   # print(last_word)
    result.append(first_word)
   # print(result)
    for i in range(1, len(words)-1):
        if words[i] in little_words:
            result.append(words[i])
           # print("I;m here in little words")
          #  print(f"If loop {i} {result}")

        else:
            result.append(words[i].capitalize())
           # print(result)

    result.append(last_word)
    result=" ".join(result)
    return result
    
    #Task 9: Hangman, with more String Operations
# Create a function hangman. It takes two parameters, both strings, 
# the secret and the guess.
# The secret is some word that the caller doesn't know.
#  So the caller guesses various letters, which are the ones in the guess string.
# A string is returned. Each letter in the returned string corresponds 
# to a letter in the secret, except any letters that are not in the guess
#  string are replaced with an underscore. The others are returned in place.
#  Not everyone has played this kid's game, but it's common in the US.
# Example: Suppose the secret is "alphabet" and the guess is "ab".
#  The returned string would be "a___ab__".
#

def hangman(secret,guess):
    secret=secret.lower()
    result=[]
    for i in range(len(secret)):
        result.append("_")
   
   # print(result)
   
    for j in range(len(guess)):
        print("first letter",j)
        for i, letter in enumerate(secret):
            if guess[j]==letter:
                number=i
                result[number]=letter
              
    result="".join(result)
    return result
#hangman("whotheare","we")


    #Task 10: Pig Latin, Another String Manipulation Exercise
# Pig Latin is a kid's trick language.
#  Each word is modified according to the following rules.
#  (1) If the string starts with a vowel (aeiou), "ay" is tacked onto the end.
#  (2) If the string starts with one or several consonants, 
# they are moved to the end and "ay" is tacked on after them.
#  (3) "qu" is a special case, as both of them get moved to the end of the word, 
# as if they were one consonant letter.
# Create a function called pig_latin. 
# It takes an English string or sentence and converts it to Pig Latin,
#  returning the result. We will assume that there is no punctuation 
# and that everything is lower case.


def pig_latin_one_word(input):
    vowels = ["a","i","e","o","u"]
    special = ["q"]
    result=[]
    position=None

    for i, letter in enumerate(input):
        if letter in special:
            position=i
            position=int(position)+2
            break
    
        elif letter in vowels:
            position=i
            break
        
            
    for j in range(position, len(input)):
        result.append(input[j])
        # print(result)
        # print("Current j equals", j)
    for l in range(0, position):
        result.append(input[l]) 
    result="".join(result)
    result= result +"ay" 
    return result


def pig_latin(sentence_input):
   words = sentence_input.split(" ")
   result=[]
   for i in range (0, len(words)):
        result.append(pig_latin_one_word(words[i]))

   result=" ".join(result)
   #print(result)
   return result


#print(pig_latin("apple"))

            


        


        
















