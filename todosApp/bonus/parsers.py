def parse(feet_inches):
    values = feet_inches.split(" ") 
    feet, inches = float(values[0]), float(values[1])
    return { 'feet': feet, 'inches': inches }