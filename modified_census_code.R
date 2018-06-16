### Data Manipulation from the Data Sets Steven gave insturctions to create
## HS_Grad
hs_grad_file_upload <- file.choose()
hs_grad <- read.csv(hs_grad_file_upload)
hs_grad$Pct_HS_Grad <- as.numeric(levels(hs_grad$Pct_HS_Grad))[hs_grad$Pct_HS_Grad]

i = 1
for (i in 1:nrow(hs_grad)) {
  hs_grad$Pct_Not_HS_Grad[i] <- sum(100, -(hs_grad$Pct_HS_Grad[i]))
}

## Adult_Working
Adult_Working_file_upload <- file.choose()
Adult_Working <- read.csv(Adult_Working_file_upload)
Adult_Working$Pct_Working <- as.numeric(levels(Adult_Working$Pct_Working))[Adult_Working$Pct_Working]
Adult_Working$Pct_Working_bach_or_more <- as.numeric(levels(Adult_Working$Pct_Working_bach_or_more))[Adult_Working$Pct_Working_bach_or_more]

#Adult_Working$Pct_Not_Working <- NULL
#Adult_Working$Pct_Not_Working_bach_or_more <- NULL

i = 1
for (i in 1:nrow(Adult_Working)) {
  Adult_Working$Pct_Not_Working[i] <- sum(100, -(Adult_Working$Pct_Working[i]))
  Adult_Working$Pct_Not_Working_bach_or_more[i] <- sum(100, -(Adult_Working$Pct_Working_bach_or_more[i]))
}

vacancy_status <- read.csv("C:/Users/Mike/Documents/Practicum 2/vacancy_status.csv")
dci <- read.csv("C:/Users/Mike/Documents/Practicum 2/dci_components.csv")
### Creating a loop for vacancy_status >> Creating a new column for 
### vancancy - seasonal >> to see if it is a better depiction
i = 1
for (i in 1:nrow(vacancy_status)) {
  vacancy_status$Vacant_perm[i] <- sum(vacancy_status$Total_Vacant[i], -(vacancy_status$Seasonal[i]))
  vacancy_status$vacancy_pct[i] <- (vacancy_status$Vacant_perm[i]/vacancy_status$Housing_Units[i])*100
}
## Cleaning up vacancy_status
vacancy_status$For_rent <- NULL
vacancy_status$Rented_not_oc <- NULL
vacancy_status$For_sale <- NULL
vacancy_status$Sale_not_oc <- NULL
vacancy_status$Migrant_worker <- NULL
vacancy_status$Other_vacant <- NULL
vacancy_status$vacancy_pct <- format(round(vacancy_status$vacancy_pct, 1), nsmall = 1) 

## Writing vacancy_status to a csv >> to upload to github
#write.csv(vacancy_status, "C:/Users/Mike/Documents/Practicum 2/vacancy_status_accurate.csv")
vacancy_status$Housing_Units <- NULL
vacancy_status$Total_Vacant <- NULL
vacancy_status$Seasonal <- NULL
vacancy_status$Vacant_perm <- NULL
### Creating dci_1 >> to get vacancy_status$Vacant_perm >> a more accurate number
dci_1 <- merge(dci, vacancy_status, by="Zip_Code")

# Rearranging the columns & renaming vacancy_pct >> Vacancy
dci_1 <- dci_1[,c(1,2,3,4,5,11,6,7,8,9,10)]
colnames(dci_1)[colnames(dci_1)=="vacancy_pct"] <- "Vacancy"

## Writing dci_1 to csv
#write.csv(dci_1, "C:/Users/Mike/Documents/Practicum 2/dci_1.csv", row.names = FALSE)
