from django.shortcuts import render,redirect
from user.forms import RegistrationForm
from message.forms import MessageForm
from news.models import Post
from news.forms import PostForm
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout,decorators
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def home(request): # ty nua sua
    return render(request,'TLU/index.html')


class Login(View):
    def get(self,request):
        return render(request, 'TLU/login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        my_user = authenticate(username=username,password=password)
        if my_user is None:
            return HttpResponse("Dang nhap that bai")
        login(request,my_user)
        return redirect('home')

def Logout(request):
    logout(request)
    return redirect('home')

def Profile(request):
    return render(request, 'TLU/contact.html')

class Register(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request, 'TLU/register.html', {'f':form})

    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Dang nhap thanh cong")
        return render(request, 'TLU/register.html', {'f':form})

class MyMessage(View):
    def get(self,request):
        mess = MessageForm()
        return render(request,'TLU/contact.html',{'mess':mess})

    def post(self,request):
        mess = MessageForm(request.POST)
        if mess.is_valid():
            mess.save()
            return redirect('home')
        return HttpResponse("Error")

def News(request):
    my_data = Post.objects.all()
    return render(request,'TLU/news.html',{'Data':my_data})

@decorators.login_required(login_url='/Login/')
def Profile(request):
    return render(request,'TLU/profile.html')

class MyPost(View):
    def get(self,request):
        post_form = PostForm()
        return render(request,'TLU/post.html',{'post_form':post_form})

    def post(self,request):
        my_post = PostForm(request.POST)
        if my_post.is_valid():
            my_post.save()
            return redirect('home')
        return HttpResponse("Error")




