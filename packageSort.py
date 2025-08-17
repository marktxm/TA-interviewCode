def sort(width, height, length, mass):
    # Determine if the package is bulky
    volume = width * height * length
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150

    # Determine if the package is heavy
    heavy = mass >= 20

    # Dispatch based on package characteristics
    return "REJECTED" if bulky and heavy else ("SPECIAL" if bulky or heavy else "STANDARD")


# Example test cases
if __name__ == "__main__":
    print(sort(100, 100, 100, 10))    # STANDARD
    print(sort(200, 50, 50, 10))      # SPECIAL (bulky)
    print(sort(50, 50, 50, 25))       # SPECIAL (heavy)
    print(sort(200, 200, 200, 30))    # REJECTED (bulky + heavy)
