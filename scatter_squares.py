import matplotlib.pyplot as plt

x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values, y_values, edgecolor="none", c=y_values, cmap=plt.cm.Blues, s=40)

#设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which="major", labelsize=14)

plt.axis([0, 1100, 1, 1100000])

plt.show()
plt.savefig("squares_plot.png", bbox_inches="tight")
