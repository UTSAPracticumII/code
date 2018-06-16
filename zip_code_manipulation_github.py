"""
Created on Mon Jun 11 21:23:50 2018

@author: Mike Mahoney

Practicum 2 >> Creating a CSV file with all the zip_codes, city and state
This file is the github version
"""
import pandas as pd

us_postal_codes = pd.read_csv("C:/Users/Mike/Documents/Practicum 2/us_postal_codes.csv")
zip_code_list = pd.read_csv("C:/Users/Mike/Documents/Practicum 2/Housing.csv")
# Getting a list from us_postal_codes >> The list we want to filter >> It contains city and state
us_post = us_postal_codes.iloc[:,0].tolist()

# Getting the list of zipcodes we want >> The filter >> Use these to get the info from "zip_code_list" we want
zip_codes_using = zip_code_list.iloc[:,0].tolist()

#### Converting us_post (the list) to str
for i in range(len(us_post)):
    us_post[i] = str(us_post[i])

## Adding the Z and leading zeros to us_post
us_post_list = []
for zip_code in us_post:
    if (len(str(zip_code))) == 3:
        zip_code="Z00"+zip_code
        us_post_list.append(zip_code)
    elif (len(str(zip_code))) == 4:
        zip_code="Z0"+zip_code
        us_post_list.append(zip_code)
    elif (len(str(zip_code))) == 5:
        zip_code="Z"+zip_code
        us_post_list.append(zip_code)
        
## Getting the zip codes we need (from a known data file from Steve's instructions) from our info dataset   
master_zip_code = []
for item in zip_codes_using:
    for zip_code in us_post_list:
        if zip_code in item:
            master_zip_code.append(zip_code)

### This adds our str formated zip_codes to us_postal_codes
us_postal_codes.insert(loc=7, column="Zip_Code", value=us_post_list)

# Filtering us_postal_codes using master_zip_codes 
zip_code_data = us_postal_codes[us_postal_codes["Zip_Code"].isin(master_zip_code)]


### Indexing out columns
zip_code_data_1 = zip_code_data
zip_code_data_1 = zip_code_data_1.drop["Zip Code", 1]
zip_code_data_1.drop(zip_code_data_1.columns[[0,5,6]], axis = 1, inplace = True)
### Rearranging Columns
zip_code_data_1 = zip_code_data_1[["Zip_Code", "Place Name", "State Abbreviation", "State", "County"]]
#len(zip_codes_using) - len(master_zip_code)

#### Popuation Estimates >> 2011 to 2015 by Zip_Code
pop_est = pd.read_csv("C:/Users/Mike/Documents/Practicum 2/Pop_Est_11_15.csv")
# Filtering pop_est with zip_codes_using
pop_est = pop_est[pop_est["Zip_Code"].isin(master_zip_code)]

#### Merging the pop_est and zip_code_data_1 files on "Zip_Code"
zip_code_data_master = pd.merge(zip_code_data_1, pop_est, on = "Zip_Code", how = "outer")

###### Cleaning up the extra datasets >> To save space
zip_code_data = None
us_post = None
zip_code_list = None

###### Uploading the data file "dci_componenets.csv" that Steve created
dci = pd.read_csv("C:/Users/Mike/Documents/Practicum 2/dci_components.csv", index_col=0)
dci_zip_code = dci.iloc[:,0].tolist()
# Getting the zip_codes we are using >> filtering our zipcodes using dci_zip_code
master_zip_code = []
for item in dci_zip_code:
    for zip_code in us_post_list:
        if zip_code in item:
            master_zip_code.append(zip_code)

# Filtering us_postal_codes using master_zip_codes 
zip_code_data = us_postal_codes[us_postal_codes["Zip_Code"].isin(master_zip_code)]
# Indexing out columns
zip_code_data_2 = zip_code_data
#zip_code_data_2 = zip_code_data_2.drop["Zip Code", 1]
zip_code_data_2.drop(zip_code_data_2.columns[[0,5,6]], axis = 1, inplace = True)
### Rearranging Columns
zip_code_data_2 = zip_code_data_1[["Zip_Code", "Place Name", "State Abbreviation", "State", "County"]]

##### Uploading vacancy_status >> To see if we can get a better vacancy rate for DCI
vacancy_status = pd.read_csv("C:/Users/Mike/Documents/Practicum 2/vancany_status.csv")#, index_col=0)
housing = pd.read_csv("C:/Users/Mike/Documents/Practicum 2/housing.csv")
# Filtering vacancy_status using master_zip_codes 
vacancy_status = vacancy_status[vacancy_status["Zip_Code"].isin(master_zip_code)]
# Filtering housing using master_zip_codes 
housing = housing[housing["Zip_Code"].isin(master_zip_code)]
# Merging Housin_ units to vancany_status
vacancy_status = pd.merge(vacancy_status, housing, on="Zip_Code", how = "outer")
vacancy_status.drop(vacancy_status.columns[[10,11]], axis = 1, inplace = True)
# Getting vacancy_status column names >> to rearrange the column names
vacancy_headers = list(vacancy_status)
vacancy_headers.insert(1, vacancy_headers.pop())
# Rearranging the columns in vacancy_status
vacancy_status = vacancy_status[vacancy_headers]

# Wrting our results to CSV
#zip_code_data.to_csv("C:/Users/Mike/Documents/Practicum 2/zip_code_data.csv", encoding="utf-8", index=False)
####zip_code_data_1.to_csv("C:/Users/Mike/Documents/Practicum 2/zip_code_data_1.csv", encoding="utf-8", index=False)
zip_code_data_master.to_csv("C:/Users/Mike/Documents/Practicum 2/zip_code_data_master.csv", encoding="utf-8", index=False)

zip_code_data_2.to_csv("C:/Users/Mike/Documents/Practicum 2/zip_code_data_2.csv", encoding="utf-8", index=False)
#vacancy_status.to_csv("C:/Users/Mike/Documents/Practicum 2/vacancy_status.csv", encoding="utf-8", index=False)
