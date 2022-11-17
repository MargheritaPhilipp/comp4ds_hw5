# prep for question 6 on data analysis

import os
import pandas as pd

#os.chdir('/Users/MargheritaP/Documents/GitHub/comp4ds_hw5')
os.getcwd()

df = pd.read_csv(os.path.realpath("sample_diabetes_mellitus_data.csv"))

df.head()


# prep for library creation



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

#test function:
car_at_light("silver")

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

#test function
print(safe_subtract(-9.44,5))
print(safe_subtract("six",5))
print(safe_subtract(a,5))

# with Look Before You Leap: LBYL
def safe_subtract_old(n1, n2):
    if isinstance(n1, (float, int, complex)) and isinstance(n2, (float, int, complex)):
        print(n1-n2)
    elif isinstance(n1, str) or isinstance(n2, str):
        print("Strings cannot be subtracted - please enter a number.")
    else:
        print("There is an issue with your input - maybe you entered an undefined variable.")

#test function       
safe_subtract_old(8,complex(7))     


# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl


## EAFP

dic1= {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
dic2= {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
dic3= {'name': 'Janet', 'last_name': 'Bird', 'birth': '1984'}


def retrieve_age_eafp1(dictionary: dict):
    try:
        return(2022 - dictionary.get('birth'))
    except:
        print("This dictionary does not have a birth date to retrieve age from") # Might this be what the question is asking for??

retrieve_age_eafp1(dic2)

#check out different errors:
dic1.get('birth')
dic1['birth']
dic2.get('birth')
dic2['birth']


# possibly better as the calling with square brackets results in key error
def retrieve_age_eafp2(dictionary: dict):
    try:
        return print(2022 - dictionary['birth'])
    except KeyError:
        print("There is no key called birth in this dictionary")
    except Exception as error:
        print("Something went wrong - maybe check the value(s) under birth in your dictionary")
        
retrieve_age_eafp2(dic1)
retrieve_age_eafp2(dic2)
retrieve_age_eafp2(dic3)

## LBYL

dic1.keys()

def retrieve_age_lbyl(dictionary: dict):
    if 'birth' in dictionary.keys():
        True
        if isinstance(dictionary['birth'],(float, int)):
            print(2022 - dictionary['birth'])
        else:
            print("The value under birth is not a float or an integer")
    else:
        print("There is no key called birth in this dictionary")

retrieve_age_lbyl(dic1)      
retrieve_age_lbyl(dic2)
retrieve_age_lbyl(dic3)

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#

def read_data(testf: str):
    try:
        df1 = pd.read_csv(testf)
        print("your file has been imported as df1")
        df1.head()
    except FileNotFoundError: 
        return "The file " +str(testf)+ " is not in the directory you have specified."

#check 
test1 = "sample_diabetes_mellitus_data.csv"
test2 = "data.csv"

read_data(test1)
read_data(test2)

# remnants of old attempts
#if os.path.exists(testf) == True:
#df1 = pd.read_csv((f'l{file_path}l'))
#return df1.head()
#k = pd.read_csv('/Users/MargheritaP/Documents/GitHub/comp4ds_hw5/sample_diabetes_mellitus_data.csv')        
#k.head()        


# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += elem

# comments on a:
total_double_sum
# returns 17, and indeed only the elements have been summed
# presumably we want to double each element and find total, so 20+10+4=34
# correction:
total_double_sum2 = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum2 += double
total_double_sum2

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = string+"_"+string

# comments on b:
strings
#returns 'Groot_Groot'
#presumably the desired output is "I_am_Groot"?
# correction:
strings2 = ''
for string in ['I', 'am', 'Groot']:
    strings2 += string+"_"
strings2


### (c) Careful!
j=10
while j > 0:
   j += 1

# comments on c: not tried to run, but this would keep running as j is always > 0
# correction such that it stops:

k=10
while k < 20:
   k += 1        #equivalent:  k = k+1
k

### (d)
productory = 0
for elem in [1, 5, 25]:
    productory *= elem

# comments on d:
productory
# returns 0 - presumably because it is first multiplying by productory, so 0
# presumably what we want it a product of all numbers in the list: 1*5*25=125
# correction:
productory2 = 1
for elem in [1, 5, 25]:
    productory2 *= elem
productory2


################################################
##### Try to use map and reduce in the next 3 exercises
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#


list_strings= ["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 



# 7)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

# Without map or reduce:

import pandas as pd
import datetime


def get_day_month_year_simple(list_dt):
    df = pd.DataFrame(example, columns = ['date_full'])
    # Get day
    df['day'] = pd.DatetimeIndex(df['date_full']).year
    # Get month
    df['month'] = pd.DatetimeIndex(df['date_full']).month
    # Get year
    df['year'] = pd.DatetimeIndex(df['date_full']).day
    
    df.drop(['date_full'], axis=1, inplace=True) 
    
    return(df)

# test
example = [datetime.datetime.today() - datetime.timedelta(days=x) for x in range(5)]

get_day_month_year_simple(example)    
    
# Testing map or reduce

import pandas as pd
import datetime


def get_day_month_year(list_dt):
    list_day=list(map(lambda x: x.day, list_dt))
    list_month=list(map(lambda x: x.month, list_dt))
    list_year=list(map(lambda x: x.year, list_dt))
    df = pd.DataFrame(list(zip(list_day, list_month, list_year)),
               columns =['day', 'month', 'year'])
    return(df)
    
# test
example = [datetime.datetime.today() - datetime.timedelta(days=x) for x in range(5)]
get_day_month_year(example)



# 8) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

from geopy import distance

def compute_distance(list_tuples):
    def compute_distance_one(one_tuple):
        p1=one_tuple[0]
        p2=one_tuple[1]
        distance_pair=distance.distance(p1, p2)
        return(distance_pair.km)
    
    result=map(compute_distance_one, list_tuples)
    return(list(result))
    
# test
input_example=[((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]

compute_distance(input_example)

#################################################
# 9)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#


def sum_general_int_list(l):
    total=0
    for j in range(len(l)):
        if type(l[j])==list:
            total += sum_general_int_list(l[j])
        else:
            total += l[j]
    return(total)
 
# test
list_1=[[2], 3, [[1,2],5]]  
print(sum_general_int_list(list_1))  

