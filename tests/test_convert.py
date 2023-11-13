import pytest


# Aislo la funcion
def convert(amount, from_curr, to_curr, value):
    try:
        amount = float(amount)
        from_curr = from_curr
        to_curr = to_curr

        # Numero negativo
        if amount < 0:
            raise ValueError("Only positve numbers")

        # Realizar la conversión
        if from_curr == "BTC":
            if to_curr == "USD":
                result = amount * value
            elif to_curr == "ARS":
                result = amount * value
        elif from_curr == "ETH":
            if to_curr == "USD":
                result = amount * value
            elif to_curr == "ARS":
                result = amount * value
        elif from_curr == "USDT":
            if to_curr == "USD":
                result = amount * value
            elif to_curr == "ARS":
                result = amount * value

        return result
    except ValueError:
        return "Conversion Invalidad"


# Testing funcion
@pytest.mark.parametrize(
    "amount, from_curr, to_curr,value, expected_result",
    [
        (10, "BTC", "USD", 10, 100),
        (5, "ETH", "ARS", 5, 25),
        (-1, "USDT", "USD", 5, "Conversion Invalidad"),
        ("AAA", "USDT", "USD", 5, "Conversion Invalidad"),
    ],
)
def test_convert(amount, from_curr, to_curr, value, expected_result):
    # Llamar a la función convert() con los valores de prueba
    result = convert(amount, from_curr, to_curr, value)

    # Verificar el resultado
    assert result == expected_result
