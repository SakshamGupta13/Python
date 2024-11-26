import matplotlib.pyplot as pit
from scipy import stats as st
from sklearn.metrics import r2_score
import numpy as np

age = [20,25,45,30,50,40]
salary = [20000,25000,45000,30000,50000,40000]

# futureData = np.poly1d(np.polyfit(age,salary,30))
# print(r2_score,salary,futureData(35))

# slope,intercept,r,p,std_err = st.linregress(age,salary)
# print("scope :",slope,", intercept :",intercept,", r :",r,", p :",p,", str_err :",std_err)

# if r is near to 1 --> best case
# if r is near to 0 --> worst case

# def futureSalary(age):
#     return slope * age + intercept

# print("Salary :",futureSalary(35))


# pit.scatter(age,salary)
# pit.show()

# pit.plot(age,salary,marker='o')
# pit.title('Salary-Age Wise Graph')
# pit.xlabel('Age')
# pit.ylabel('Salary')
# pit.show()