# from django.shortcuts import render,redirect
# from .forms import EmailForm
# from django.template.loader import render_to_string
# from django.conf import settings
# from django.core.mail import send_mail


# # Create your views here.
# def EmailView(request):
#     if request.POST:
#         form=EmailForm(request.POST)

#         if form.is_valid():
#             name=(form.cleaned_data['name'])
#             email=(form.cleaned_data['email'])
#             content=(form.cleaned_data['message'])


#             send_mail(name,content,settings.EMAIL_HOST_USER,[email],fail_silently=False)

#             return redirect('emailsend:email')
#     else:        
#      form=EmailForm()

#     return render(request,'emailsend/home.html',{
#         'form':form
#     })

from django.core.mail import get_connection, send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import EmailForm

def EmailView(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['message']

            # Establish a connection to the SMTP server
            connection = get_connection(
                'django.core.mail.backends.smtp.EmailBackend',
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                fail_silently=False,
            )

            try:
                # Open the connection
                connection.open()

                # Send the email using the established connection
                send_mail(
                    name,
                    content,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                    connection=connection,
                )
            finally:
                # Close the connection after sending the email
                connection.close()

            return redirect('emailsend:email')

    else:
        form = EmailForm()

    return render(request, 'emailsend/home.html', {'form': form})
