from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import os
from django.http import FileResponse, Http404

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'New message from portfolio site'
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            try:
                send_mail(subject, full_message, email, ["janbandhukunal47@gmail.com"], fail_silently=False)
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, f"Error sending message: {e}")
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})

def download_resume(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'Kunal_Janbandhu_Resume.pdf')
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Kunal_Janbandhu_Resume.pdf')
        return response
    else:
        raise Http404('Resume not found') 