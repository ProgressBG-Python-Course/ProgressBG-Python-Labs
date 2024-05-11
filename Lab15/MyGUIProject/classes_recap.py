# the base class
class Parent:
    def __init__(self,*args, **kwargs):
        print('constructor execute')
        print(args)
        print(kwargs)
        self.a = args[0]
        self.b = args[1]
        self.c = kwargs.get('c')
        self.d = kwargs.get('d')

    def show_a(self):
        print(f'a={self.a}')

# the derived class, which inherits from base class:
class Child(Parent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "(a={},b={},c={},d={})".format(self.a, self.b, self.c, self.d)


# p1 = Parent(1,2,a=3,b=4)

c = Child(5,6,c=7,d=8)

c.show_a()