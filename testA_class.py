class classA:

    def __init__(self):
        self.xyz = 'Instance Attribute from ClassA'

    val = 'Class Attribute from testA'

    def newFunc():
        return __name__

    if __name__ == '__main__':
        val = newFunc()
        print(val)
