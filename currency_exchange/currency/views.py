from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import requests
import time


API_URL = 'https://api.exchangerate-api.com/v4/latest/USD'
REQUESTS_LIMIT = 10
REQUESTS_INTERVAL = 10

recent_requests = []

@csrf_exempt
@require_http_methods(['GET'])
def get_current_usd(request):
    global recent_requests
    if len(recent_requests) >= REQUESTS_LIMIT:
        recent_requests.pop[0]
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        current_rate = data['rates']['RUB']
        recent_requests.append(current_rate)
        time.sleep(REQUESTS_INTERVAL)

        return JsonResponse({'current_rates_to_rub': current_rate, "recent_requests": recent_requests})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
