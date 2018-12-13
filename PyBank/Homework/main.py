# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 21:33:50 2018

@author: jawhite
"""

# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..","Resources","budget_data.csv")
file_to_output = os.path.join("..","Output", "Output.txt")



# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Name the variables
    #total number of months
    month=0
    #net profit/loss
    netpl=0
    #average profit/loss
    avgpl=0
    #maximum increase
    maxincrease=0
    #maximum increase month
    maximonth=""
    #maximum decrease
    maxdecrease=0
    #maximum decrease month
    maxdmonth=""
    
    
    #Output stuffffff
    print("Financial Analysis")
# Loop through the file
    for row in csvreader:
        #skip the first row for headers
        if row[0]=="Date":
            next
        else:
            #increment the number of months
            month+=1
            
            #increment the net profit or loss
            netpl=netpl+float(row[1])
            
            #test to see if this is greater than the max, if so reassign the max
            if float(row[1])>maxincrease:
                maximonth=row[0]
                maxincrease=float(row[1])
            #test to see if this is less than the min, if so reassign the min
            if float(row[1])<maxdecrease:
                maxdmonth=row[0]
                maxdecrease=float(row[1])
    #output everything
    print("----------------------------")
    print("Total Months: "+ str(month))
    print("Total: $"+"{:.0f}".format(netpl))
    print("Average Change: $" +"{:.2f}".format(netpl/month))
    print("Greatest Increase in Profits: "+str(maximonth)+" ($"+"{:.0f}".format(maxincrease)+")")
    print("Greatest Decrease in Profits: "+str(maxdmonth)+" ($"+"{:.0f}".format(maxdecrease)+")")
    
    #write to the output text file

# logic and code

# do stuff, stuff, and more stuff

# prepare your final output data frame

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write("Total Months: "+ str(month)+"\n")
    txt_file.write("Total: $"+"{:.0f}".format(netpl)+"\n")
    txt_file.write("Average Change: $" +"{:.2f}".format(netpl/month)+"\n")
    txt_file.write("Greatest Increase in Profits: "+str(maximonth)+" ($"+"{:.0f}".format(maxincrease)+")"+"\n")
    txt_file.write("Greatest Decrease in Profits: "+str(maxdmonth)+" ($"+"{:.0f}".format(maxdecrease)+")"+"\n")

    