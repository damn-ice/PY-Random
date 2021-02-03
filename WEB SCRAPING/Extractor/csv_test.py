

# def listList(items, threshold):
#     final_result = []
#     variable_data = []
#     count = 0
#     for item in items:
#         count += 1
#         variable_data.append(item)
#         if count == threshold:
#             final_result.append(variable_data)
#             count = 0
#             variable_data = []
#     return final_result
        

import csv 
  
# field names 
fields = ['Name', 'Branch', 'Year', 'CGPA'] 
  
# data rows of csv file 
rows = [ ['Nikhil', 'COE', '2', '9.0'], 
         ['Sanchit', 'COE', '2', '9.1'], 
         ['Aditya', 'IT', '2', '9.3'], 
         ['Sagar', 'SE', '1', '9.5'], 
         ['Prateek', 'MCE', '3', '7.8'], 
         ['Sahil', 'EP', '2', '9.1']] 
  
# name of csv file 
filename = "university_records.csv"
  
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
      
    # writing the fields 
    csvwriter.writerow(fields) 
      
    # writing the data rows 
    csvwriter.writerows(rows)

