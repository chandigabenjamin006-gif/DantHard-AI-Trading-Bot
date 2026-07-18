src/main.py
src/data_loader.py
src/indicators.py
src/strategy.py
src/risk_manager.py
src/ai_model.py
src/trading_bot.py
requirements.txt
config.example.json
DantHard-AI-Trading-Bot/
│
├── README.md
├── LICENSE
├── requirements.txt
├── config.example.json
│
└── src/
    ├── main.py
    ├── data_loader.py
    ├── indicators.py
    ├── strategy.py
    ├── risk_manager.py
    ├── ai_model.py
    └── trading_bot.py
  from trading_bot import TradingBot

def main():
    bot = TradingBot()
    bot.start()

if __name__ == "__main__":
    main()
  
