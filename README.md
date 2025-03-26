# 🎮 HackStreetboys Game Simulator

A **Python-based game simulator** for running automated matches between different team strategies. This project is built upon the game engine provided by **WnCC IIT Bombay**, which we've modified to run without graphics and added parallel match simulation capabilities for efficient strategy testing.

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

- **Parallel Match Simulation**: Run multiple matches simultaneously for efficient strategy testing
- **Matrix-Based Parameter Generation**: Advanced matrix calculations for optimal troop deployment parameters
- **Headless Operation**: Modified to run without graphics for faster execution
- **Comprehensive Logging**: Detailed debugging logs for strategy analysis
- **Configurable Strategies**: Easy integration of new team strategies

## 🔧 Matrix Calculator

The `matrixCalculation.py` module is a critical component that generates customized parameters for optimal troop deployment in `hackstreetboys.py`. Here's how it works:

1. **Parameter Generation**: 
   - The module calculates counter factors between different troop types using a 12x12 matrix. Each entry in the matrix represents the effectiveness of one troop type against another.
   - Key parameters considered include troop number, health, damage, splash range, attack speed, and type.

2. **Counter Factor Calculation**:
   - For each pair of troops, the module calculates the time required for one troop to kill the other, considering splash damage and attack range.
   - Adjustments are made based on which troop starts attacking first, depending on their attack ranges.

3. **Strategic Analysis**:
   - The module analyzes the counter matrix to determine the best and worst counters for each troop type.
   - Detailed logs are generated in `counter_debug.log`, providing insights into the calculations and strategic recommendations.

## 🎯 Strategy Implementation in HackStreetBoys.py

The `HackStreetBoys.py` file implements the strategy logic for troop deployment. Here's a detailed overview of the `logic` function:

1. **Signal Update**:
   - Updates the `team_signal` to track the state of the game, including enemy troop deployments and elixir levels.

2. **Troop Properties and Counters**:
   - Utilizes a dictionary of troop properties and a counter matrix to evaluate the effectiveness of different troops against enemy troops.

3. **Defense Strategy**:
   - Prioritizes defending the tower by calculating the best counter troops to deploy when enemy troops are close.

4. **Offensive Strategy**:
   - Considers launching a powerful push using predefined troop combinations if conditions are favorable (e.g., sufficient elixir and deployable troops).

5. **Dynamic Deployment**:
   - Adjusts troop deployment dynamically based on the current game state, including enemy troop positions and available elixir.

6. **Fallback Strategies**:
   - Deploys single counter troops or launches a preemptive attack if no specific strategy is applicable and there are no enemy troops.

This strategic approach allows for flexible and effective troop deployment, leveraging the detailed analysis provided by the matrix calculator to optimize performance in matches.

## 💻 Usage


**Run the simulator**:
```bash
python main.py
```

The simulator will run multiple batches of matches between the configured teams and provide results.

## 🙏 Acknowledgments

- **WnCC IIT Bombay** for providing the original game engine
- Thanks to all contributors who have helped shape this project
- Special thanks to the teams who have implemented their strategies
- This project was inspired by the [CodeWars V5: Code Royale](https://tulip-cone-606.notion.site/CodeWars-V5-Code-Royale-1ac881a58b9a807196a5e351b6ea8a79) competition.

---
*Made with ❤️ by the HackStreetboys Team* 