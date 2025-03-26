# 🎮 Clash Royale Strategy Competition - HackStreetBoys

A **Python-based game simulator** for strategic match analysis between competing team algorithms. This project extends the original game engine provided by **WnCC IIT Bombay** for CodeWars V5, implementing headless operation and parallel simulation architecture for computationally efficient strategy optimization.

## 📁 Project Structure

```
.
├── main.py              # Entry point with parallel match simulation implementation
├── game.py              # Modified core game engine implementation
├── matrixCalculation.py # Matrix-based troop counter metrics generation
├── config.py            # Team configuration and simulation parameters
├── teams/              # Strategy implementations for competing algorithms
├── scripts/            # Utility and analysis scripts
└── data/               # Simulation result storage and analytics
```

## ✨ Technical Features

- **Parallel Process Simulation**: Multiprocessing implementation for concurrent match evaluation
- **Counter Matrix Generation**: Numerical analysis of troop effectiveness through time-to-kill metrics
- **Headless Execution**: Optimized runtime through elimination of graphical rendering overhead
- **Detailed Performance Logging**: Comprehensive match data collection for statistical analysis
- **Modular Strategy Interface**: Standardized API for strategy implementation and evaluation

## 🔧 Matrix-Based Counter System

The `matrixCalculation.py` module performs quantitative analysis of troop interaction dynamics:

1. **Counter Factor Calculation**:
   - Generates a 12×12 matrix representing relative effectiveness between all troop type pairs
   - Calculates precise time-to-kill metrics considering:
     - Raw damage per second (damage × attack_speed)
     - Splash damage multipliers for multi-unit engagement
     - Health-to-damage ratios
     - Attack range differentials affecting engagement timing
     - Target type compatibility constraints

2. **Mathematical Model**:
   - For troops that can target each other, the counter factor is calculated as:
     ```
     counter_factor = -1/(time_B_kills_A) + 1/(time_A_kills_B)
     ```
   - For one-sided engagements (e.g., ground troops vs. air troops):
     ```
     counter_factor = -1/time_B_kills_A  # When only B can attack A
     counter_factor = 1/time_A_kills_B   # When only A can attack B
     ```
   - Time-to-kill calculations incorporate range advantages:
     ```
     adjusted_time_to_kill = raw_time_to_kill + range_approach_time
     ```

3. **Output Analysis**:
   - Performs statistical analysis to identify optimal counter relationships
   - Generates `counter_debug.log` with detailed metrics for strategy refinement

## 🎯 Advanced Strategy Implementation in HackStreetBoys.py

The `HackStreetBoys.py` implements a multi-tier decision system for optimal troop deployment:

1. **State Tracking and Analysis**:
   - Maintains a persistent game state through `team_signal` for tracking:
     - Enemy troop composition history
     - Elixir economy estimation
     - Recent deployment patterns
   - Normalizes enemy troop counts based on troop-specific multiplicity factors

2. **Vector-Based Counter Calculation**:
   - Implements matrix multiplication to calculate optimal counter choices:
     ```python
     # Generate normalized enemy composition vector
     opp_troops = np.zeros(12)
     for troop in enemy_troops:
         opp_troops[all_troops.index(troop.name)] += 1 / troop_counts[all_troops.index(troop.name)]
     
     # Matrix multiplication for counter effectiveness scoring
     troop_scores = counters @ opp_troops
     ```
   - This operation performs a weighted dot product between each row of the counter matrix and the current battlefield composition
   - Positive scores indicate effective counters; negative scores indicate unfavorable matchups

3. **Hierarchical Decision System**:
   - Implements a priority-based decision tree:
     - **Priority 1**: Tower defense when enemies are within critical proximity (15 units)
     - **Priority 2**: Strategic push combinations when elixir reserves permit
     - **Priority 3**: Tactical offensive pairs for lane pressure
     - **Priority 4**: Individual counter deployments
     - **Priority 5**: Preemptive deployment when enemy activity is low

4. **Positional Optimization**:
   - Calculates optimal deployment coordinates using the `calculate_best_position` function:
     - Evaluates attack and discovery ranges
     - Considers troop mobility and engagement timing
     - Optimizes for troop-specific advantages (e.g., splash damage positioning)
     - Implements lane-based deployment strategies for coordinated attacks

5. **Elixir Management**:
   - Dynamically adjusts deployment thresholds based on game state
   - Maintains minimum elixir reserves for defensive responses
   - Tracks estimated enemy elixir to identify opportunistic push windows

This multi-tiered approach allows for adaptable strategy execution that responds to battlefield conditions in real-time while maximizing the effectiveness of available troops based on mathematically derived counter relationships.

## 💻 Execution

```bash
python main.py
```

The simulator executes multiple concurrent match instances, aggregating results to evaluate strategy performance across varied scenarios.

## 🙏 Acknowledgments

- **WnCC IIT Bombay** for the original game engine implementation
- This project was developed for the [CodeWars V5: Code Royale](https://tulip-cone-606.notion.site/CodeWars-V5-Code-Royale-1ac881a58b9a807196a5e351b6ea8a79) competition.

---
*Developed by the HackStreetBoys Team* 