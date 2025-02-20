def convert_to_miles(kilometers):
    """Converts kilometers to miles using the formula: miles = kilometers * 0.6214"""
    return kilometers * 0.6214


km = float(input("Enter distance in kilometers: "))


miles = convert_to_miles(km)


print(f"{km} kilometers is equal to {miles:.2f} miles.")