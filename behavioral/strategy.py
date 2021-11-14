import types


class Strategy:

    def __init__(self, function=None):
        self.name = "Default Strategy"
        # If function is provided, replace the execute() method with the given function
        if function:
            self.execute = types.MethodType(function, self)
            # this allows us to add new method dynamically

    def execute(self):
        """The defaut method that prints the name of the strategy being used"""
        print(f"{self.name} is used!")


def strategy_one(self):
    print(f"{self.name} is used to execute method 1")


def strategy_two(self):
    print(f"{self.name} is used to execute method 2")


# create default strategy
s0 = Strategy()
s0.execute()

# create first varition of the default strategy by providing a new behavior
s1 = Strategy(strategy_one)
s1.name = "Strategy One"
s1.execute()

# create second varition of the default strategy by providing a new behavior
s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()
