
class CurrencyConverter:
    def __init__(self, currencies):
        self.currencies = currencies

    def convert(self, amount, from_currency, to_currency):
        if (not from_currency in self.currencies):
            print("Current exchange rate does not exist in converter.")
            return amount
        elif (not to_currency in self.currencies):
            print("Desired exchange rate does not exist in converter.")
            return amount
        elif (amount < 0):
            print("Original currency amount cannot be negative.")
            return amount
        else:
            new_amount = (amount / self.currencies[from_currency]) * self.currencies[to_currency]
            return round(new_amount, 2)

    def add_rate(self, currency, rate):
        self.currencies[currency] = rate


