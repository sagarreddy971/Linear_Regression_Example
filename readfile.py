import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
a=pd.read_excel("C:\\Users\\DELL\\OneDrive\\Desktop\\PP_Projects\\data\\new_data.xlsx")
print(a)



plt.scatter(a.Area,a.Price,marker="*",color="red")
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Linear_Regression")
plt.show()