# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 21:33:50 2018

@author: jawhite
"""

# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..","Resources","election_data.csv")
file_to_output = os.path.join("..","Output", "Output.txt")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Naming the variables!!
    #number of total votes
    totalvotes=0
    
    #list of candidates
    candidate_list=[]
    
    #number of votes for each candidate
    candidate_votes=[]
    
    for row in csvreader:
        #skip the first row for headers
        if row[0]=="Voter ID":
            next
        else:
            #increment the total number of votes
            totalvotes+=1
            #if the candidate has not been voted on before
            if row[2] not in candidate_list:
                #add to candidate list
                candidate_list.append(row[2])
                #add candidate counter to the list
                candidate_votes.append(1)
            if row[2] in candidate_list:
                #increment counter to add
                candidate_votes[candidate_list.index(row[2])]=candidate_votes[candidate_list.index(row[2])]+1
    
    #figure out which candidate had the most votes through the lists
    maxm=str(candidate_list[candidate_votes.index(max(candidate_votes))])
    print("Election Results")
    print("-------------------------")           
    print("Total Votes: "+str(totalvotes))
    print("-------------------------")
    
    #printing the candidates with all of their vote counts and percentages
    for i in range(len(candidate_list)):
        print(candidate_list[i]+": "+"{0:.3%}".format((candidate_votes[i]-1)/totalvotes)+" ("+str(candidate_votes[i]-1)+")")
    print("-------------------------")
    print("Winner: "+maxm)
    print("-------------------------")
    
with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results"+"\n")
    txt_file.write("-------------------------"+"\n")           
    txt_file.write("Total Votes: "+str(totalvotes)+"\n")
    txt_file.write("-------------------------"+"\n")
    
    #printing the candidates with all of their vote counts and percentages
    for i in range(len(candidate_list)):
        txt_file.write(candidate_list[i]+": "+"{0:.3%}".format((candidate_votes[i]-1)/totalvotes)+" ("+str(candidate_votes[i]-1)+")"+"\n")
    txt_file.write("-------------------------"+"\n")
    txt_file.write("Winner: "+maxm+"\n")
    txt_file.write("-------------------------"+"\n")