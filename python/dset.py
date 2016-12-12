import csv as csv 
import numpy as np
import scipy
from scipy import stats
import sqlite3
import cgi,cgitb
import matplotlib.pyplot as plt
import pylab
from sklearn import datasets, linear_model
import mpld3
#*******************************EXTRACTING DATA FROM CSV FILE *************************

# Open up the csv file in to a Python object
csv_file_object = csv.reader(open('E:\python itt project\data.csv', 'rt')) 
header = next(csv_file_object)  # The next() command just skips the 
                                 # first line which is a header
data=[]                          # Create a variable called 'data'.
for row in csv_file_object:      # Run through each row in the csv file,
    data.append(row)
[data.pop(9) for r in data]         # adding each row to the data variable
data = np.array(data) 	         # Then convert from a list to an array
			         # Be aware that each item is currently

                                # a string in this format
#****************************END OF EXTRACTING DATA FROM CSV FILE ***********************
#print(data)
conn=sqlite3.connect('itt.db') 
cursor=[]

##max=conn.execute("select max(id) from project;")
##cursor=conn.execute("select * from project where id in ( select max(id) from project) ;")
##print(max)
##print(cursor[0])
cursor = conn.execute('SELECT max(id) FROM project')
max_id = cursor.fetchone()[0]
print(max_id)
cur = conn.cursor()
cursor=conn.execute("SELECT NumPregnant,Glucose,BloodPressure,TSF,SerumInsulin,BMI,PedigreeFunc,AGE FROM project where id= "+str(max_id)+";")
val=[]
##cursor=cursor[0:1]
for row in cursor:
        val.append(row[0])
        val.append(row[1])
        val.append(row[2])
        val.append(row[3])
        val.append(row[4])
        val.append(row[5])
        val.append(row[6])
        val.append(row[7])
##cursor=cursor[1:]

print(val)


                                
#*********************DATA FOR MULTIPLE LINEAR REGRESSION *******************************

y= data[2::,8]
y = y.astype(float)
#print(y)

x = data[2:,[0,1,2,3,4,5,6,7]]

x = x.astype(float)
#print(x)

#***********************END OF DATA FOR MULTIPLE LINEAR REGRESSION*********************
#print(x)
#y=b.tolist()
#print(y)
##5

#****************************MULTIPLE LINEAR REGRESSION *******************************
print("MULTIPLE LINEAR REGRESSION")
def reg_m(y, x):
    ones = np.ones(len(x[0]))
    X = sm.add_constant(np.column_stack((x[0], ones)))
    for ele in x[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results

clf = linear_model.LinearRegression()
clf.fit(x, y)
z=[]
z=clf.coef_
p=clf.intercept_
##print(clf.intercept_)
##print(z[0])
mulreg=p+val[0]*z[0] + val[1]*z[1] +val[2]*z[2] +val[3]*z[3]+val[4]*z[4] +val[5]*z[5]+val[6]*z[6] +val[7]*z[7]
print(mulreg)
#**************************END OF MULTIPLE LINEAR REGRESSION **************************


#**************************DATA FOR LINEAR REGRESSION ON FIELD 1*********************
a= data[2::,8]
a = a.astype(float)
#print(a)

b = data[2::,0]
b = b.astype(float)
#print(b)

#**************************END OF DATA FOR LR1*************************************




#***********************LINEAR REGRESSION 1 *************************
print("LINEAR REGRESSION 1")
slope, intercept, r_value, p_value, std_err = stats.linregress(a,b)
##print(slope, intercept, r_value, p_value, std_err)
##print(slope, intercept)
# Calculate some additional outputs
predict_y = intercept + slope * a
p1=intercept+val[0]*slope
print(p1)
# Plotting
pylab.plot(a, b, 'o')
pylab.plot(a, predict_y, 'k-')
plt.ylabel('number of pregnancy')
plt.xlabel('class variable')
plt.title('number of pregnancy V/s class variable')

plt.show()

##fig = plt.figure()
##fig.show()
##html=mpld3.fig_to_html(fig,"E:\p5.html","E:\p5.html",False,'general',None,False)

#********************END OF LINEAR REGRESSION 1 **********************

#****************DATA FOR LINEAR REGRESSION ON FIELD 2***************
a= data[2::,8]
a = a.astype(float)
#print(a)

b = data[2::,1]
b = b.astype(float)
#print(b)

#*****************END OF DATA FOR LR2**************************




#***********************LINEAR REGRESSION 2 *************************
print("LINEAR REGRESSION 2")
slope, intercept, r_value, p_value, std_err = stats.linregress(a,b)
#print(slope, intercept, r_value, p_value, std_err)
#print(slope, intercept)
# Calculate some additional outputs
predict_y = intercept + slope * a
p1=intercept+val[1]*slope
print(p1)
# Plotting
pylab.plot(a, b, 'o')
pylab.plot(a, predict_y, 'k-')
plt.ylabel('Glucose')
plt.xlabel('class variable')
plt.title('Glucose V/s class variable')
pylab.show()
#********************END OF LINEAR REGRESSION 2 **********************

#****************DATA FOR LINEAR REGRESSION ON FIELD 3***************
a= data[2::,8]
a = a.astype(float)
#print(a)

b = data[2::,2]
b = b.astype(float)
#print(b)

#*****************END OF DATA FOR LR3**************************




#***********************LINEAR REGRESSION 3 *************************
print("LINEAR REGRESSION 3")
slope, intercept, r_value, p_value, std_err = stats.linregress(a,b)
#print(slope, intercept, r_value, p_value, std_err)
#print(slope, intercept)
# Calculate some additional outputs
predict_y = intercept + slope * a
p1=intercept+val[2]*slope
print(p1)
# Plotting
pylab.plot(a, b, 'o')
pylab.plot(a, predict_y, 'k-')
plt.ylabel('BloodPressure')
plt.xlabel('class variable')
plt.title('BloodPressure V/s class variable')
pylab.show()


#********************END OF LINEAR REGRESSION 3 **********************

#****************DATA FOR LINEAR REGRESSION ON FIELD 4***************
a= data[2::,8]
a = a.astype(float)
#print(a)

b = data[2::,3]
b = b.astype(float)
#print(b)

#*****************END OF DATA FOR LR4**************************




#***********************LINEAR REGRESSION 4 *************************
print("LINEAR REGRESSION 4")
slope, intercept, r_value, p_value, std_err = stats.linregress(a,b)
#print(slope, intercept, r_value, p_value, std_err)
#print(slope, intercept)
# Calculate some additional outputs
predict_y = intercept + slope * a
p1=intercept+val[3]*slope
print(p1)
# Plotting
pylab.plot(a, b, 'o')
pylab.plot(a, predict_y, 'k-')
plt.ylabel('TSF')
plt.xlabel('class variable')
plt.title('TSF V/s class variable')
pylab.show()
#********************END OF LINEAR REGRESSION 4 **********************

#****************DATA FOR LINEAR REGRESSION ON FIELD 5***************
a= data[2::,8]
a = a.astype(float)
#print(a)

b = data[2::,4]
b = b.astype(float)
#print(b)

#*****************END OF DATA FOR LR5**************************




#***********************LINEAR REGRESSION 5 *************************
print("LINEAR REGRESSION 5")
slope, intercept, r_value, p_value, std_err = stats.linregress(a,b)
#print(slope, intercept, r_value, p_value, std_err)
#print(slope, intercept)
# Calculate some additional outputs
predict_y = intercept + slope * a
p1=intercept+val[4]*slope
print(p1)
# Plotting
pylab.plot(a, b, 'o')
pylab.plot(a, predict_y, 'k-')
plt.ylabel('SerumInsulin')
plt.xlabel('class variable')
plt.title('SerumInsulin V/s class variable')
pylab.show()
#********************END OF LINEAR REGRESSION 5 **********************

#****************DATA FOR LINEAR REGRESSION ON FIELD 6***************
a= data[2::,8]
a = a.astype(float)
#print(a)

b = data[2::,5]
b = b.astype(float)
#print(b)

#*****************END OF DATA FOR LR6**************************




#***********************LINEAR REGRESSION 6 *************************
print("LINEAR REGRESSION 6")
slope, intercept, r_value, p_value, std_err = stats.linregress(a,b)
#print(slope, intercept, r_value, p_value, std_err)
#print(slope, intercept)
# Calculate some additional outputs
predict_y = intercept + slope * a
p1=intercept+val[5]*slope
print(p1)
# Plotting
pylab.plot(a, b, 'o')
pylab.plot(a, predict_y, 'k-')
plt.ylabel('BMI')
plt.xlabel('class variable')
plt.title('BMI V/s class variable')
pylab.show()
#********************END OF LINEAR REGRESSION 6 **********************

#****************DATA FOR LINEAR REGRESSION ON FIELD 7***************
a= data[2::,8]
a = a.astype(float)
#print(a)

b = data[2::,6]
b = b.astype(float)
#print(b)

#*****************END OF DATA FOR LR7**************************




#***********************LINEAR REGRESSION 7 *************************
print("LINEAR REGRESSION 7")
slope, intercept, r_value, p_value, std_err = stats.linregress(a,b)
#print(slope, intercept, r_value, p_value, std_err)
#print(slope, intercept)
# Calculate some additional outputs
predict_y = intercept + slope * a
p1=intercept+val[6]*slope
print(p1)
# Plotting
pylab.plot(a, b, 'o')
pylab.plot(a, predict_y, 'k-')
plt.ylabel('PedigreeFunc')
plt.xlabel('class variable')
plt.title('PedigreeFunc V/s class variable')
pylab.show()

#********************END OF LINEAR REGRESSION 7 **********************

#****************DATA FOR LINEAR REGRESSION ON FIELD 8***************
a= data[2::,8]
a = a.astype(float)
#print(a)

b = data[2::,7]
b = b.astype(float)
#print(b)

#*****************END OF DATA FOR LR8**************************




#***********************LINEAR REGRESSION 8 *************************
print("LINEAR REGRESSION 8")
slope, intercept, r_value, p_value, std_err = stats.linregress(a,b)
#print(slope, intercept, r_value, p_value, std_err)
#print(slope, intercept)
# Calculate some additional outputs
predict_y = intercept + slope * a
p1=intercept+val[7]*slope
print(p1)
# Plotting
pylab.plot(a, b, 'o')
pylab.plot(a, predict_y, 'k-')
plt.ylabel('AGE')
plt.xlabel('class variable')
plt.title('AGE V/s class variable')
pylab.show()
#********************END OF LINEAR REGRESSION 8 **********************

