import requests
import tkinter as tk


# Create obj for each coin
class Coin:
    def __init__(self, name, nick, value, value_ars):
        self.name = name
        self.nick = nick
        self.value = round(float(value), 2)
        self.value_ars = round(float(value) * float(value_ars), 2)


def main():
    # Create the objects
    btc = Coin(
        "Bitcoin",
        "BTC",
        response_crypto("https://rest.coinapi.io/v1/exchangerate/BTC/USD"),
        response_ars(),
    )
    eth = Coin(
        "Ethereum",
        "ETH",
        response_crypto("https://rest.coinapi.io/v1/exchangerate/ETH/USD"),
        response_ars(),
    )
    usdt = Coin(
        "Tether",
        "USDT",
        response_crypto("https://rest.coinapi.io/v1/exchangerate/USDT/USD"),
        response_ars(),
    )

    # Crear ventana
    window = tk.Tk()
    window.title("Cotizaciones de Monedas")
    window.geometry("400x300")
    window.config(background="#121212")

    # Crear etiquetas para las cotizaciones
    btc_label = tk.Label(
        window, text=f"{btc.name} ({btc.nick}):", fg="white", bg="orange"
    )
    btc_label.grid(row=0, column=0)
    btc_usd_label = tk.Label(
        window, text=f"USD: {btc.value:,.2f}", fg="white", bg="orange"
    )
    btc_usd_label.grid(row=0, column=1)
    btc_ars_label = tk.Label(
        window, text=f"ARS: {btc.value_ars:,.2f}", fg="white", bg="orange"
    )
    btc_ars_label.grid(row=0, column=2)

    eth_label = tk.Label(
        window, text=f"{eth.name} ({eth.nick}):", fg="white", bg="gray"
    )
    eth_label.grid(row=1, column=0)
    eth_usd_label = tk.Label(
        window, text=f"USD: {eth.value:,.2f}", fg="white", bg="gray"
    )
    eth_usd_label.grid(row=1, column=1)
    eth_ars_label = tk.Label(
        window, text=f"ARS: {eth.value_ars:,.2f}", fg="white", bg="gray"
    )
    eth_ars_label.grid(row=1, column=2)

    usdt_label = tk.Label(
        window, text=f"{usdt.name} ({usdt.nick}):", fg="white", bg="green"
    )
    usdt_label.grid(row=2, column=0)
    usdt_usd_label = tk.Label(
        window, text=f"USD: {usdt.value:,.2f}", fg="white", bg="green"
    )
    usdt_usd_label.grid(row=2, column=1)
    usdt_ars_label = tk.Label(
        window, text=f"ARS: {usdt.value_ars:,.2f}", fg="white", bg="green"
    )
    usdt_ars_label.grid(row=2, column=2)

    # Crear convertidor de monedas
    convert_label = tk.Label(
        window, text="Convertidor de Monedas", fg="black", bg="yellow"
    )
    convert_label.grid(row=3, column=0, columnspan=3, pady="10px")

    amount_label = tk.Label(window, text="Cantidad:", fg="black", bg="yellow")
    amount_label.grid(row=4, column=0)
    amount_entry = tk.Entry(window)
    amount_entry.grid(row=4, column=1)

    from_label = tk.Label(window, text="De:", fg="black", bg="yellow")
    from_label.grid(row=5, column=0)
    from_currency = tk.StringVar()
    from_currency.set("BTC")
    from_menu = tk.OptionMenu(window, from_currency, "BTC", "ETH", "USDT")
    from_menu.grid(row=5, column=1)

    to_label = tk.Label(window, text="A:", fg="black", bg="yellow")
    to_label.grid(row=5, column=2)
    to_currency = tk.StringVar()
    to_currency.set("USD")
    to_menu = tk.OptionMenu(window, to_currency, "USD", "ARS")
    to_menu.grid(row=5, column=3)

    result_label = tk.Label(window, text="Resultado:", fg="black", bg="yellow")
    result_label.grid(row=6, column=0)
    result_value = tk.StringVar()
    result_entry = tk.Entry(window, textvariable=result_value, state="readonly")
    result_entry.grid(row=6, column=1)

    def convert():
        try:
            amount = float(amount_entry.get())
            from_curr = from_currency.get()
            to_curr = to_currency.get()

            # Numero negativo
            if amount < 0:
                raise ValueError("Only positve numbers")

            # Realizar la conversión
            if from_curr == "BTC":
                if to_curr == "USD":
                    result = amount * btc.value
                elif to_curr == "ARS":
                    result = amount * btc.value_ars
            elif from_curr == "ETH":
                if to_curr == "USD":
                    result = amount * eth.value
                elif to_curr == "ARS":
                    result = amount * eth.value_ars
            elif from_curr == "USDT":
                if to_curr == "USD":
                    result = amount * usdt.value
                elif to_curr == "ARS":
                    result = amount * usdt.value_ars

            result_value.set(str(result))
        except ValueError:
            result_value.set("Conversion Invalida")

    convert_button = tk.Button(
        window, text="Convertir", command=convert, fg="black", bg="yellow"
    )
    convert_button.grid(row=7, column=0, columnspan=3)

    # Ejecutar la ventana
    window.mainloop()


# Get rates from COINAPI
def response_crypto(url):
    try:
        headers = {"X-CoinAPI-Key": "70EB5633-A605-4C2B-8385-20C83B8DB841"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanza una excepción si hay un error en la respuesta
        return response.json()["rate"]
    except requests.RequestException:
        return "Datos no disponibles"


# Ger rates ars blue from DOLARAPI
def response_ars():
    try:
        response = requests.get("https://dolarapi.com/v1/dolares/blue")
        response.raise_for_status()  # Lanza una excepción si hay un error en la respuesta
        return response.json()["venta"]
    except requests.RequestException:
        return "Datos no disponibles"


if __name__ == "__main__":
    main()
