DantHard-AI-Trading-Bot / src
class RiskManager:
    def __init__(self, risk_percentage=2):
        self.risk_percentage = risk_percentage

    def calculate_position_size(self, balance, price):
        risk_amount = balance * (self.risk_percentage / 100)
        
        if price == 0:
            return 0
            
        return round(risk_amount / price, 6)


if __name__ == "__main__":
    manager = RiskManager()
    size = manager.calculate_position_size(1000, 50000)
    print("Position size:", size)
