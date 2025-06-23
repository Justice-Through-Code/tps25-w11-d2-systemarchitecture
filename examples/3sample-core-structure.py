import FileManager
import WeatherAPIClient
import MainWindow


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
