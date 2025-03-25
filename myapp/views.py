from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def services(request):
    return render(request,'services.html')
def about(request):
    return render(request,'about.html')
def privacy(request):
    return render(request,'privacy.html')
def terms(request):
    return render(request,'terms.html')
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Contact
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact = form.save()

            # Send email to HR
            send_mail(
                subject=f"New Consultation Request from {contact.fullname}",
                message=f"""
                Name: {contact.fullname}
                Email: {contact.email}
                Company: {contact.company}
                Phone: {contact.phone}
                Message: {contact.message}
                """,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['achalsultane855@gmail.com'],  # Replace with HR email
                fail_silently=False,
            )

            # Redirect to the same page with a success message
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

