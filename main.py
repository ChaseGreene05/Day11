import matplotlib.pyplot as plt


x = [1,2,3,4,5]
y = [math.sin(1),math.sin(2),math.sin(3),math.sin(4),math.sin(5)]


plt.plot(x, y, color = "red", marker = "x")
plt.title("The sum of 1 to 5")
plt.show()