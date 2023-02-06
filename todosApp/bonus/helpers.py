FREEZING_POINT, BOILING_POINT = 0, 100

def get_water_state(temperature):
    if 0 < temperature < 100:
        return 'Liquid'
    elif temperature <= freezing_point:
        return 'Solid'
    elif temperature >= boiling_point:
        return 'Gas'