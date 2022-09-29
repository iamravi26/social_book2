
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate
from .models import CustomUser



# Create your views here.

def home(request):
    # context={
    #     'posts':Custo.objects.all()
    # }
    return render(request,'index.html')



def register(request):
    # import pdb;pdb.set_trace()
    if request.method == "POST":
        data = request.POST
        firstname= data.get("firstname")
        lastname= data.get("lastname")
        # username=data.get("username")
        email = data.get("email")
        password1 = data.get("password1")
        password2 = data.get("password2")
        public_visibility=data.get("public_visibility")
        author=data.get("author")
        seller=data.get("seller")
        date_of_birth=data.get("date_of_birth")
        address=data.get("address")
        
        if author == 'True':
            print("author")
            author = True
        else:
            author = False

        if seller == 'True':
            print("author")
            seller = True
        else:
            seller = False

        if public_visibility == 'True':
            print("author")
            public_visibility = True
        else:
            public_visibility = False
        

       
        user_obj = User.objects.create_user(email=email,  password= password1)
        user_obj.save()
        if email and (password1 == password2):
            user = CustomUser.objects.get_or_create(first_name=firstname,last_name=lastname,public_visibility=public_visibility, email=email,password=password1,author=author,seller=seller,date_of_birth=date_of_birth,Address=address)
            
            return redirect("login")

    return render(request,'register1.html')

def login_view(request):
    context = dict()
    # import pdb;pdb.set_trace()
    if request.method == "POST":
        data = request.POST
        email=data.get("email")
        password = data.get("password")


        print("username",email)
        print("password",password)

        myuser = CustomUser.objects.get(email=email, password=password)

        print("myuser",myuser)
        user =authenticate(email=email, password=password)
        print("user",user)
        
        if user is not None:

            login(request,user)
            return redirect("/")

        else:
            return render(request,'login1.html')





        

        # if username and password:
        #     # import pdb;pdb.set_trace()

        #     print("username",username)
        #     print("password",password)
        #     user = CustomUser.objects.get(username=username, password=password)
        #     print("user",user)

        #     user = authenticate(username=username, password=password)
        #     print("user",user)
        #     if user and len(user)==1:
        #         login(request, user[0])
        #         return redirect("/")
        #     else:
        #         context.update({"message":"user not found"})
        # else:
        #     context.update({"message":"email and password missing"})

    return render(request,'login1.html', context)

    