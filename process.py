log_file = open("um-server-01.txt") #this line is opening the um-server text file to be accessed in the process.py file

def sales_reports(log_file): # this is a function called sales_reports thats taking in the um-server aliased as log_file as a parameter
    for line in log_file: # a for loop that loops over every element in the log_file 
        line = line.rstrip() # removing any trailing characters at the end of a string (including spaces)
        day = line[0:3] # this line is setting a variable "day" equal to the third index of each line 
        if day == "Mon": # this line checks to see if the day variable is equal to Mon(day)
            print(line) # prints out the line if it is equal to "Mon"

sales_reports(log_file) # invoking the sales_report funciton passing in log_file (um-server-01.txt) as an argument 

