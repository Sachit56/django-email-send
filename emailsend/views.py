from django.shortcuts import render,redirect
from .forms import EmailForm
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def EmailView(request):
    if request.POST:
        form=EmailForm(request.POST)

        if form.is_valid():
            name=(form.cleaned_data['name'])
            email=(form.cleaned_data['email'])
            content=(form.cleaned_data['message'])


            send_mail(name,content,settings.EMAIL_HOST_USER,[email],fail_silently=False)

            return redirect('emailsend:email')
    else:        
     form=EmailForm()

    return render(request,'emailsend/home.html',{
        'form':form
    })