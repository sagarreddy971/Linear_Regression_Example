from readfile import *
reg=linear_model.LinearRegression()
reg.fit(a[["Area"]],a.Price)
print("The predicted value is",reg.predict([[int(input("Enter the area:"))]]))
print("The coeffecient is",reg.coef_)
print("Intercept c is:",reg.intercept_)



from readfile2 import *
f=reg.predict(d)
d["Prices"]=f
print(d)
d.to_excel("new_predicted.xlsx",index=False)
plt.scatter(a.Area,a.Price,marker="*",color="red")
plt.plot(a.Area,reg.predict(a[["Area"]]),color='blue')
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Linear_Regression")
plt.show()