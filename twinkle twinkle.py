#Write a Python program to print the following string in a specific format

a = ("Twinkle, twinkle, little star,")
b = ("How I wonder what you are!")
c = ("Up above the world so high,")
d = ("Like a diamond in the sky.")
e = ("Twinkle, twinkle, little star,")
f = ("How I wonder what you are")


print(str(a) + '\n' + " " + " " + str(b) + '\n' + " " + " " + " " + str(c) + '\n'
      + " " + " " + " " + str(d) + '\n' + str(e) + '\n' + " " + " " + str(f) )


#Write a Python program to display the current date and time.
import datetime
A = datetime.datetime.now()
print(A)



#Write a Python program which accepts the radius of a circle from the user and compute the area.
import math

b = float(math.pi)
a = int(input("Enter the radius of the circle here in meters:"))
area = b * a * a
print("The area of the circle of radius" + str(a) + " " + "is" + " " + str(area) + "m")



#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
a = input("First Name:")
b = input("Last Name:")
print(str(b) + " " + str(a))
