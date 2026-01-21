# importare module din pachetul geometry
from geometry import circle
from geometry import rectangle

print("--- Calcule Geometrice ---")

# cerc
raza = 5
aria_c = circle.circle_area(raza)
circ_c = circle.circle_circumference(raza)

print(f"Cerc (raza {raza}):")
print(f" Aria: {round(aria_c, 2)}")
print(f" Circumferinta: {round(circ_c, 2)}")

# dreptunghi
lungime = 10
latime = 4
aria_d = rectangle.rectangle_area(lungime, latime)
peri_d = rectangle.rectangle_perimeter(lungime, latime)

print(f"Dreptunghi ({lungime} x {latime}):")
print(f" Aria: {aria_d}")
print(f" Perimetrul: {peri_d}")