from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.models import Task,User
from .forms import TaskForm

# Create your views here.
def home(request):
    return render(request, 'tasks/home.html')

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/tasks/login')
    context = {'form':form}
    return render(request,'tasks/register.html',context)
    

def registerOld(request):
    context = {}
    #print(request.POST)
    #print(request.GET)
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname =  request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        User.objects.create(firstname=firstname,lastname=lastname,username=username,Password=password,gender=gender,email=email)
        context['firstname'] = firstname
        context['lastname'] = lastname 
        context['username'] = username  
        context['email'] = email
        context['password'] = password 
        context['gender'] = gender
        context['created'] = True
    return render(request, 'tasks/register.html', context=context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            redirect('/tasks/')
    else:
        form = AuthenticationForm(request)
    context = {'form' : form}
    return render(request, 'tasks/login.html',context)

def login_viewOld(request):
    #login_details = request.GET #get the query dictionary submitted by the user
    #name = login_details.get(id) #from the dictionary, extract the 
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        #authenticate user
        print(username,password)
        user  = authenticate(request,username=username,password=password)
        if user is None:
            context = {'error':'Invalid Username or password'}
            return render(request, 'tasks/login.html',context)
        print(user)
        login(request,user)
        return redirect('/tasks/home')
    return render(request, 'tasks/login.html',{})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        redirect('tasks/login/')
    return render(request,'tasks/logout.html',{})

@login_required
def task_create_view(request):
    form = TaskForm(request.POST or None)
    context = {'form':form}
    #What happens when the form is valid
    if form.is_valid():
        #extract the content of the form from the resulting 'request.POST' dictionary
        task_object = form.save(commit=False)  #don't commit the changes to the database yet
        task_object.user = request.user #link the current user to the user field in the TaskForm
        task_object.save() #commit all changes including the linked user field
        context['form'] = TaskForm() #initialise a new form
    return render(request,'tasks/task_create_view.html',context=context)

# @login_required
# def task_create_view(request):
#     form = TaskForm(request.POST or None)
#     context = {'form':form}
#     #What happens when the form is valid
#     if form.is_valid():
#         #extract the content of the form from the resulting 'request.POST' dictionary
#         #task_object = form.save()
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         target_date = request.POST.get('target_date')
#         target_time = request.POST.get('target_time')
#         Task.objects.create(title=title,content=content,target_date=target_date,target_time=target_time,user=request.user)
#         #content.save()
#     print(request.POST)
        
#     return render(request,'tasks/task_create_view.html',context=context)
    
def welcome_user(request):#,user_id=None):
    #user_name = None
    #if user_id is not None:
        #user_name = User.objects.get(id=user_id)
        #context = {"username" : user_name.firstname}
    username_dict = request.GET #this is a dictionary
    username  = username_dict.get('username')
    user = User.objects.get(username = username)
    list_all = [user.id,user.firstname,user.lastname,user.email]
    return render(request, 'tasks/welcome.html',{'username': username, 'details':list_all})#, context=context)


    