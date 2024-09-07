from django.shortcuts import render
from django.http import HttpResponse
from .models import coffee
def home(request):
    coffee_l = coffee.objects.all()
    return render(request, 'welcome.html', {'coffee_l':coffee_l})


def home2(request):
    coffee_l = coffee.objects.all()
    return render(request, 'home.html', {'coffee_l':coffee_l})

def logout(request):
    return render(request, 'welcome.html')


def about(request):
    return render(request, 'about.html')    


def contact(request):
    return render(request, 'contact.html')    

def message(request):
    return render(request,'message.html')    




    from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def handle_action(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        action = data.get('action')

        # Process the action here (e.g., save to database)
        # You can use action to decide what to do
        
        # Example response
        response_data = {
            'status': 'success',
            'message': f'{action} action processed'
        }
        return JsonResponse(response_data)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
