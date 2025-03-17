class Calculator:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def get_values(self):
        self.principal = float(input("What is your principal? "))
        self.rate = float(input("What is your rate? ")) / 100
        self.time = float(input("What is your time? "))

class SimpleInterest(Calculator):
    def result(self):
        amount = self.principal * (1 + (self.rate/100) * self.time)
        print(amount)

class CompoundInterest(Calculator):
    def __init__(self, principal, rate, time, no_of_times_compounded_per_year):
        super().__init__(principal, rate, time)
        self.no_of_times_compounded_per_year = float(input("How many times does your interest compound per year? "))

    def result(self):
        amount = self.principal * (1 + (self.rate / self.no_of_times_compounded_per_year)) ** (self.no_of_times_compounded_per_year * self.time)
        print(amount)

class AnnuityPlan(Calculator):
    def __init__(self, principal, rate, time, no_of_times_compounded_per_year, payment_amount_per_period):
        super().__init__(principal, rate, time)
        self.no_of_times_compounded_per_year = float(input("How many times does your interest compound per year? "))
        self.payment_amount_per_period = float(input("your payment amount per period? "))

    def result(self):
        r_over_n = self.rate / self.no_of_times_compounded_per_year
        nt = self.no_of_times_compounded_per_year * self.time
        amount = self.payment_amount_per_period * (((1 + r_over_n) ** nt - 1) / r_over_n) + (self.principal * (1 + r_over_n) ** nt)
        print(amount)

# Simple Interest
si_instance = SimpleInterest(0, 0, 0) #place holder values.
si_instance.get_values()
si_instance.result()

# Compound Interest
ci_instance = CompoundInterest(0, 0, 0, 0)
ci_instance.get_values()
ci_instance.result()

# Annuity Plan
ap_instance = AnnuityPlan(0, 0, 0, 0, 0)
ap_instance.get_values()
ap_instance.result()