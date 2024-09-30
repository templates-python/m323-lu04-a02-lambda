from math import pi

# Lambda-Funktionen für die Flächenberechnung
circle_area = lambda r: pi * r * r  # Kreisfläche
square_area = lambda s: s * s  # Quadratfläche
rectangle_area = lambda l, w: l * w  # Rechteckfläche

if __name__ == '__main__':
    print(circle_area(5))
    print(square_area(4))
    print(rectangle_area(3, 5))
