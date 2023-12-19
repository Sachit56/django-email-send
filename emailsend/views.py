from django.shortcuts import render

# Create your views here.
def EmailView(request):
    return render(request,'emailsend/home.html')