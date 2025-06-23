# 1. Model-View-Controller (MVC)
"The MVC pattern separates your application into three components:"
"Model: Manages data and business logic"
"View: Handles presentation and user interface"
"Controller: Manages user input and coordinates Model/View"
# # Model
class WeatherModel:
    def __init__(self):
        self.current_weather = {}
        self.history = []
    
    def update_weather(self, city):
        # Fetch and store weather data
        pass
    
    def get_weather(self):
        return self.current_weather

# View
class WeatherView:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
    
    def display_weather(self, weather_data):
        # Update GUI with weather data
        pass
    
    def get_city_input(self):
        return self.city_entry.get()

# Controller
class WeatherController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.search_button.config(command=self.fetch_weather)
    
    def fetch_weather(self):
        city = self.view.get_city_input()
        self.model.update_weather(city)
        weather = self.model.get_weather()
        self.view.display_weather(weather)




# 2. Layered Architecture
"Organize your application into layers, each with specific responsibilities:"
# ┌─────────────────────────────┐
# │    Presentation Layer       │  (GUI components)
# ├─────────────────────────────┤
# │    Business Logic Layer     │  (Weather processing)
# ├─────────────────────────────┤
# │    Data Access Layer        │  (API, File I/O)
# └─────────────────────────────┘
