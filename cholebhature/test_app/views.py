from django.shortcuts import HttpResponse, render, redirect
from test_app.models import test
def home(request):
    return render(request,'home.html')

def contact(request):
    data=test.objects.all()#geeting all the data fromthe table
    if request.method=='POST':
        name= request.POST.get('name')
        number= request.POST.get('number')
        test_instance=test(name=name,number=number)
        test_instance.save()
        return redirect('home')

    return render(request,'contact.html',{'data': data})

def About(request):
    return render(request,'about.html')

#get method is less secure because data is sent throught url
#but post is more secure as it uses requests
#cross site request forgary 