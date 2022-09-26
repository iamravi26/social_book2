from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from mybooks.models import user
# Create your views here.

def home(request):
    # context={
    #     # 'posts':Post.objects.all()
    #     "welcome to home page"
    # }
    return render(request,'home.html')



def register(request):
    # import pdb;pdb.set_trace()
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        password1 = data.get("password1")
        password2 = data.get("password2")

        if email and (password1 == password2):
            bhai = user(email=email,password=password1,username=email, name=name)
            bhai.save()
            return redirect("login")

    return render(request,'register1.html')

def login_view(request):
    context = dict()
    # import pdb;pdb.set_trace()
    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = User.objects.filter(username=email, password=password)
            # user = authenticate(username=email, password=password)
            if user and len(user)==1:
                login(request, user[0])
                return redirect("/")
            else:
                context.update({"message":"user not found"})
        else:
            context.update({"message":"email and password missing"})

    return render(request,'login1.html', context)

    