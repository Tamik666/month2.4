class Stock:
    def __init__(self, fray):
        self.fray = fray

    def __str__(self):
        return self.fray


class Bond:
    def __init__(self, brew):
        self.brew = brew

    def __str__(self):
        return self.brew


class Security(Stock, Bond):
    def __init__(self, fray, brew):
        Stock.__init__(self, fray)
        Bond.__init__(self, brew)

    def __str__(self):
        return f"{Stock.__str__(self)}, {Bond.__str__(self)}"


a = Security('a', 'b')

print(a)
