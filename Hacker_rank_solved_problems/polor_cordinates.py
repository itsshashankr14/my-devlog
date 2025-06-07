# Given a complex number, convert it to polar coordinates.
# Output the modulus and phase angle (in radians), each rounded to 3 decimal places.
import cmath
z = complex(input())
modulus = abs(z)
phase_angle = cmath.phase(z)
print("{0:.3f}".format(modulus))
print("{0:.3f}".format(phase_angle))
