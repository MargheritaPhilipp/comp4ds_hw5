import unittest
import pandas as pd
from hw5_library.hw5_functions import simplefuns
from pandas.testing import assert_frame_equal



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
            with self.assertRaises(NameError):
                output=simplefuns.safe_subtract(5, a)

class TestRead_Data(unittest.TestCase):

    def test_read_data_1(self):
        url="https://raw.githubusercontent.com/MargheritaPhilipp/comp4ds_hw5/main/hw5_files/sample_diabetes_mellitus_data.csv"
        data= pd.read_csv(url)
        expected_output_1="Your file can now be called as read_data.df here are the headings:"
        expected_output_2=data.head()
        output1, output2=simplefuns.read_data(url)
        assert_frame_equal(expected_output_2, output2, check_dtype=False)
        self.assertEqual(expected_output_1, output1)
        
    
    def test_read_data_2(self):
        expected_output="The file is not in the directory you have specified."
        output=simplefuns.read_data("random_data")
        self.assertEqual(expected_output, output)        
  