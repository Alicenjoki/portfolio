from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        
        send_mail(
            name, #title
            message, #message
            email,
            ['njokialice503@gmail.com'],
            # 'settings.EMAIL_HOST_USER', 
            fail_silently=False
        )

        return render(request, 'pages/home.html', {'name':name} )
    else:
        return render(request, 'pages/home.html')
        
        
    

def about(request):
    return render(request, 'pages/home.html')
