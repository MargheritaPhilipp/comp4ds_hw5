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

    
        
  