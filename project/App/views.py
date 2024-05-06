from django.shortcuts import render, redirect
import requests
import csv
from django.http import HttpResponse
from .models import Satellite, LaunchCountry


# def fetch_satellite_data():
#     satellite_names = ['intelsat', 'iridium', 'starlink', 'orbcomm', 'swarm', 'satnogs', 'ses', 'oneweb', 'globalstar', 'amateur']
#     satellite_data = []

#     for satellite in satellite_names:
#         url = f'https://celestrak.org/NORAD/elements/gp.php?GROUP={satellite}&FORMAT=json'
#         response = requests.get(url)
#         if response.status_code == 200:
#             satellite_data.extend(response.json()[:30])  # Take 30 entries from each website

#     return satellite_data

# def fetch_launch_countries():
#     satellite_countries = {
#         'Intelsat': 'USA',
#         'Iridium': 'USA',
#         'Starlink': 'USA',
#         'Orbcomm': 'USA',
#         'Swarm': 'USA',
#         'SatNogs': 'USA',
#         'SES': 'USA',
#         'Oneweb': 'UK',
#         'globalstar': 'USA',
#         'amateur': 'Various',
#     }
    
#     launch_data = [{'satellite_name': name, 'launch_country': country} for name, country in satellite_countries.items() for _ in range(10)]

#     return launch_data

# def home(request):
#     # Fetch satellite data and save to database
#     satellite_data = fetch_satellite_data()
#     for data in satellite_data:
#         Satellite.objects.create(**data)

#     # Fetch launch country data and save to database
#     launch_data = fetch_launch_countries()
#     for data in launch_data:
#         LaunchCountry.objects.create(**data)

#     # Retrieve data from database
#     satellites = Satellite.objects.all()[:30]  # Fetching 30 entries
#     launch_countries = LaunchCountry.objects.all()[:100]  # Fetching 100 entries

#     return render(request, 'home.html', {'satellites': satellites, 'launch_countries': launch_countries})



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
    # return render(request, 'home.html', {'satellite_data': satellite_data, 'launch_data': launch_data})






    # Generating CSV data
    csv_data = [['OBJECT_NAME', 'OBJECT_ID', 'EPOCH', 'MEAN_MOTION', 'ECCENTRICITY', 'INCLINATION', 'RA_OF_ASC_NODE', 'ARG_OF_PERICENTER', 'MEAN_ANOMALY', 'EPHEMERIS_TYPE', 'CLASSIFICATION_TYPE', 'NORAD_CAT_ID', 'ELEMENT_SET_NO', 'REV_AT_EPOCH', 'BSTAR', 'MEAN_MOTION_DOT', 'MEAN_MOTION_DDOT']]
    for entry in satellite_data:
        csv_data.append([
            entry['OBJECT_NAME'],
            entry['OBJECT_ID'],
            entry['EPOCH'],
            entry['MEAN_MOTION'],
            entry['ECCENTRICITY'],
            entry['INCLINATION'],
            entry['RA_OF_ASC_NODE'],
            entry['ARG_OF_PERICENTER'],
            entry['MEAN_ANOMALY'],
            entry['EPHEMERIS_TYPE'],
            entry['CLASSIFICATION_TYPE'],
            entry['NORAD_CAT_ID'],
            entry['ELEMENT_SET_NO'],
            entry['REV_AT_EPOCH'],
            entry['BSTAR'],
            entry['MEAN_MOTION_DOT'],
            entry['MEAN_MOTION_DDOT']
        ])

    # Create HTTP response with CSV file- Uncomment below lines to download csv on visiting homepage
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="satellite_data.csv"'
    # writer = csv.writer(response)
    # writer.writerows(csv_data)

    # return response


    return render(request, 'home.html', {'satellite_data': satellite_data, 'launch_data': launch_data})





