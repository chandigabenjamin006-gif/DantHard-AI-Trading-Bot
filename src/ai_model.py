DantHard-AI-Trading-Bot / src
class AIModel:
    def __init__(self):
        self.name = "DantHard AI Prediction Model"

    def predict(self, market_data):
        price = market_data.get("price", 0)

        if price > 30000:
            return "SELL"

        elif price < 10000:
            return "BUY"

        else:
            return "HOLD"


if __name__ == "__main__":
    model = AIModel()

    data = {
        "price": 25000
    }

    print(model.predict(data))
