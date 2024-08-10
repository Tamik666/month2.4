class SavingAccount:
    pass


class CheckingAccount:
    pass


class Stock:
    pass


class Bond:
    pass


class RealEstate:
    pass


class BankAccount(SavingAccount, CheckingAccount):
    pass


class Security(Stock, Bond):
    pass


class Asset(BankAccount, Security, RealEstate):
    pass


class InsurableItem(BankAccount, RealEstate):
    pass


class InterestBearingItem(BankAccount, Security):
    pass
