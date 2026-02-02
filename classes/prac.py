class greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"
    
    def rename (self, rename):
        self.name = rename
        return f"Hello {rename}"


x = greeter("raghav")

x.rename("rb")


print(x.greet())





