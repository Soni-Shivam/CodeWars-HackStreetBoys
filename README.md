# 🎮 HackStreetboys Game Simulator

A **Python-based game simulator** for running automated matches between different team strategies. This project provides a framework for simulating and analyzing game outcomes between different teams using their custom strategies.

## 📁 Project Structure

```
.
├── main.py              # Main entry point for running simulations
├── game.py             # Core game logic implementation
├── matrixCalculation.py # Matrix-based calculations for game mechanics
├── config.py           # Configuration settings and team imports
├── teams/              # Directory containing team strategy implementations
├── scripts/            # Utility scripts and tools
└── data/              # Data storage directory
```

## ✨ Features

- **Automated Match Simulation**: Run matches between different team strategies
- **Batch Processing**: Execute multiple matches in batches
- **Matrix Calculations**: Advanced matrix-based game mechanics
- **Configurable Strategies**: Easy integration of new team strategies
- **Comprehensive Logging**: Detailed debugging and analysis capabilities

## 🔧 Prerequisites

- **Python 3.x**
- Required Python packages (to be listed in requirements.txt)

## 🚀 Setup

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/HackStreetboys.git
cd HackStreetboys
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. **Configure your teams** in the `config.py` file:
```python
from teams import your_team1, your_team2

TEAM1 = your_team1
TEAM2 = your_team2
```

2. **Run the simulator**:
```bash
python main.py
```

The simulator will run multiple batches of matches between the configured teams and provide results.

## 🎯 Team Strategy Implementation

To implement a new team strategy:

1. Create a new Python file in the `teams/` directory
2. Implement the required interface:
   - `team_name`: Your team's name
   - `troops`: Your team's troop configuration
   - `deploy_list`: Your deployment strategy
   - `team_signal`: Your team's signal handling

## ⚙️ Configuration

Key configuration options in `config.py`:
- `TEAM1`: First team's strategy
- `TEAM2`: Second team's strategy
- `VALUE_ERROR`: Error handling flag

## 📝 Logging

The simulator generates detailed logs in `counter_debug.log` for debugging and analysis purposes.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape this project
- Special thanks to the teams who have implemented their strategies

---
*Made with ❤️ by the HackStreetboys Team* 