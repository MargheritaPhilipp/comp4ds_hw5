import unittest

from hw5_library.hw5_functions import lists

# not sure if this is needed?
import pandas as pd
import datetime
from geopy import distance
from functools import reduce 

#import os
#os. chdir("/Users/MargheritaP/Documents/GitHub/comp4ds_hw5")
#pwd()

class TestSimba_Count(unittest.TestCase):
    
    def test_simba_count_1(self):
        list_input = ["Simba and Nala are lions.", "Nala likes Simba"]
        expected_output = 2
        output = lists.simba_count(list_input)
        self.assertEqual(expected_output, output)
        
    def test_simba_count_2(self):
        list_input = ["I laugh in the face of danger, simba."]
        expected_output = 0
        output = lists.simba_count(list_input)
        self.assertEqual(expected_output, output)
        
    def test_simba_count_3(self):
        list_input = ["Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
        expected_output = 2
        output = lists.simba_count(list_input)
        self.assertEqual(expected_output, output)


from pandas.testing import assert_frame_equal

class TestGet_Day_Month_Year(unittest.TestCase):
    
    def test_get_day_month_year_1(self):
        date_input = [datetime.datetime(2009, 1, 14, 19, 12, 21), datetime.datetime(2, 6, 30, 1, 32, 37, 286836)]
        output_data = {'day': [14,30], 'month': [1,6], 'year': [2009,2]}
        expected_output =  pd.DataFrame(data_output)
        output = lists.get_day_month_year(date_input)
        assert_frame_equal(expected_output, output, check_dtype=False) #should be more suitable than self.assertEqual

## note to maybe edit original function:
        # induce ValueError: month must be in 1..12
        # induce ValueError: year -50 is out of range


class TestCompute_Distance(unittest.TestCase):
    
    def test_compute_distance_1(self):
        coord_input = [((-5,1), (-5, 1)), ((52.38, 20.1),(52.3, 17.8))]
        expected_output= [0.0, 157.00582786889402]                      
        output = lists.compute_distance(coord_input)
        self.assertEqual(expected_output, output)

## note to maybe edit original function:
        # induce ValueError: Latitude (first value) must be in the [-90; 90] range.
        # note: longitude technically should be between -180 and 180, but python doesn't throw and error
        # it seems to just stop at a maximum distance (doesn't seem to quite treat the values as 180...)
        
        # induce: ValueError: A single number has been passed to the Point constructor. This is probably a mistake, because constructing a Point with just a latitude seems senseless. If this is exactly what was meant, then pass the zero longitude explicitly to get rid of this error.
        # this seems to be raised under three circumstances:
            # 1) a missing tuple 
            # 2) not wrapping the tuple pair into square brackets:  ((1,1), (1, 1)) instead of [((1,1), (1, 1))]
            # 3) not "pairing" the tuple: [(1,1), (1, 1)] instead of [((1,1), (1, 1))]
            

class TestSum_General_Int_List(unittest.TestCase):

    def test_sum_general_int_list_1(self):
        list_input = [[2], 3, [[1,2],5]]
        expected_output= 13                      
        output = lists.sum_general_int(list_input)
        self.assertEqual(expected_output, output)

    def test_sum_general_int_list_2(self):
        list_input = [[-1, [[-1, -1]],[[-1,-1],[-1,-1]]]]  
        expected_output= -7                  
        output = lists.sum_general_int(list_input)
        self.assertEqual(expected_output, output)


## note to maybe edit original function:
        # induce TypeError: list indices must be integers or slices, not tuple
        #  e.g. from list_2=[[-1,-1][-1,-1]]


