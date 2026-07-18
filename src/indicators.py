class Indicators:
    def __init__(self):
        self.name = "Technical Indicators"

    def moving_average(self, prices, period=5):
        if len(prices) < period:
            return None

        return sum(prices[-period:]) / period

    def signal(self, prices):
        average = self.moving_average(prices)

        if average is None:
            return "Not enough data"

        if prices[-1] > average:
            return "BUY"

        elif prices[-1] < average:
            return "SELL"

        return "HOLD"


if __name__ == "__main__":
    indicator = Indicators()
    prices = [100, 105, 110, 108, 115]
    print(indicator.signal(prices))
