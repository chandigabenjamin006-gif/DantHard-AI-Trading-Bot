import random

class DataLoader:
    def __init__(self):
        self.market = "Crypto Market"

    def get_data(self):
        price = random.uniform(100, 50000)

        return {
            "market": self.market,
            "price": round(price, 2)
        }


if __name__ == "__main__":
    data = DataLoader()
    print(data.get_data())
  indicators.py
