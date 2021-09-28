import datetime
date=datetime.date.today()
year=date.strftime("%y")
print(year)
name= input("enter name")
age= int(input("enter age"))
if (age < 100):
     age=100-age
     year1=year+age
     print("you complete 100 year at",year1)

