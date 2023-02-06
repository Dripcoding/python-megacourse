from helpers import get_water_state

# Create a function that finds out the state of water (i.e., gas, liquid, solid) given the temperature. 
# In other words, the function has a temperature parameter and returns either "Gas", "Liquid" or "Solid" as a string depending on the temperature. 
# The function should be written in a separate file from the command line interface file. The output should look like in the screenshot below:

temperature = int(input('Enter water temperature: '))

print(get_water_state(temperature))