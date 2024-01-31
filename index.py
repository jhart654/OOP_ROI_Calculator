class rental_property_calculator:
    pass

    def __init__(self, rental_income, expenses):
        self.rental_income = rental_income
        self.expenses = expenses

    def monthly_cashflow(self):
        self.cashflow = self.rental_income - self.expenses
        return self.cashflow
    
    def cashOnCash(self):
        self.downPayment = int(input('How much is your down payment? $'))
        self.closingCost = int(input('How much is your closing costs? $'))
        self.rehab = int(input('How much was your rehab budget? $'))
        self.misc = int(input('How much is your miscellaneous costs? $'))

        self.totalInvestment = self.downPayment + self.closingCost + self.rehab + self.misc

        self.yearlyCashflow = self.cashflow * 12
        
        self.roi = self.yearlyCashflow / self.totalInvestment
        self.roi *= 100
        print(f'Your ROI for this property is {self.roi}%')

property1 = rental_property_calculator(2000, 1610)
property1.monthly_cashflow()
property1.cashOnCash()

    

         
        
    