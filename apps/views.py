import os.path
from email.message import EmailMessage

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User,auth
# Create your views here.

def regmail(request):
    context= {}

    if request.method=="POST":
        username=request.POST.get("username")
        mail=request.POST.get("email")
        password=request.POST.get("password")
        subject="welcome to fadedstore"
        message="hi,thankyou for registering with us !"



        if mail :
            try:
                # email = EmailMessage(subject,message,settings.EMAIL_HOST_USER,[mail])
                # image_path = os.path.join(settings.BASE_DIR, 'media', 'ben.jpg')
                # email.attach_file(image_path)
                # email.send()
                send_mail(subject,message,settings.EMAIL_HOST_USER,[mail])
                context['result']='email send succsessfully'
                return redirect("loginpage")
            except Exception as e:
                context['result']=f'error sending mail {e}'
        else:
            context['result']="all fields are required"

    return render(request,'regemail.html',context)


def logu(request):
    return render(request,'loginpage.html')
