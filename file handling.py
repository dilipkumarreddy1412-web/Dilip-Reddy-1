
nv=0
temp="today is monday"
for i in temp:
    if i in 'likiTH':
        nv+=1
print(nv)


with open("notes.txt", "w") as file:
    file.write("hello,python!\n")
    file.write("file handling is easy.")


with open("notes.txt","r")as file:
    content=file.read()
print(content)


with open("notes.txt","r") as file:
    for line in file:
        print(line.strip())



fp=open(r"m:\1st semester\python\notes.txt","r")
fp.seek(0)
print(fp.read(5))
fp.seek(10)
print(fp.read(5))

import pickle
data={"name":"alice","age":25}
with open(r"m:\1st semester\python\notes.txt","wb")as file:
    pickle.dump(data,file)
    print("file written")


with open(r"m:\1st semester\python\notes.txt","rb")as file:
    data=pickle.load(file)
    print(data)
    


chr(65)

chr(90)

chr(97)

chr(122)

import pickle
with open(r"m:\1st semester\python\image1.jpg","rb")as source:
    data=source.read()

with open(r"m:\1st semester\python\eye1.jpg","wb")as target:
    target.write(data)
    
print("image completed")



import pickle
with open(r"m:\1st semester\python\video1.mp4","rb")as source:
    data=source.read()

with open(r"m:\1st semester\python\nature1.mp4","wb")as target:
    target.write(data)
    
print("image completed")
