# Planetary surface gravity relative to Earth (Earth = 100)
gravity_factors = {
    "Mercury": 37.6,
    "Venus": 88.9,
    "Mars": 37.8,
    "Jupiter": 236.0,
    "Saturn": 108.1,
    "Uranus": 81.5,
    "Neptune": 114.0
}

def calculate_planet_weight():
    print("Planetary Weight Calculator")
    print("Available planets:", ", ".join(gravity_factors.keys()))
    
    try:
        # Get user input
        earth_weight = float(input("Enter your weight on Earth: "))
        planet = input("Enter a planet: ").capitalize()
        
        # Check if planet is valid
        if planet not in gravity_factors:
            print(f"Error: '{planet}' is not a valid planet in our system.")
            return
        
        # Calculate weight on other planet
        planet_gravity = gravity_factors[planet]
        calculated_weight = (earth_weight * planet_gravity) / 100
        rounded_weight = round(calculated_weight, 2)
        
        print(f"Your weight on {planet} would be: {rounded_weight}")
    
    except ValueError:
        print("Error: Please enter a valid number for your weight.")

# Start the program
calculate_planet_weight()