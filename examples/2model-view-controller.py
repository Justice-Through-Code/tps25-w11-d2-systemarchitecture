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


# Core Architecture Structure
class WeatherDashboard:
    def __init__(self):
        # Initialize layers
        self.data_layer = DataLayer()
        self.business_layer = BusinessLayer(self.data_layer)
        self.presentation_layer = PresentationLayer(self.business_layer)
        
        # Initialize features
        self.features = {}
        self.load_features()
    
    def load_features(self):
        # Dynamically load selected features
        if "history" in self.selected_features:
            from features.history import HistoryFeature
            self.features['history'] = HistoryFeature(self.business_layer)

class DataLayer:
    def __init__(self):
        self.api_client = WeatherAPIClient()
        self.file_manager = FileManager()
    
    def fetch_weather(self, city):
        return self.api_client.get_weather(city)
    
    def save_weather(self, weather_data):
        self.file_manager.save(weather_data)

class BusinessLayer:
    def __init__(self, data_layer):
        self.data_layer = data_layer
    
    def get_weather_for_city(self, city):
        raw_data = self.data_layer.fetch_weather(city)
        processed_data = self.process_weather_data(raw_data)
        self.data_layer.save_weather(processed_data)
        return processed_data
    
    def process_weather_data(self, raw_data):
        # Convert, validate, enhance data
        pass

class PresentationLayer:
    def __init__(self, business_layer):
        self.business_layer = business_layer
        self.main_window = MainWindow()
        self.setup_ui()
