import pytest
from currency import CurrencyConverter

@pytest.fixture
def converter():
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.78,
        "JPY": 150.50,
        "INR": 83.30
    }
    return CurrencyConverter(exchange_rates)

def test_convert_to_base_currency(converter):
    # Tests converting EUR to USD (100 / 0.92 * 1.0 = 108.6956...)
    result = converter.convert(100, "EUR", "USD")
    assert result == 108.70

def test_convert_between_non_base_currencies(converter):
    # Tests converting GBP to JPY (100 / 0.78 * 150.50 = 19294.871...)
    result = converter.convert(100, "GBP", "JPY")
    assert result == 19294.87

def test_add_rate(converter):
    # Tests adding a new currency (CAD) and using it
    converter.add_rate("CAD", 1.36)
    
    # Verify it exists by converting USD to CAD
    assert converter.convert(100, "USD", "CAD") == 136.00

def test_convert_to_nonexistant_currency(converter):
    # Tests failure converting TO a currency that does not exist in the converter
    result = converter.convert(100, "USD", "IND")
    assert result == 100

def test_convert_from_nonexistant_currency(converter):
    # Tests failure converting FROM a currency that does not exist in the converter
    result = converter.convert(100, "IND", "USD")
    assert result == 100

def test_convert_negative_amount(converter):
    # Tests failure converting a negative amount of money
    result = converter.convert(-100, "USD", "GBP")
    assert result == -100
