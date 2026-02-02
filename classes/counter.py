class counter:
    def __init__(self, start = 0, step = 1):
        self.start = start
        self.step = step
        self.value = start

    def inc(self):
        self.value = self.value + self.step
        return self.value

    def dec(self):
        self.value = self.value - self.step
        return self.value
    
    def reset(self):
        self.value = self.start


x = counter(start=10, step=4)

print(x.inc())
