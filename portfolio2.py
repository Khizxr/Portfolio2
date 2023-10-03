#!usr/bin/env python 3

name = input ("What is your name")
print ("Hello", name + ".", "Good to meet you")

tempc = input("What is the temperature in celsius")
tempc = float(tempc)
print(tempc," is equivalent to",tempc *1.8)

students = input("How many students are there")
students = int(students)
groupsize = input("Required group size")
groupsize = int(groupsize)
fullg = students // groupsize
remainder = students % groupsize
print ("There will be",fullg, "groups with", remainder, "students left over")

sweets = input("How many sweets are there")
sweets = int(sweets)
pupils = input("How many puipils are there?")
pupils = int(pupils)
total = sweets // pupils
leftovr = sweets % pupils
print ("Each pupil needs",total,"sweets and there will be",leftovr,"sweets leftover")