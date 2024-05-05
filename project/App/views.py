from django.shortcuts import render
import requests


# def home(request):
#     # List of satellite names
#     satellite_names = ['Intelsat', 'Iridium', 'Starlink', 'Orbcomm', 'Swarm', 'SatNogs', 'SES', 'Oneweb', 'globalstar', 'amateur']

#     satellite_data = []

#     # Iterate through each satellite name and fetch 30 satellite data entries from each website
#     for satellite in satellite_names:
#         url = f'https://celestrak.org/NORAD/elements/gp.php?GROUP={satellite}&FORMAT=json'
#         response = requests.get(url)
#         if response.status_code == 200:
#             satellite_data.extend(response.json()[:70])

#     return render(request, 'home.html', {'satellite_data': satellite_data})


from django.shortcuts import render
import requests

def home(request):
    # List of satellite names and their launch countries (dummy data)
    satellite_countries = {
        'intelsat': 'USA',
        'iridium': 'USA',
        'starlink': 'USA',
        'orbcomm': 'USA',
        'swarm': 'USA',
        'satnogs': 'USA',
        'ses': 'USA',
        'oneweb': 'UK',
        'globalstar': 'USA',
        'amateur': 'Various',
    }

    # Fetching 30 entries for the first table
    satellite_data = []
    satellite_names = list(satellite_countries.keys())

    for satellite in satellite_names:
        url = f'https://celestrak.org/NORAD/elements/gp.php?GROUP={satellite}&FORMAT=json'
        response = requests.get(url)
        if response.status_code == 200:
            satellite_data.extend(response.json()[:70])  # Take 10 entries from each website

    # Generating dummy data for the second table
    launch_data = [{'name': name, 'country': country} for name, country in satellite_countries.items()]
    return render(request, 'home.html', {'satellite_data': satellite_data, 'launch_data': launch_data})

