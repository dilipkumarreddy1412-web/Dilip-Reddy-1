#python program to find the highest from a student data dictionary
student={"alice":100, "bob":200, "charlic":300, "david":700}
#find highest marks
highest_marks=max(student.values())

#find student(s) with highest marks
top_student=[name for name,marks in student.items()if marks==highest_marks]


print("Highest Marks:",highest_marks)
print("Top Marks:", ", ".join(top_student))


-------------------------------------------------------------------------------------
#shortcuts in above program
student={"alice":100, "bob":200, "charlic":300, "david":700}

print(student)

student['alice']

student['alice']=20
print(student)

k=input()

v=int(input())

student[k]=v               
print(student)


student={"mangapathi":'mango', "mahesh babu":'banana', "pasupathi":'apple', "prasad":'goa'}
