class classB:

    def __init__(self):
        self.xyz = 'Instance Attribute from ClassB'

    val = 'Class Attribute from testB'

    def newFunc():
        return __name__

    if __name__ == '__main__':
        val = newFunc()
