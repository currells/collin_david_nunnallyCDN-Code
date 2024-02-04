"""
Name: Collin Nunnally
Class: CSE-111
Comments:

"""
def water_column_height(tower_height, tank_height):
    # h = t + 3w / 4
    water_column_height = (tower_height + ((3 * tank_height) / 4))
    return water_column_height
def pressure_gain_from_water_height(height):
    # P = ρgh / 1000
    pressure_gain_from_water_height = ((998.2 * 9.80665 * height) / 1000)
    return pressure_gain_from_water_height
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    # P = -f * L * p * v^2 / 2000 * d
    pressure_loss_from_pipe = ((-friction_factor * pipe_length * 998.2) * (fluid_velocity ** 2) / (2000 * pipe_diameter))
    return pressure_loss_from_pipe
