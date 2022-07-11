from testA_class import classA
from testB_class import classB

print(classA.val)
print(classB.val)

print("")

a = classA()
print(a.xyz)
a.xyz = 'Instance Attribute from ClassA, 2022-07-05'
print(a.xyz)
classA.classFunc()

print("")

b = classB()
print(b.xyz)
b.xyz = 'Instance Attribute from ClassB, 2022-07-05'
print(b.xyz)
classB.classFunc()
