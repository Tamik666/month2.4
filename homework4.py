class SavingAccount:
    def __init__(self, attribute):
        self.attribute = attribute

    def __str__(self):
        return self.attribute


class CheckingAccount:
    def __init__(self, attribute):
        self.attribute1 = attribute

    def __str__(self):
        return self.attribute1


class Stock:
    def __init__(self, attribute):
        self.attribute2 = attribute

    def __str__(self):
        return self.attribute2


class Bond:
    def __init__(self, attribute):
        self.attribute3 = attribute

    def __str__(self):
        return self.attribute3


class RealEstate:
    def __init__(self, attribute):
        self.attribute4 = attribute

    def __str__(self):
        return self.attribute4


class BankAccount(SavingAccount, CheckingAccount):
    def __init__(self, attribute, attribute1):
        SavingAccount.__init__(self, attribute)
        CheckingAccount.__init__(self, attribute1)

    def __str__(self):
        return f"{SavingAccount.__str__(self)} + {CheckingAccount.__str__(self)}"


class Security(Stock, Bond):
    def __init__(self, attribute2, attribute3):
        Stock.__init__(self, attribute2)
        Bond.__init__(self, attribute3)

    def __str__(self):
        return f"{Stock.__str__(self)} + {Bond.__str__(self)}"


class Asset(BankAccount, Security, RealEstate):
    def __init__(self, attribute, attribute1, attribute2, attribute3, attribute4):
        BankAccount.__init__(self, attribute, attribute1)
        Security.__init__(self, attribute2, attribute3)
        RealEstate.__init__(self, attribute4)

    def __str__(self):
        return f"{BankAccount.__str__(self)} + {Security.__str__(self)} + {RealEstate.__str__(self)}"


class InsurableItem(BankAccount, RealEstate):
    def __init__(self, attribute, attribute1, attribute4):
        BankAccount.__init__(self, attribute, attribute1)
        RealEstate.__init__(self, attribute4)

    def __str__(self):
        return f"{BankAccount.__str__(self)} + {RealEstate.__str__(self)}"


class InterestBearingItem(BankAccount, Security):
    def __init__(self, attribute, attribute1, attribute2, attribute3):
        BankAccount.__init__(self, attribute, attribute1)
        Security.__init__(self, attribute2, attribute3)

    def __str__(self):
        return f"{BankAccount.__str__(self)} + {Security.__str__(self)}"


# Пример использования класса BankAccount
a = InterestBearingItem("1", "2", "3", "4")
print(a)
print(InsurableItem.mro())
