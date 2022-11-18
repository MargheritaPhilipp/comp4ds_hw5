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

