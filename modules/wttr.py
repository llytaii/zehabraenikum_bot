import requests

def forecast(locations):
    locations = locations.split()
    pngs = []

    if len(locations) == 0:
        locations.append('weilheim')

    for location in locations:
        response = requests.get('http://v2.wttr.in/' + location + '.png')
        if response.status_code == 200:
            png = response.content
            pngs.append(png)

    return pngs

