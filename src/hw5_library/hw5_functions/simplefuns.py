# Simple functions

import pandas as pd

# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

def car_at_light(light:str) -> str: 
    if light == "red": 
        print("stop")
    elif light == "green":
        print("go")
    elif light == "yellow":
        print("wait")
    else :
        print("Undefined instruction for color: " + str(light))

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

# with Easier to Ask for Forgiveness than Permission (EAFP) 
   
def safe_subtract(n1, n2):
    try:
        return n1-n2
    except TypeError: 
        return None
    except Exception as error:
        print(str(error))
        
        
# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#


def read_data(testf: str):
    try:
        read_data.df = pd.read_csv(testf)
        t = "Your file can now be called as read_data.df here are the headings:"
        return t, read_data.df.head()
       #print( read_data.df.head())
    except FileNotFoundError: 
        return "The file is not in the directory you have specified."
    
