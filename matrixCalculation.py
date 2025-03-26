from helper_function import Troops, Utils
import numpy
import decimal
import math
import os
# Create a debug log file
debug_file = "counter_debug.log"
with open(debug_file, "w") as f:
    f.write("Counter Matrix Debug Log\n")
    f.write("=" * 50 + "\n\n")

def write_debug(message):
    with open(debug_file, "a") as f:
        f.write(message + "\n")


troops = Troops.troops_data.values()

def calculate_counter_factor(troopA, troopB):
    # Get properties for both troops
    num_A = troopA.number
    num_B = troopB.number
    health_A = troopA.health
    health_B = troopB.health
    damage_A = troopA.damage
    damage_B = troopB.damage
    has_splash_A = troopA.splash_range > 0
    has_splash_B = troopB.splash_range > 0
    attack_speed_A = 1/troopA.attack_speed
    attack_speed_B = 1/troopB.attack_speed
    typeA = troopA.type
    typeB = troopB.type
    
    write_debug(f"\nDetailed calculation for {troopA.name} vs {troopB.name}:")
    write_debug(f"Troop A ({troopA.name}):")
    write_debug(f"  Number: {num_A}")
    write_debug(f"  Health: {health_A}")
    write_debug(f"  Damage: {damage_A}")
    write_debug(f"  Has splash: {has_splash_A}")
    write_debug(f"  Attack speed: {attack_speed_A}")
    write_debug(f"Troop B ({troopB.name}):")
    write_debug(f"  Number: {num_B}")
    write_debug(f"  Health: {health_B}")
    write_debug(f"  Damage: {damage_B}")
    write_debug(f"  Has splash: {has_splash_B}")
    write_debug(f"  Attack speed: {attack_speed_B}")
    
    # Calculate hits needed based on splash and health/damage ratios
    if has_splash_A:
        # If A has splash, calculate how many hits to kill all B units at once
        hits_A_to_kill_B = math.ceil(health_B / damage_A)/num_A
        write_debug(f"  Hits A needs to kill B (with splash): {hits_A_to_kill_B}")
    else:
        # If A doesn't have splash, calculate hits to kill each B unit individually
        hits_per_unit_B = math.ceil(health_B / damage_A)
        hits_A_to_kill_B = hits_per_unit_B * num_B/num_A
        write_debug(f"  Hits per unit B: {hits_per_unit_B}")
        write_debug(f"  Total hits A needs to kill B: {hits_A_to_kill_B}")
    
    if has_splash_B:
        # If B has splash, calculate how many hits to kill all A units at once
        hits_B_to_kill_A = math.ceil(health_A / damage_B)/num_B
        write_debug(f"  Hits B needs to kill A (with splash): {hits_B_to_kill_A}")
    else:
        # If B doesn't have splash, calculate hits to kill each A unit individually
        hits_per_unit_A = math.ceil(health_A / damage_B)
        hits_B_to_kill_A = hits_per_unit_A * num_A/num_B
        write_debug(f"  Hits per unit A: {hits_per_unit_A}")
        write_debug(f"  Total hits B needs to kill A: {hits_B_to_kill_A}")
    
    # Calculate time to kill
    time_A_to_kill_B = hits_A_to_kill_B / attack_speed_A
    time_B_to_kill_A = hits_B_to_kill_A / attack_speed_B
    write_debug(f"  Time A to kill B: {time_A_to_kill_B}")
    write_debug(f"  Time B to kill A: {time_B_to_kill_A}")
    
    # Only calculate time to reach if both troops can attack each other
    if troopB.target_type[typeA] and troopA.target_type[typeB]:
        if troopA.attack_range > troopB.attack_range:
            isBfar = 1
            isAfar = 0
            timetoreach = (troopA.attack_range - troopB.attack_range) / troopB.speed
            write_debug(f"  A has longer range, time to reach: {timetoreach}")
        elif troopA.attack_range < troopB.attack_range:
            isBfar = 0
            isAfar = 1
            timetoreach = (troopB.attack_range - troopA.attack_range) / troopA.speed
            write_debug(f"  B has longer range, time to reach: {timetoreach}")
        else: 
            isBfar = 0
            isAfar = 0
            timetoreach = 0
            write_debug("  Equal ranges, no time to reach")
        
        # Adjust time to kill based on who starts attacking first
        if isAfar:
            # B starts attacking first
            adjusted_time_A_to_kill_B = time_A_to_kill_B + timetoreach
            adjusted_time_B_to_kill_A = time_B_to_kill_A
            write_debug("  B starts attacking first")
        elif isBfar:
            # A starts attacking first
            adjusted_time_A_to_kill_B = time_A_to_kill_B
            adjusted_time_B_to_kill_A = time_B_to_kill_A + timetoreach
            write_debug("  A starts attacking first")
        else:
            # Both start attacking simultaneously
            adjusted_time_A_to_kill_B = time_A_to_kill_B
            adjusted_time_B_to_kill_A = time_B_to_kill_A
            write_debug("  Both start attacking simultaneously")
    else:
        # If either troop cannot attack the other, no time to reach adjustment needed
        adjusted_time_A_to_kill_B = time_A_to_kill_B
        adjusted_time_B_to_kill_A = time_B_to_kill_A
        write_debug("  No time to reach adjustment - one troop cannot attack the other")
    
    write_debug(f"  Final adjusted times:")
    write_debug(f"    A to kill B: {adjusted_time_A_to_kill_B}")
    write_debug(f"    B to kill A: {adjusted_time_B_to_kill_A}")
    
    return adjusted_time_A_to_kill_B, adjusted_time_B_to_kill_A


counter = numpy.zeros((12,12))
max_threshold = 1000000000000000
countA = 0
for troopA in sorted(Troops.troops_data.values(), key=lambda x: x.name):
    countB = 0
    typeA = troopA.type
    for troopB in sorted(Troops.troops_data.values(), key=lambda x: x.name):
        typeB = troopB.type      
        decimal.getcontext().prec = 3
        
        # Get adjusted time to kill values
        time_A_kills_B, time_B_kills_A = calculate_counter_factor(troopA, troopB)
        if (time_A_kills_B == 0): time_A_kills_B = max_threshold
        if (time_B_kills_A == 0): time_B_kills_A = max_threshold
        
        # Use the correct counter factor calculation based on who can attack whom
        if troopB.target_type[typeA] and troopA.target_type[typeB]: 
            # Both can attack each other - counter is difference in kill times
            counter_factor = -1/(time_B_kills_A) + 1/(time_A_kills_B)
            write_debug(f"Both {troopA.name} and {troopB.name} can attack each other so counter is {counter_factor}")
        elif troopB.target_type[typeA] and not troopA.target_type[typeB]:
            counter_factor = -1/time_B_kills_A
            write_debug(f"Enemy {troopB.name} can attack {troopA.name} but our {troopA.name} cannot attack {troopB.name} so counter is {counter_factor}")
            # B can attack A but A cannot attack B - counter is just time B takes to kill A
        elif not troopB.target_type[typeA] and troopA.target_type[typeB]:
            counter_factor = 1/time_A_kills_B
            write_debug(f"Our {troopA.name} can attack {troopB.name} but enemy {troopB.name} cannot attack {troopA.name} so counter is {counter_factor}")
            # A can attack B but B cannot attack A - counter is negative of time A takes to kill B
        else:
            # Neither can attack the other
            counter_factor = 0
            write_debug(f"Neither {troopA.name} nor {troopB.name} can attack each other")
        
        # Keep the decimal conversion
        counter_factor = decimal.Decimal(counter_factor)
        counter[countA][countB] = counter_factor
        countB += 1
    countA += 1

# Write the final counter matrix to the debug file
write_debug("\nFinal Counter Matrix:")
write_debug(str(counter.view()))

# Analyze the counter matrix for strategic insights
write_debug("\nStrategic Analysis:")
write_debug("=" * 50)

# Find strongest counters for each troop
for i, troopA in enumerate(sorted(Troops.troops_data.values(), key=lambda x: x.name)):
    best_counter = None
    best_counter_value = float('-inf')
    worst_counter = None
    worst_counter_value = float('inf')
    
    for j, troopB in enumerate(sorted(Troops.troops_data.values(), key=lambda x: x.name)):
        counter_value = float(counter[j][i])
        if counter_value > best_counter_value:
            best_counter_value = counter_value
            best_counter = troopB.name
        if counter_value < worst_counter_value:
            worst_counter_value = counter_value
            worst_counter = troopB.name
    
    write_debug(f"\n{troopA.name}:")
    write_debug(f"  Best counter: {best_counter} ({best_counter_value:.3f})")
    write_debug(f"  Worst counter: {worst_counter} ({worst_counter_value:.3f})")

print(f"Debug output has been written to {debug_file}")

