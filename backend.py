import requests

API_KEY = "3aad2a1b33c9b8f18b324bfb35919066"
def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place='Tokyo', forecast_days=3))
# http://api.openweathermap.org/data/2.5/forecast?q={city name}&appid=3aad2a1b33c9b8f18b324bfb35919066
