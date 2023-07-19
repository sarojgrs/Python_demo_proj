from twilio.rest import Client
# Define command classes for each intent


class GreetCommand:
    def execute(self):
        return "Hello! How can I assist you?"


class WeatherCommand:
    def execute(self, location):
        # Your code to fetch and return the weather information for the specified location
        return f"The weather in {location} is sunny."

# Add more command classes as needed for other commands
# Define command classes for each intent


class GreetCommand:
    def execute(self):
        return "Hello! How can I assist you?"


class WeatherCommand:
    def execute(self, location):
        # Your code to fetch and return the weather information for the specified location
        return f"The weather in {location} is sunny."

# Add more command classes as needed for other commands
