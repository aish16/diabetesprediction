#!C:/Users/Aishwarya/Anaconda3/python.exe
import sqlite3
import cgi,cgitb
from decimal import *
form=cgi.FieldStorage()
name=form.getvalue('name')
pregnant=form.getvalue('pregnant')
plasma=form.getvalue('plasma')
bp=form.getvalue('bp')
triceps=form.getvalue('triceps')
insulin=form.getvalue('insulin')
bmi=form.getvalue('bmi')
pedigree=form.getvalue('pedigree')
age=form.getvalue('age')
print ("Location:http://localhost:81/p5.html\r\n")
print ("Content-type: text/html\r\n\r\n")
print ("<html><body></body></html>")
conn=sqlite3.connect('itt.db')
#conn.execute("create table project(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name text, NumPregnant int, Glucose REAL, BloodPressure REAL, TSF REAL, SerumInsulin REAL, BMI REAL, PedigreeFunc REAL,AGE INTEGER);")
conn.execute("INSERT INTO project(name,NumPregnant,Glucose,BloodPressure,TSF,SerumInsulin,BMI,PedigreeFunc,AGE)VALUES(?,?,?,?,?,?,?,?,?);",(name,pregnant,plasma,bp,triceps,insulin,bmi,pedigree,age))
conn.commit();
conn.close();