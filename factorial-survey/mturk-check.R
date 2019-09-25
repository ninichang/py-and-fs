# Factoroal survey mturk check funtion 

# mturk how to approve and reject task : =====

# APPROVE ASSIGNMENT: Indicate which assignments to approve by putting an "x" under a column titled "Approve".
# REJECT ASSIGNMENT: Indicate which assignments to reject by putting your reject feedback under a column titled "Reject".


# NOTE : check if the input columns are indeed from 30-37 in the csv files

# code =====
data <- read.csv("results.csv", stringsAsFactors = FALSE)
range_inputs <- 30:37 #without reasons_cannot_find!!
data[, "Reject"] = ""

# Calculate the distribution of time it takes to finish a task. If someone is too fast, flag it. We will manually check.

for(i in 1:nrow(data)){
  # if the answer was given within ___ seconds, reject the answer.
  if(data[i, "WorkTimeInSeconds"] < 70){
    data[i,"Reject"] = paste(data[i,"Reject"], "Too fast.")
  }
  
  # Force them to write First Name as “Single” and Last Name as “Author” for those     articles with only one author. Then reject everyone that has the same first name     and last name for the two authors.
  
  if("Answer.first_name1" == "Answer.first_name2" && 
     "Answer.last_name1" == "Answer.last_name2"){
    data[i, "Reject"] = paste(data[i,"Reject"], 
                              "Did not read instructions (Single Author). ")
  }
  
  # Reject those with any missing data, except the last one. If the last response is   not missing, then do not reject them. We will look at them manually.
  
  if(data[i, "Answer.reason_cannot_find"] == "{}" || 
     is.na(data[i, "Answer.reason_cannot_find"])){
    
    if(any(data[i, range_inputs] == "{}" ||
           any(is.na(data[i, range_inputs])))){
      data[i, "Reject"] = paste(data[i,"Reject"], "Did not answer every question. ")
    }
    
    # Select those with all capital letters in a response and look at them manually.
    if(all(unlist(sapply(data[i, range_inputs], 
                         function(x) strsplit(x, ''))) %in% LETTERS)){
      data[i, "Reject"] = paste(data[i,"Reject"], "CHECK: All capital inputs ")
    }
    
    
    # Select those with a lower-case first letter of any response and decide if we       want to reject them.
    if(any(substr(data[i, range_inputs], 1, 1) %in% letters)){
      data[i, "Reject"] = paste(data[i,"Reject"], "First letter not capitalized. ")
    }
    
    # Reject if the surname of the authors is only a single letter.
    if(length(unlist(strsplit(data[i, "Answer.last_name1"], ''))) == 1 ||
       length(unlist(strsplit(data[i, "Answer.last_name2"], ''))) == 1){
      data[i, "Reject"] = paste(data[i,"Reject"], "Last Name only 1 character. ")
    }
  }
  else{
    data[i, "Reject"] = paste(data[i,"Reject"], "CHECK: Cannot find.")
  }
}

# reject rate:
rate <- sum(data[, "Reject"] != '')/nrow(data)
print(paste("Reject rate is:", rate))

# csv of data that needs manual check
data_check <- data[grepl("CHECK", data[, "Reject"]), ]

# add an index column for reference
data_check[ , "index"] <- 1: nrow(data_check)

write.csv(data, file = "need-checking.csv")

# go through each data that needs checking. Say that row x shall not be rejected and we wish to update this in "data"
approve <- function(x){
  for(i in x){
    index <- which(data_check[i , "AssignmentId"] == data[ , "AssignmentId"])
    data[index, "Reject"] <- ""
    data[index, "Approve"] <- "x"
  }
}

# function to see how many tasks a specific turker does
num_task <- function(x){
  index <- which(data_check[x , "WorkerId"] == data[ , "WorkerId"])
  print(index)
}

# new reject rate:
rate2 <- sum(data[, "Reject"] != '')/nrow(data)
print(paste("New reject rate is:", rate2))



# turn all the reject reasons into "did not meet requirements"
data2 <- data
data2[data2[, "Reject"] != "", "Reject"] =  "did not meet requirements"

# update the Approve column by putting an x inside
data2[data2[, "Reject"] == "", "Approve"] <- "x"
data2[is.na(data2[, "Approve"]), "Approve"] <- ""

# csv to upload to mturk website
write.csv(data2, file = "checked-mturk.csv")




# manage the workers =====
workers <- read.csv("workers.csv", stringsAsFactors = FALSE)


for(i in 1:nrow(data_check)){
  index <- which(data_check[i, "WorkerId"] == workers[, 1])
  workers[index, "UPDATE.BlockStatus"] <- "Block"
  workers[index, "BlockReason"] <- "Low quality response"
}

library(dplyr)
worker_data <- workers %>%
  select(c("Worker.ID", "UPDATE.BlockStatus", "BlockReason")) 

colnames(worker_data) <- c("WorkerID", "UPDATE BlockStatus", "BlockReason")
write.csv(worker_data, file = "workers.csv")

# 1st trial for emails =====

author1 <- paste(data2$Answer.first_name1, data2$Answer.last_name1)
author2 <- paste(data2$Answer.first_name2, data2$Answer.last_name2)
df <- data.frame(name = c(author1, author2), institution = c(data2$Answer.inst1, data2$Answer.inst2), delete = rep("", 690))

write.csv(df, file = "emails-1990-1995.csv", row.names = FALSE)
