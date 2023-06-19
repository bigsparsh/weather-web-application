import requests
API_KEY = 'edfff301310c966881ff4476669158be'


def get_data(place, days, option):
    url = 'https://api.openweathermap.org/data/2.5/forecast?' \
          f'q={place}&' \
          f'appid={API_KEY}'
    response = requests.get(url)
    content = response.json()
    match option:
        case 'Temperature':
            num_of_hrs = 8 * days
            temperatures = [i['main']['temp'] for i in content['list'][:num_of_hrs]]
            return temperatures
        # case 'Sky':


if __name__ == '__main__':
    print(get_data('london', 5, 'Temperature'))
