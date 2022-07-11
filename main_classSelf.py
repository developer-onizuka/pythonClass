from testA_classSelf import classA
from testB_classSelf import classB

print(classA.val)
print(classB.val)

a = classA('Instance Attribute from ClassA, 2022-07-05')
a.selfFunc()

b = classB('Instance Attribute from ClassB, 2022-07-05')
b.selfFunc()
