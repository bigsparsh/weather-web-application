import requests
API_KEY = 'edfff301310c966881ff4476669158be'


def get_data(place, days, option):
    url = 'https://api.openweathermap.org/data/2.5/forecast?' \
          f'q={place}&' \
          f'appid={API_KEY}'
    response = requests.get(url)
    content = response.json()
    num_of_hrs = 8 * days
    dates = [i['dt_txt'] for i in content['list'][:num_of_hrs]]
    match option:
        case 'Temperature':
            temperatures = [i['main']['temp'] for i in content['list'][:num_of_hrs]]
            return dates, temperatures
        case 'Sky':
            sky = [i['weather'][0]['main'] for i in content['list'][:num_of_hrs]]
            return dates, sky


if __name__ == '__main__':
    print(get_data('london', 5, 'Temperature'))
