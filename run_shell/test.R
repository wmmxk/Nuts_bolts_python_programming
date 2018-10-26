args <- commandArgs(TRUE)

path <- args[1]

df = read.csv(paste(path,"test_data.csv",sep="/"))
print(df)

