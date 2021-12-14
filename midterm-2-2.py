# Author: JD 12/14/2021

initial = int(input("Enter the initial velocity: "))

final = int(input("Enter the final velocity: "))

time = int(input("Enter the time: "))

accel = (final - initial) / time

print("The acceleration is {0} m/s**2".format(accel))