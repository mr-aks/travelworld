from django.db.models.query import RawQuerySet
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages
from main.forms import BlogForm
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail

from main.models import Blog

# Create your views here.

def home(request):
    blog = Blog.objects.all()
    return render(request, 'home.html',{'blog':blog})



def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'email already exist')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                subject = 'About Registration'
                message = f'Hi, {username}. You have been registred successfuly on Travel '
                email_from = 'smashtv777@gmail.com'
                rec_list = [email,]
                send_mail(subject, message, email_from, rec_list)
                messages.success(request, 'user registered')
                return redirect('login')
        else:
            messages.warning(request, 'password did not match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            print(username)
            return redirect('home')
        else:
            messages.warning(request, 'username or password is incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html')



def post(request):
    if request.method=='POST':
        tittle = request.POST.get('tittle')
        dsc =  request.POST.get('dsc')
        imgs = request.FILES['image']
        post = Blog(tittle=tittle,dsc=dsc,user_id=request.user,Img=imgs)
        post.save()
        messages.success(request,'Post has been submitted succesfully')
        return redirect('post')
    return render(request, 'post.html')


def search(request):
    sname = request.POST['search']
    blog = Blog.objects.filter(tittle__icontains=sname)
    return render(request, 'home.html',{'blog':blog})


def logout(request):
    auth.logout(request)
    return redirect('home')

def pdetails(request,id):
    blog = Blog.objects.get(id=id)
    return render(request, 'pdetails.html',{'blog':blog})


def delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request, 'Post has been deleted')
    return redirect('home')

def edit(request,id):

    blog = Blog.objects.get(id=id)
    form = BlogForm(instance=blog)
    if request.method=='POST':
        form = BlogForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post has been edited successfuly')
            return redirect('home')
    return render(request, 'edit.html',{'form':form} )


def changepassword(request):
    if request.method=='POST':
        cform = PasswordChangeForm(request.user, request.POST)
        if cform.is_valid():
            user = cform.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password has been changed successfuly')
            return redirect('home')
        else:
            messages.warning(request, 'error')
            return redirect('changepassword')
    else:
        form = PasswordChangeForm(request.user)
        return render(request,'changepassword.html',{'form':form})
