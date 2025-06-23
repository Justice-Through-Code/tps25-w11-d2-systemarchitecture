# W11D2 In class examples - how to set up your code
import requests



# 1. Separation of Concerns
"Each component should have one clear responsibility:"
# BAD: Everything mixed together
class WeatherApp:
    def get_weather_and_display(self, city):
        # API call
        response = requests.get(f"http://api.weather.com/{city}")
        data = response.json()
        
        # Processing
        temp = data['temp'] * 1.8 + 32  # Convert to F
        
        # Display
        self.label.config(text=f"{temp}°F")
        
        # Save
        with open("data.txt", "a") as f:
            f.write(f"{city},{temp}\n")

# GOOD: Separated concerns
class WeatherAPI:
    def fetch_weather(self, city):
        response = requests.get(f"http://api.weather.com/{city}")
        return response.json()

class WeatherProcessor:
    def convert_temperature(self, celsius):
        return celsius * 1.8 + 32

class WeatherStorage:
    def save_weather(self, city, temp):
        with open("data.txt", "a") as f:
            f.write(f"{city},{temp}\n")

class WeatherGUI:
    def display_temperature(self, temp):
        self.label.config(text=f"{temp}°F")


# 2. Modularity
"Break your system into independent, interchangeable modules."



# 3. Low Coupling, High Cohesion
"Components should be independent (low coupling) but internally focused (high cohesion):"
# High Coupling (BAD)
class WeatherGraph:
    def __init__(self, weather_app):
        self.app = weather_app  # Depends on entire app
        self.data = weather_app.storage.data
        self.api = weather_app.api_handler
        
# Low Coupling (GOOD)
class WeatherGraph:
    def __init__(self, data_source):
        self.data_source = data_source  # Only depends on data interface
    
    def plot_temperatures(self, temperature_data):
        # Works with any data that matches expected format
        pass

