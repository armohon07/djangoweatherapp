from django.shortcuts import render

def home(request):
	import json
	import requests

	api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=93932&distance=25&API_KEY=7627CAAC-A7AF-45D1-B4A2-F64CD7001B41')

	try: 
		api = json.loads(api_request.content)
	except Exception as e:
		api = 'Error...'

	if api[0]['Category']['Name'] == 'Good':
		category_description = 'Enjoy your outdoor activities.'
		category_color = 'good'

	elif api[0]['Category']['Name'] == 'Moderate':
		category_description = 'If you are unusually sensitive to particle pollution, consider reducing your activity level or shorten the amount of time you are active outdoors.'
		category_color = 'moderate'

	return render(request, 'home.html', {'api': api, "category_description": category_description, 'category_color': category_color })


def about(request):
	return render(request, 'about.html', {})