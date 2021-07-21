class Account:
    def __init__(self, owner, amount = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []
    def __repr__(self):
        # return f"Account of {self.owner} with starting amount: {self.amount}"
        return f"{__class__.__name__}"
    # def __repr__(self):
    #     return Account(self.owner, self.amount)



acc = Account('bob', 10)
acc2 = Account('john')
# print(acc)
print(repr(acc))
