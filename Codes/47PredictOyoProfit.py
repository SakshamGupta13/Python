from sklearn.metrics import r2_score
import matplotlib.pyplot as pit
import numpy as np
from scipy import stats as st

oyoYears = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
oyoProfit = [150, 200, -50, 300, 400, 250, -100, 350, 500, 450] # in Cr

# pit.scatter(oyoYears,oyoProfit,marker='o')
# pit.show()

futureProfit = np.poly1d(np.polyfit(oyoYears,oyoProfit,3))  # polynomial regerssion
print(futureProfit(2025))
print(r2_score(oyoProfit,futureProfit(oyoYears)))

slope,intercept,r,p,std_err = st.linregress(oyoYears,oyoProfit)    # linear regression
print("scope :",slope,", intercept :",intercept,", r :",r,", p :",p,", str_err :",std_err)