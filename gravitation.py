# Calculate the gravitational force between the earth and the moon

name = input('What is your name?')
G = 6.67 * (10 ** -11)  # Gravitational constant
r = 3.84 * (10 ** 8)  # distance between the Earth and Moon

# Default values for M and m
M_default = 6.0 * (10 ** 24)  # Mass of Earth
m_default = 7.34 * (10 ** 22)  # Mass of the moon

# Prompt the user for the values of M and m
M_input = input(f"Enter the mass of Earth (in kg, scientific notation allowed) [default: {M_default}]: ")
m_input = input(f"Enter the mass of the moon (in kg, scientific notation allowed) [default: {m_default}]: ")

# Use default values if the user input is empty
M = float(M_input) if M_input else M_default
m = float(m_input) if m_input else m_default

def gravitational_Force(M, m):
    return G * M * m / r ** 2

print(f"The gravitational force between Earth and the moon is {gravitational_Force(M, m)} N, {name}")
