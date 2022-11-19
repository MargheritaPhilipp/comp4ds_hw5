# Lists

import pandas as pd
import datetime
from geopy import distance

# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

from functools import reduce 

def simba_count(lst):
    result= map(lambda x: x.count("Simba") , lst)
    n_simba = list(result)
    return(reduce(lambda x,y: x+y, n_simba))

# test
simba_test= ["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 


# 7)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

  
def get_day_month_year(list_dt):
    list_day=list(map(lambda x: x.day, list_dt))
    list_month=list(map(lambda x: x.month, list_dt))
    list_year=list(map(lambda x: x.year, list_dt))
    df = pd.DataFrame(list(zip(list_day, list_month, list_year)),
               columns =['day', 'month', 'year'])
    return(df)
    
# test
test_get_month_data= [datetime.datetime.today() - datetime.timedelta(days=x) for x in range(5)]



# 8) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#


def compute_distance(list_tuples):
    def compute_distance_one(one_tuple):
        p1=one_tuple[0]
        p2=one_tuple[1]
        distance_pair=distance.distance(p1, p2)
        return(distance_pair.km)
    
    result=map(compute_distance_one, list_tuples)
    return(list(result))
    
# test
test_compute_distance=[((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]


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
test_sum_general_int_list=[[2], 3, [[1,2],5]]  


