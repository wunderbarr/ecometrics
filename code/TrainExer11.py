import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('TrainExer11.xls')
print (data.head())

# (a) the histogram & scatter plot of the data
n, bins, patches = plt.hist(data['Age'], 10, density=True, facecolor='g', alpha=0.75)
plt.xlabel('Age')
plt.ylabel('Probability')
plt.title('Histogram of Age')
plt.xlim(10, 60)
plt.ylim(0, 0.05)
plt.grid(True)
plt.show()

n, bins, patches = plt.hist(data['Expenditures'], 4, density=True, facecolor='y', alpha=0.75)
plt.xlabel('Age')
plt.ylabel('Probability')
plt.title('Histogram of Expenditures')
plt.xlim(85, 110)
plt.ylim(0, 0.1)
plt.grid(True)
plt.show()


plt.scatter(data['Age'], data['Expenditures'], alpha=0.5)
plt.show()

# (b) the trend is not monotonic

# (c) split user group and explore again

# (d) sample mean of Expenditures
print (data['Expenditures'].mean())

# (e) sample means of Expenditures for two groups
print (data[data['Age']<40]['Expenditures'].mean())
print (data[data['Age']>=40]['Expenditures'].mean())

# (f) predict expenditure for a 50 / 25 customer
print ('25', data[data['Age']<40]['Expenditures'].mean())
print ('50', data[data['Age']>=40]['Expenditures'].mean())