import requests
import tkinter as tk
import customtkinter as ctk

#eur_url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/eur.json"
url = "https://api.exchangerate-api.com/v4/latest/EUR"

class currency_converter():
    currencies = {}
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data["rates"]

    def convertor(self, to_currency, amount):
        amount = round(amount * self.currencies[to_currency], 2)
        return amount


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
appWidth, appHeight = 370, 370

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Euro Converter")
        self.geometry(f"{appWidth}x{appHeight}")

        self.eurLabel = ctk.CTkLabel(self, text="Euro:")
        self.eurLabel.grid(row=0, column=0,padx=20, pady=20,sticky="ew")

        self.eurEntry = ctk.CTkEntry(self, placeholder_text="Enter your amount")
        self.eurEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.currencyLabel = ctk.CTkLabel(self, text="Choose a currency:")
        self.currencyLabel.grid(row=4, column=0, padx=20, pady=2, sticky="ew")

        self.currencyOptionMenu = ctk.CTkOptionMenu(self, values=["USD","TRY", "RUB", "MKD","JPY","CUP","CAD","AZN","IQD"])
        self.currencyOptionMenu.grid(row=4, column=1,padx=20, pady=20,columnspan=2, sticky="ew")

        self.convertButton = ctk.CTkButton(self, text="Convert", command= self.convert_currency)
        self.convertButton.grid(row=5, column=1,columnspan=2,padx=20, pady=20, sticky="ew")

        #self.displayBox = ctk.CTkTextbox(self, width=85, height=85)
        #self.displayBox.grid(row=6, column=0, columnspan=4,padx=20, pady=20, sticky="nsew")

        self.resultLabel = ctk.CTkLabel(self, text=" ",)
        self.resultLabel.grid(row=3, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

    def convert_currency(self):
        try:
            amount = float(self.eurEntry.get())
            to_currency = self.currencyOptionMenu.get()
            result = self.converter.convertor(to_currency, amount)
            #print(result)
            self.resultLabel.configure(text= f"Result: {result} {to_currency}",)
            self.resultLabel.configure(text_color="white", fg_color="#073D54",corner_radius=10, width=200, height=50)
        except ValueError:
            self.resultLabel.configure(text="Please enter a valid amount")
        except KeyError:
            self.resultLabel.configure(text="Please select a valid currency")


    converter = currency_converter(url)

if __name__ == "__main__":
    app = App()
    app.mainloop()