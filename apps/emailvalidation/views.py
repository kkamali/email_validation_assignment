from django.shortcuts import render, redirect
from django.contrib import messages
from . import models

# Create your views here.
def index(request):
    return render(request, 'emailvalidation/index.html')

def submit(request):
    email = request.POST['email']
    validation = models.Email.objects.email_validation(email)
    if (validation):
        query = models.Email(email = email)
        query.save()
        emails = models.Email.objects.all()
        context = {
            'all_emails' : emails,
            'valid_email' : email
            }
        return render(request, "emailvalidation/success.html", context)
    else:
        messages.error(request, 'Not a valid email!')
        return redirect("/")
