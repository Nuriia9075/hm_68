from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def get_numbers(numbers):
    a = numbers.get('A')
    b = numbers.get('B')
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
       return [a,b]
    else:
        return None

@csrf_exempt
def add(request, *args, **kwargs):
    if request.method == 'POST':
        numbers = json.loads(request.body)
        values = get_numbers(numbers)
        if values is not None:
            return JsonResponse({'answer': values[0]+ values[1]}, status= 200)
        return JsonResponse({'error': "enter a number"}, status= 400)

@csrf_exempt
def subtract(request, *args, **kwargs):
    if request.method == 'POST':
        numbers = json.loads(request.body)
        values = get_numbers(numbers)
        if values is not None:
            return JsonResponse({'answer': values[0] - values[1]}, status=200)
        return JsonResponse({'error': "enter a number"}, status=400)

@csrf_exempt
def multiply(request, *args, **kwargs):
    if request.method == 'POST':
        numbers = json.loads(request.body)
        values = get_numbers(numbers)
        if values is not None:
            return JsonResponse({'answer': values[0] * values[1]}, status=200)
    return JsonResponse({'error': "enter a number"}, status=400)

@csrf_exempt
def divide(request, *args, **kwargs):
    if request.method == 'POST':
        numbers = json.loads(request.body)
        values = get_numbers(numbers)
        if values is not None:
            if values[1] == 0:
                return JsonResponse({'error': "you can't divide by zero"}, status=400)
            return JsonResponse({'answer': values[0] / values[1]}, status=200)
    return JsonResponse({'error': "enter a number"}, status=400)

