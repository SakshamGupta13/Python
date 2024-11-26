from sklearn.metrics import r2_score
import matplotlib.pyplot as pit
import numpy as np
from scipy import stats as st

amazonYears = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
amazonProfit= [2300, 3200, 4100, 5000, 6700, 8200, 10500, 12400, 14800, 17600]  # in millions

# pit.scatter(amazonYears,amazonProfit,marker='o')
# pit.show()

futureProfit = np.poly1d(np.polyfit(amazonYears,amazonProfit,3))  # polynomial regerssion
print(futureProfit(2025))
print(r2_score(amazonProfit,futureProfit(amazonYears)))

slope,intercept,r,p,std_err = st.linregress(amazonYears,amazonProfit)    # linear regression
print("scope :",slope,", intercept :",intercept,", r :",r,", p :",p,", str_err :",std_err)