# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:09:19 2018

@author: Mike

This program is to read and parse text data >> from the: Random_Zips_EIG_info_test.txt (Practicum 2 folder)
See data >> Random_Zips_EIG_info_test.txt >> for input data
"""
import re

text_file = open("C:/Users/Mike/Documents/Practicum 2/Random_Zips_EIG_info_test.txt", "r")
lines = text_file.readlines()

#filename = "C:/Users/Mike/Documents/Practicum 2/super_test.csv"
filename = "C:/Users/Mike/Documents/Practicum 2/EIG_check.csv"
f=open(filename, "w")
headers="Zip_Code, Pop, Minority, No_Diploma, Vacancy, No_Job, Poverty, Med_Inc, Chg_Job, Chg_Biz, Distress_Score, Rank\n"
f.write(headers)
zip_code = []
population = []
minority_list = []
No_Diploma_list = []
Vacancy_list = []
No_Job_list = []
Poverty_list = []
Med_Inc_list = []
Chg_Job_list = []
Chg_Biz_list = []
Distress_Score_list = []
Rank_list = []
for line in lines:
    if re.search("Economic Distress Indicators for", line):
        zipcode = line.strip()
        zipcode = zipcode.split(": ",1)[1]
        zipcode = zipcode.strip()
        zipcode = "Z"+zipcode
        zip_code.append(zipcode)
        print(zipcode)
    if re.search("Population", line):
        pop = line.strip()
        pop = pop.split(":\t",1)[1]
        pop = pop.replace(",", "")
        population.append(pop)
        print(pop)
    if re.search("Minority Share", line):
        minority = line.strip()
        minority = minority.split(":\t",1)[1]
        minority = minority.replace("%", "")
        minority_list.append(minority)
        print(minority)
    if re.search("No High School Diploma:", line):
        No_Diploma = line.strip()
        No_Diploma = No_Diploma.split("\t",2)[1]
        No_Diploma = No_Diploma.replace("%", "")
        No_Diploma_list.append(No_Diploma)
        print(No_Diploma)
    if re.search("Housing Vacancy Rate:", line):
        Vacancy = line.strip()
        Vacancy = Vacancy.split("\t",2)[1]
        Vacancy = Vacancy.replace("%", "")
        Vacancy_list.append(Vacancy)
        print(Vacancy)
    if re.search("Adults Not Working:", line):
        No_Job = line.strip()
        No_Job = No_Job.split("\t",2)[1]
        No_Job = No_Job.replace("%", "")
        No_Job_list.append(No_Job)
        print(No_Job)
    if re.search("Poverty Rate:", line):
        Poverty = line.strip()
        Poverty = Poverty.split("\t",2)[1]
        Poverty = Poverty.replace("%", "")
        Poverty_list.append(Poverty)
        print(Poverty)
    if re.search("Median Income Ratio:", line):
        Med_Inc = line.strip()
        Med_Inc = Med_Inc.split("\t",2)[1]
        Med_Inc = Med_Inc.replace("%", "")
        Med_Inc_list.append(Med_Inc)
        print(Med_Inc)
    if re.search("Change in Employment:", line):
        Chg_Job = line.strip()
        Chg_Job = Chg_Job.split("\t",2)[1]
        Chg_Job = Chg_Job.replace("%", "")
        Chg_Job_list.append(Chg_Job)
        print(Chg_Job)
    if re.search("Change in Businesses:", line):
        Chg_Biz = line.strip()
        Chg_Biz = Chg_Biz.split("\t",2)[1]
        Chg_Biz = Chg_Biz.replace("%", "")
        Chg_Biz_list.append(Chg_Biz)
        print(Chg_Biz)
    if re.search("Distress Score", line):
        Distress_Score = line.strip()
        Distress_Score = Distress_Score.split("\t",2)[1]
        Distress_Score_list.append(Distress_Score)
        print(Distress_Score)
    if re.search("Distress Rank:", line):
        Rank = line.strip()
        Rank = Rank.split("\t",2)[1]
        Rank = Rank.split("of",1)[0]
        Rank = Rank.replace(",", "")
        Rank = Rank.replace(" ", "")
        Rank_list.append(Rank)
        print(Rank)
i = 0
for i in range(len(zip_code)):
    f.write(zip_code[i]+","+population[i]+","+minority_list[i]+","+No_Diploma_list[i]+","+Vacancy_list[i]+","
            +No_Job_list[i]+","+Poverty_list[i]+","+Med_Inc_list[i]+","+Chg_Job_list[i]+","+Chg_Biz_list[i]+","
            +Distress_Score_list[i]+","+Rank_list[i]+"\n")
f.close()

## To check all the values are parsed correctly
print("There are ",(len(zip_code)),": observations for zipcode")
print("There are ",(len(population)),": observations for popuation")
print("There are ",(len(minority_list)),": observations for minority")
print("There are ",(len(No_Diploma_list)),": observations for No_Diploma")
print("There are ",(len(Vacancy_list)),": observations for Vacancy")
print("There are ",(len(No_Job_list)),": observations for zipcode")
print("There are ",(len(Poverty_list)),": observations for Poverty")
print("There are ",(len(Med_Inc_list)),": observations for med_inc")
print("There are ",(len(Chg_Job_list)),": observations for chg_job")
print("There are ",(len(Chg_Biz_list)),": observations for zipcode")
print("There are ",(len(Distress_Score_list)),": observations for Distress_Score")
print("There are ",(len(Rank_list)),": observations for Rank")


