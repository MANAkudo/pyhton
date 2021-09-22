num = {"id":"100",
 "name":"大原太郎",
 "age":19
}

num.update(age = 20)

for key,value in num.items():
    print(key, ":",value,sep="")