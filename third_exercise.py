import matplotlib.pyplot as plot # Exercise 3

###############
# Exercise #1 #
###############
def function(x, y= None):
    if y is None:
        y = []

    y.append(x)
    return y

print(function(1))
print(function(2))
print(function(3))

###############
# Exercise #2 #
###############
with open('test.txt', 'w') as file:
    file.write("I love chocolate very much".replace(' ', '\n'))

###############
# Exercise #3 #
###############
xCoordinates = [-2, 2]
yCoordinates = [x * x for x in xCoordinates]

plot.plot(xCoordinates, yCoordinates).show()