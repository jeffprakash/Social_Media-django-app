
from .models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required( login_url='signin')
def index(request):
    user_profile=Profile.objects.get(user=request.user) 
    
    return render(request,'index.html',{'u':user_profile})     #not working when obj passed with same name as of that.


@login_required(login_url='signin')
def settings(request):
    user_profile=Profile.objects.get(user=request.user)     #note
    
    if request.method=='POST':
        
        if request.FILES.get('profilepic')==None:
            
            image=user_profile.profileimg['profilepic']
            bio=request.POST['bio']
            location=request.POST['location']


            user_profile.profileimg=image
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()

        if request.FILES.get('profilepic') != None:
           
            image=request.FILES.get('profilepic')
            bio=request.POST['bio']
            location=request.POST['location']


            user_profile.profileimg=image
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()


        return redirect('settings')    



    
    
    return render(request,'setting.html',{'user_profile':user_profile})

def signin(request):
    
    if (request.method=='POST'):
        
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)      #returns a obj user if authentication is success
        if (user is not None):
            auth.login(request,user)
            return redirect('/')
            
                   
        else:
            messages.info(request,'Credentials invalid')
            return redirect('signin')
    
    
    
    
    else:
       
        print("not jeff")
        return render(request,'signin.html')



def signup(request):

    

    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['confirmpass']

        if(password==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()    

                user_login=auth.authenticate(username=username,password=password)
                auth.login(request,user_login) 

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('settings')

        else:
             messages.info(request,'Password not matching')
             return redirect('signup')

    else:
        
        return render(request,'signup.html')    

@login_required(login_url='/signin')
def logout(request):

    auth.logout(request)

    return redirect('signin')



        