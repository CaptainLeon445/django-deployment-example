from django.shortcuts import render

#from MyDjango_stuff.fourth_project import fourth_app
from fourth_app.forms import NewUser

# Create your views here.
def index(Request):
    return render(Request,'fourth_app/index.html')

def form_views(Request):
    Form=NewUser()

    if Request.method=="POST":
        Form=NewUser(Request.POST)

        if Form.is_valid():
            Form.save(commit=True)
            return index(Request)

        else:
            print("Error!")

    return render(Request,"fourth_app/forms.html",{'form':Form})
