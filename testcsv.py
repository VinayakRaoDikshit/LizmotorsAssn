import csv
with open('testFile.csv', 'a',newline='') as file:
  writer=csv.writer(file)
  a=['Hello','World']
  writer.writerow(a)  
