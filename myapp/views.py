
# from students.models import Stud
from myapp.models import Student
# from employees.models import Employee
from employees.models import Employee

from recordings.models import Topic
# from myapp.form import register
# Create your views here.



def home(request):
    # data = Stud.objects.all()
    return render(request,'home.html')


def about(request):
    values = Employee.objects.all()
    return render(request,'about.html',{'context':values})

def contact(request):
    data = Student.objects.all()
    return render(request,'contact.html',{'info':data})


def services(request):
    return render(request,'services.html')



def register(request):
    print("Request method:", request.method)
    if request.method == "POST":  # Use uppercase 'POST'
        name = request.POST['name']  # Use uppercase 'POST'
        emp_id = request.POST['emp_id']  # Corrected to access emp_id
        role = request.POST['role']  # Added to capture role
        date_joined = request.POST['date_joined']
        address = request.POST['address']
        city = request.POST['city']  # Added to capture city
        company_name = request.POST['company_name']
        company_location = request.POST['company_location']
        qualification= request.POST['qualification']

        Emp = Employee(name=name, emp_id=emp_id, role=role,  # Include role
                       date_joined=date_joined, address=address,
                       city=city, company_name=company_name,company_location=company_location,qualification=qualification)

        Emp.save()
        return redirect('register')  # Redirect to a specific URL after saving

    return render(request, 'register.html')

# def register(request):
#     # data = register()

#     if request.method == "post":
#         name = request.post['name']
#         emp_id = request.post['role']
#         date_joined = request.post['date_joined']
#         address = request.post['address']
#         city = request.post['city']
#         company_name = request.post['company_name']

#         Emp = Employee(name=name,emp_id=emp_id,date_joined=date_joined,address=address,city=city,company_name=company_name)

#         Emp.save()
#         return redirect('')

#     return render(request,'register.html')



def recordings(request):
    data = Topic.objects.all()

    return render(request,'Recordings.html',{'recordings':data})



def upload(request):
    if(request.method == "POST"):
        title = request.POST['title']
        thumbnail = request.FILES['thumbnail']
        video = request.FILES['video']

        record = Topic(
            title = title,
            thumbnail = thumbnail,
            video = video
        )

        record.save()

        return redirect('recordings')
    
    return render(request,'uploadrecord.html')


# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# from .form import UserRegister

# def signup(request):

#     form = UserRegister()

#     if request.method == "POST":

#         form = UserRegister(request.POST)

#         if form.is_valid():

#             form.save()

#             return redirect('login')
        
        
#     return render(request, 'signup.html', {'form': form})




from django.contrib import messages

# from django.contrib import messages
from django.shortcuts import render, redirect
from .form import UserRegister 


def signup(request):

    if request.method == 'POST':

        form = UserRegister(request.POST)

        if form.is_valid():

            user = form.save()
            # Add a success message

            messages.success(request, 'Your account has been created successfully!')

            # Instead of redirecting immediately, we just return the same page
            # return redirect('login')
            return redirect(request, 'signup.html', {'form':  UserRegister()})
        
        else:
            messages.error(request, 'There were some errors with your submission. Please try again.')
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserRegister()

    return render(request, 'signup.html', {'form': form})



from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

def user_login(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)

        if form.is_valid():
            
            user = form.get_user()
            
            if user is not None:
                login(request,user)
                return redirect('home')

    return render(request,'login.html',{'form':form})













def user_logout(request):

    logout(request)

    return redirect("login")