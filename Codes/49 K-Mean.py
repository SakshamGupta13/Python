import matplotlib.pyplot as pit
from sklearn.cluster import KMeans

age = [60,30,40,30,20]
salary = [15000,20000,25000,30000,32000]

# pit.scatter(age,salary,marker='o')
# pit.show()

data = list(zip(age,salary))
blank_array = []

for mydata in range(1,6):
    kmeans = KMeans(n_clusters=mydata)
    kmeans.fit(data)
    blank_array.append(kmeans.inertia_)
    
pit.plot(range(1,6),blank_array,marker='o')
pit.show()