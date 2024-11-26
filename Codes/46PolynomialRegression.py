from sklearn.metrics import r2_score
import matplotlib.pyplot as pit
import numpy as np
from scipy import stats as st

age = [40,20,35,50,60,30,70,80]
salary = [20000,40000,18000,15000,12000,25000,35000,50000]

# pit.scatter(age,salary,marker='o')
# pit.show()

futureSalary = np.poly1d(np.polyfit(age,salary,3))
print(futureSalary(55))
print(r2_score(salary,futureSalary(age)))