import matplotlib.pyplot as plt
import datetime

# x-axis values
x = [1, 3, 5, 6]

# y-axis values  --! dimension must be same
y = [3, 5, 12, 4]

# let's plot them
#
# plt.plot(x, y)
#
# plt.show()

year = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
my_iq = [10, 15, 23, 30, 35, 35, 50, 60, 70, 70, 80]
plt.plot_date(year, my_iq)

plt.show()
