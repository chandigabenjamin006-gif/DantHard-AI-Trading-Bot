from data_loader import DataLoader
from indicators import Indicators
from strategy import Strategy
from risk_manager import RiskManager


def run_backtest():
    # Initialize modules
    loader = DataLoader()
    indicators = Indicators()
    strategy = Strategy()
    risk_manager = RiskManager()

    balance = 1000

    # Simulated historical prices
    prices = [100, 105, 110, 108, 115]

    # Generate signal
    signal = indicators.signal(prices)

    # Make trading decision
    decision = strategy.decide(signal)

    # Current price
    price = prices[-1]

    # Calculate position size
    position_size = risk_manager.calculate_position_size(
        balance,
        price
    )

    # Display results
    print("Market:", loader.market)
    print("Current Price:", price)
    print("Signal:", signal)
    print("Decision:", decision)
    print("Position Size:", position_size)


if __name__ == "__main__":
    run_backtest()
