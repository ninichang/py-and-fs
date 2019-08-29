# Factoroal survey mturk check funtion 

# mturk how to approve and reject task : =====

# APPROVE ASSIGNMENT: Indicate which assignments to approve by putting an "x" under a column titled "Approve".
# REJECT ASSIGNMENT: Indicate which assignments to reject by putting your reject feedback under a column titled "Reject".


# NOTE : check if the input columns are indeed from 30-37 in the csv files

# code =====
data <- read.csv("results.csv", stringsAsFactors = FALSE)
range_inputs <- 30:37
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
  
  if(data[i, "Answer.reason_cannot_find"] == "{}"){
    
    # the columns of input are from 30-37
    if(any(data[i, range_inputs] == "{}")){
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






# Can we reject any non-words? That is words that are misspelled.
write.csv(data, file = "checked-mturk.csv")

# reject rate:
sum(data[, "Reject"] != '')/nrow(data)

