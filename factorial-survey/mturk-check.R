# Factoroal survey mturk check funtion 

# Instruction : 
# Follow the order of the code.

# Check round 1 =====
data <- read.csv("results-2016-2018-round3.csv", stringsAsFactors = FALSE)
range_inputs <- 30:37 #without reasons_cannot_find!!
colnames(data[, 30:37])
# should look like this:
# [1] "Answer.article_title" "Answer.first_name1"   "Answer.first_name2" 
# [4] "Answer.inst1"         "Answer.inst2"         "Answer.journal_name"
# [7] "Answer.last_name1"    "Answer.last_name2"   


data[, "Reject"] = ""
for(i in 1:nrow(data)){
  
  # if the answer was given within ___ seconds, reject the answer.
  if(data[i, "WorkTimeInSeconds"] < 70){
    data[i,"Reject"] = paste(data[i,"Reject"], "Too fast.")
  }
  
  # Force them to write First Name as “Single” and Last Name as “Author” for 
  # articles with only one author. 
  # Reject everyone that has the same first name and last name for the two authors.
  
  if(data[i, "Answer.first_name1"] == data[i, "Answer.first_name2"] ||
     data[i, "Answer.last_name1"] == data[i, "Answer.last_name2"]){
    data[i, "Reject"] = paste(data[i,"Reject"], 
                              "Did not read instructions (Single Author). ")
  }
  
  # Reject those with any missing data, except the last one. 
  # If the last response isn't missing, do not reject them. 
  # We will look at them manually.
  
  if(data[i, "Answer.reason_cannot_find"] == "{}" || 
     is.na(data[i, "Answer.reason_cannot_find"])){
    
    if(any(data[i, range_inputs] == "{}" ||
           any(is.na(data[i, range_inputs])))){
      data[i, "Reject"] = paste(data[i,"Reject"], "Did not answer every question. ")
    }
    
    # Select those with all capital letters in a response and look at them manually.
    if(all(unlist(sapply(data[i, range_inputs], 
                         function(x) {strsplit(x, "")})) %in% LETTERS)){
      data[i, "Reject"] = paste(data[i,"Reject"], 
                                "CHECK: All capital inputs "  )
    }
    
    
    # Select those with a lower-case first letter of any response 
    # and decide if we want to reject them.
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
print(paste("Original Reject rate is:", rate))


# Write csv to reject mturk responses =====
# turn all the reject reasons into "did not meet requirements"
data2 <- data
data2[data2[, "Reject"] != "", "Reject"] =  "did not meet requirements"

# update the Approve column by putting an x inside
data2[data2[, "Reject"] == "", "Approve"] <- "x"
data2[is.na(data2[, "Approve"]), "Approve"] <- ""

# csv to upload to mturk website
write.csv(data2, file = "checked-mturk.csv")



# Manually check data that will be rejected =====
# csv of data that needs manual check
data_check <- data[grepl("CHECK", data[, "Reject"]), ]

# add an index column for reference
data_check[ , "index"] <- 1: nrow(data_check)

write.csv(data_check, file = "need-checking.csv")

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

# Check round 2 =====
# check submitted response after rejecting them in the first round 
data <- read.csv("results-round2.csv", stringsAsFactors = FALSE)
data <- data[data$AssignmentStatus == "Submitted", ]
# now run the function created in round 1 on this data


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

# CSV that needs manual check b4 collecting emails =====

# important: need to check if author first name = single author
data3 <- data[data$Reject == "", ]
author1 <- paste(data3$Answer.first_name1, data3$Answer.last_name1)
author2 <- paste(data3$Answer.first_name2, data3$Answer.last_name2)
df <- data.frame(name = c(author1, author2), 
                 institution = c(data3$Answer.inst1, data3$Answer.inst2),
                 delete = rep("", length(author1)), 
                 stringsAsFactors = FALSE)

df <- df %>% filter(.$name != "Single Author", .$name != "{}", .$institution !="{}")
write.csv(df, file = "author_inst_2016-2018-4.csv", row.names = FALSE)


# Manage CSV after author name and institution are ready =====
data <- read.csv("chienn1.csv")
data2 <- read.csv("chienn2.csv")
authors <- rbind(subset(data[,-3], data$delete != "x"), subset(data2[, -3], data2$delete != "x"))

data6 <- subset(data5[,-3], data5$delete != "x")
head(authors)
write.csv(authors, file = "authors_and_emails_task_mturk.csv", row.names = FALSE)



# manage email collection =====
emails <- read.csv("2016-2018-emails01.csv")
# filter out wrong email address source 
source <- grepl("http", emails$Answer.source)
# filter out wrong email address format
correct_email_format <- grepl("@", emails$Answer.email)

approve_index <- ifelse(source == TRUE & correct_email_format == TRUE, 
                 TRUE, FALSE)
emails$Approve <- ifelse(approve_index == TRUE, "x", "")
emails$Reject <- ifelse(approve_index == FALSE, "x", "")

# csv to upload to mturk
write.csv(emails, file = "upload_to_mturk_emails.csv", row.names = FALSE)

# Collect name, institu., email, source
library(dplyr)
collected_emails <- emails %>%
  filter(.$Approve == "x") %>%
  select(Input.name, Input.institution, Answer.email, Answer.source)

original_email <- read.csv("collected_emails.csv")
write.csv(rbind(original_email, collected_emails), file = "collected_emails-v2.csv", row.names = FALSE)




data5 <- rbind(data1, data2, data3, data4)
write.csv(data5, file = "author_inst_2016-2018.csv")


results3 %>%
  count(.$AssignmentStatus == "Approved")

table(results2$AssignmentStatus)
table(results3$AssignmentStatus) - table(results2$AssignmentStatus)

num_article_per_year %>% 
  filter(.$year %in% c(2016:2018)) %>%
  colSums()




