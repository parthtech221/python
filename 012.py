a=int(input("enter total marks (out of 100):"))
marks_list= []
for i in range(5):
    marks=int(input("enter marks of student {}:".format(i+1)))
    marks_list.append(marks)
total=sum(marks_list)
print("Total marks:", total)
print("Percentage:", (total/(a*5))*100)