# Inputs for the traffic light system
color = input("Enter traffic light color (red, yellow, green): ").strip().lower()
speed = float(input("Enter your current speed (in km/h): "))

print("\n--- System Action ---")
# Structural match-case with a guard condition
match color:
    case 'red':
        print("STOP! Do not pass.")
        
    case 'yellow':
        print("PREPARE TO STOP: Clearance interval running.")
        
    case 'green' if speed > 60:
        # This guard condition intercepts green signals if speed is too high
        print("CAUTION: Slow down even on green! You are exceeding 60 km/h.")
        
    case 'green':
        # This handles green signals for normal speeds
        print("GO: Proceed with caution.")
        
    case _:
        print("ERROR: Invalid traffic light color pattern detected.")