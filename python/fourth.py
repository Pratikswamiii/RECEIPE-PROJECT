# dic={
#     "table":{
# "a piece of furbiture","list of facts and figures"
#     },
#     "cat":{
# "a small animal"
#     }
# }

# print(list(dic.keys()))


# set={"python","java","c++","python","c","java","c++","python","javascript"}
# print(len(set))

marks={}
x=int(input("enter phy marks:"))
marks.update({"phy":x})
y=int(input("enter chem marks:"))
marks.update({"chem":y})
z=int(input("enter math marks:"))
marks.update({"math":z})
print(marks)