# Question 01:
# model-based reflex agent
class ModelReflexAgent:
    def __init__(self, temp):
        self.desired_temp = temp
        self.last_action = None
        self.current_temp = None

    def perceive(self, current_temp):
        self.current_temp = current_temp
        return current_temp
        
    def actuators(self, current_temp):
        self.perceive(current_temp)
        if current_temp < self.desired_temp:
            if not self.last_action:
                return "Turn on heater"
            else:
                return "Maintain current state"
        elif current_temp > self.desired_temp:
            if self.last_action:
                return "Turn off heater"
            else:
                return "Maintain current state"
        else:
            return "Maintain current state"

def main():
    rooms = {
        "Living Room": 18,
        "Bedroom": 22,
        "Kitchen": 20,
        "Bathroom": 24
    }
    desired_temp = 22
    agent = ModelReflexAgent(desired_temp)
    for room, temp in rooms.items():
        action = agent.actuators(temp)
        print(f"{room}: Current temp ===> {temp}°C. ===> {action}.")
        # Update heater for room temperature
        agent.last_action = action.startswith("Turn")

if __name__ == "__main__":
    main()
