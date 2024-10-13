var=("item1",2,3)
print(type(var))
num=(1,)
print(type(num))
#acessing value in a tuple
print(var[2])
#immutable
#var[0]="tom"
tup1=("aitem","aitem2","aitem3")
#concatenation
print(var+tup1)
#nested tuple
print(var,tup1)
#tuple slicing
print(tup1[1:3])
#deleting a tuple
del num
#length of tuple
print(len(tup1))
#typecasting
tup1=list(tup1)
print(type(tup1))
print(tuple("string"))
#packing and unpacking
address=(32,"street","st peter","UK",123456)
(dnum,streetname,place,country,pin)=address
print(dnum)
