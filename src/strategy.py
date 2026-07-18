DantHard-AI-Trading-Bot / src
class Strategy:
    def __init__(self):
        self.name = "DantHard Trading Strategy"

    def decide(self, signal):
        if signal == "BUY":
            return "Enter BUY position"

        elif signal == "SELL":
            return "Enter SELL position"

        else:
            return "Hold position"


if __name__ == "__main__":
    strategy = Strategy()
    print(strategy.decide("BUY"))
