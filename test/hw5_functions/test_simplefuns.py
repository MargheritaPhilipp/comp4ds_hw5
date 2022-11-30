import unittest
import pandas as pd
from hw5_library.hw5_functions import simplefuns



class TestCar_at_light(unittest.TestCase):
    def test_car_at_light_1(self):
        expected_output=print("stop")
        output=simplefuns.car_at_light("red")
        assert output==expected_output
        
    def test_car_at_light_2(self):
        expected_output=print("go")
        output=simplefuns.car_at_light("green")
        self.assertEqual(expected_output, output)
        
    def test_car_at_light_3(self):
        expected_output=print("wait")
        output=simplefuns.car_at_light("yellow")
        self.assertEqual(expected_output, output)
        
    def test_car_at_light_4(self):
        expected_output=print("Undefined instruction for color: purple")
        output=simplefuns.car_at_light("purple")
        self.assertEqual(expected_output, output)
        

        
class TestSafe_subtract(unittest.TestCase):
    
    def test_safe_subtract_1(self):
        expected_output=3
        output=simplefuns.safe_subtract(5, 2)
        self.assertEqual(expected_output, output)
        
    def test_safe_subtract_2(self):
        output=simplefuns.safe_subtract(5, "2")
        self.assertIsNone(output)
        
    def test_safe_subtract_3(self):
        with self.assertRaises(Exception) as context:
            simplefuns.safe_subtract(5, a)
        self.assertTrue(Exception in context.exception)
        # This isn't working

class TestRead_Data(unittest.TestCase):)

    def test_read_data_1(self):
        
    
    def test_read_data_2(self):
        with self.assertRaises(FileNotFoundError) as context:
            simplefuns.safe_subtract(5, a)
        self.assertTrue(FileNotFoundError in context.exception) #should replace exception with filenotfound?
        
### remove at the end            
def read_data(testf: str):
    try:
        df1 = pd.read_csv(testf)
        print("your file has been imported as df1")
        df1.head()
        read_data.df = pd.read_csv(testf)
        print("Your file can now be called as read_data.df here are the headings:")
        print( read_data.df.head())
    except FileNotFoundError: 
        return "The file " +str(testf)+ " is not in the directory you have specified." 
        
  