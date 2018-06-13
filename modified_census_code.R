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
