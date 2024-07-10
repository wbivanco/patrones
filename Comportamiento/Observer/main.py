"""3. Implementa la lógica del ejemplo."""


from subject import WeatherStation
from observer import TemperaturDisplay  

def main():
    weather_station = WeatherStation()
    temperature_display = TemperaturDisplay()
    
    weather_station.register_observer(temperature_display)
    
    weather_station.set_temperature(25)
    weather_station.set_temperature(30)
    weather_station.set_temperature(35)

if __name__ == "__main__":
    main()