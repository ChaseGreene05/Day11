import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.plot(x, y, color = "red", marker = "x")
plt.xlabel("Time (m)")
plt.ylabel("Speed (m/s)")
plt.title("Graph Title")
plt.show()
