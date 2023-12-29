from django.core.mail import get_connection, send_mail,EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import EmailForm
import os
from dotenv import load_dotenv

def EmailView(request):
    if request.method == 'POST':
        form = EmailForm(request.POST,request.FILES)

        if form.is_valid():
            print(os.environ.get('EMAIL_PORT'))
            name = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            content = form.cleaned_data['message']
            attachment=form.cleaned_data['attachment']

            

            # Establish a connection to the SMTP server
            connection = get_connection(
                'django.core.mail.backends.smtp.EmailBackend',
                username=os.environ.get('EMAIL_HOST_USER'),
                password=os.environ.get('EMAIL_HOST_PASSWORD'),
                fail_silently=False,
            )

            try:
                # Open the connection
                connection.open()

                # Send the email using the established connection
                email_message=EmailMessage(
                    name,
                    content,
                    os.environ.get('EMAIL_HOST_USER'),
                    [email],
                    # fail_silently=False,
                    connection=connection,
      )
                if attachment:
                    email_message.attach(attachment.name,attachment.read(),attachment.content_type)
                email_message.send()    

            finally:
                # Close the connection after sending the email
              connection.close()

            print(request.FILES)     

            return redirect('emailsend:email')

    else:
        form = EmailForm()
        

    return render(request, 'emailsend/home.html', {'form': form})
