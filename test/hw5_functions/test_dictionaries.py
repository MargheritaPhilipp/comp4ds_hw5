import unittest

from hw5_library.hw5_functions import dictionaries

class TestRetrieve_Age_EAFP2(unittest.TestCase):
    
    def test_retrieve_age_eafp2_1(self):
        dic1= {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
        expected_output=35
        output=dictionaries.retrieve_age_eafp2(dic1)
        assert output==expected_output
        
    def test_retrieve_age_eafp2_2(self):
        dic2= {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
        expected_output='There is no key called birth in this dictionary'
        output=dictionaries.retrieve_age_eafp2(dic2)
        self.assertEqual(expected_output, output)
        
    def test_retrieve_age_eafp2_3(self):
        dic3= {'name': 'Janet', 'last_name': 'Bird', 'birth': '1984'}
        expected_output='The value under birth is not a float or an integer'
        output=dictionaries.retrieve_age_eafp2(dic3)
        self.assertEqual(expected_output, output)
    
class TestRetrieve_Age_LBYL(unittest.TestCase):
    
    def test_retrieve_age_lbyl_1(self):
        dic1= {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
        expected_output=35
        output=dictionaries.retrieve_age_lbyl(dic1)
        assert output==expected_output
            
    def test_retrieve_age_lbyl_2(self):
        dic2= {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
        expected_output='There is no key called birth in this dictionary'
        output=dictionaries.retrieve_age_lbyl(dic2)
        self.assertEqual(expected_output, output)
            
    def test_retrieve_age_lbyl_3(self):
        dic3= {'name': 'Janet', 'last_name': 'Bird', 'birth': '1984'}
        expected_output='The value under birth is not a float or an integer'
        output=dictionaries.retrieve_age_lbyl(dic3)
        self.assertEqual(expected_output, output)
        
        
        
        
    