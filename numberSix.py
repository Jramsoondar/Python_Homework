"""Write and test a program that computes the area of a circle. This program should 
request a number representing a radius as input from the user. It should use the formula 
3.14 * radius ** 2 to compute the area and then output this result suitably labeled."""
Pi = 3.14
radius = int(input('What is the radius'))
area = 2 * Pi * radius
print('The area of the circle is ', area , 'square units')