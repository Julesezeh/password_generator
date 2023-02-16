from django.shortcuts import render
import requests
from previous.models import Password

def index(request):
    p_word  = ''
    if request.method == "POST":
        choice  = request.POST.get("number")
        choice =  int(choice)
        api_url = 'https://api.api-ninjas.com/v1/passwordgenerator?length={}'.format(choice)
        response = requests.get(api_url, headers={'X-Api-Key': 'F6cYpfAQ19jcUc+NSxTKag==dIvYNWVzxqxd6wYh'})
        if response.status_code == requests.codes.ok:
            password =  response.json()

            p_word=password['random_password']
            new_pass = Password(name=p_word)
            new_pass.save()



        
    return render(request,'index.html',context={'pass':p_word})


def get_previous_pass(request):
    last_pass = Password.objects.all().order_by("id").reverse()[1]
    return render(request,"last_pass.html",context={'pass':last_pass})