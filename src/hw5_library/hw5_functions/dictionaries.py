# Dictionaries


# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl


## EAFP


def retrieve_age_eafp2(dictionary: dict):
    try:
        return (2022 - dictionary['birth'])
    except KeyError:
        return("There is no key called birth in this dictionary")
    except Exception:
        return("The value under birth is not a float or an integer")


# LBYL


def retrieve_age_lbyl(dictionary: dict):
    if 'birth' in dictionary.keys():
        True
        if isinstance(dictionary['birth'],(float, int)):
            return(2022 - dictionary['birth'])
        else:
            return("The value under birth is not a float or an integer")
    else:
        return("There is no key called birth in this dictionary")




