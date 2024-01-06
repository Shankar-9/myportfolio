from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .models import *
def home(request):
    ska1=skills.objects.all()
    pro1=projects.objects.all()
    jur1=Journey.objects.all()
    expirience1=Journey1.objects.all()
    return render(request, 'index.html', {'project':pro1, 'journey':jur1, 'skill_nam':ska1,  'journey1':expirience1})
def aboutme(request):
    return render(request, 'aboutme.html')
def contact(request):
    return render(request, 'contact.html')
def projects1(request):
    project=projects.objects.all()
    return render(request, 'projects.html',{"project":project})
def skills1(request):
    return render(request, 'skills.html')
def journey(request):
    jur2=Journey.objects.all()
    expirience=Journey1.objects.all()
    return render(request, 'journey.html', {"journey":jur2, 'journey1':expirience})

def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        subject1 = request.POST['subject']
        message1 = request.POST['message']
        
        
        subject = 'This is a mail from Portfolio'
        message = f'''
        Someone want to contact you : 
        Name: {name}
        Email: {email}
        Mobile: {mobile}
        Subject: {subject1}
        Message: {message1}
        '''
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['palaganigowrishankar8@gmail.com']

        try:
            send_mail(subject, message, email_from, recipient_list)
        except Exception as e:
            # Handle email sending errors here (e.g., log the error or return an error response)
            return render(request, 'error.html', {'error_message': str(e)})

        return render(request, 'contact.html')

       
        
    

# Create your views here.
