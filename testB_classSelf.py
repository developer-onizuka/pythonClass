class classB:
    def __init__(self, xyz):
        self.xyz = xyz
    def selfFunc(self):
        print(self.xyz)

    val = 'Class Attribute from testB'

def newFunc():
    return __name__

if __name__ == '__main__':
    val = newFunc()
    print(val)
