# Currency Translator
This Python class uses a given dictionary of currency exchange rates to convert between currency values.


| Class Name | CurrencyConverter |
| - | - |
| Variables | currencies: dictionary |
| Methods | \_\_init__(currencies) <br>convert(amount, from_currency, to_currency) <br>add_rate(currency, rate) | 

## Example
```
example_rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.78,
    "JPY": 150.50,
    "INR": 83.30
}

converter = CurrencyConverter(example_rates)

# Convert (100) USD into (92) euros
cash = 100
cash = converter.convert(cash, "USD", "EUR")

# Convert (92) euroes into (15,050) Japanese yen
cash = converter.convert(cash, "EUR", "JPY")

# Add Canadian dollars as a rate, then convert (15,050) Japanese yen into (136) Canadian dollars
converter.add_rate("CAD", 1.36)
cash = converter.convert(cash, "JPY", "CAD")

# Converter won't work if currency rates don't exist or if amount given is negative
cash = converter.convert(cash, "CAD", )