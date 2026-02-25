task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip()
time_bound = input("Is it time-bound? (yes/no): ").strip()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: \'{task}\' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: \'{task}\' is a high priority task. Consider completing it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: \'{task}\' is a medium priority task that should be completed today.")
        else:
            print(f"Note: \'{task}\' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: \'{task}\' is a low priority taskt that should be completed today.")
        else:
            print(f"Note: \'{task}\' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")