
from django.db.models import Q
from django.http import HttpResponse
import  os
from django.conf import settings
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView,ListView

from forms import StudentForm
from django.shortcuts import render, redirect
from apps.core.models import User
# from django.views import templates





def index(request):
    print("hii")
    object=User.objects.create(first_name="aman",last_name="yogi",email="yogi@gmail.com",phone_number=9685711542,age=24)
    print(object)
    # object=User.objects.create(first_name="kamal",last_name="sain",email="kamal@gmail.com",phone_number=9568547123,age=22)
    # print(object)
    # object=User.objects.create(first_name="ajay",last_name="saini",email="ajay@gmail.com",phone_number=8654712395,age=28)
    # print(object)
    # object=User.objects.filter(id=6).update(first_name="dinesh",last_name="kumar",email="dinesh@gmail.com",phone_number=9658745623,age=28)
    # print(object)
    # object = User.objects.filter(id=2).update(last_name="kumar")
    # print(object)
    # object = User.objects.filter(id=3).update(first_name="parvesh", last_name="saini", email="parvesh@gmail.com",phone_number=5698745236, age=23)
    # print(object)

    # object=User.objects.get(id=2)
    # print(object)

    # object=User.objects.all()
    # for obj in object:
    #     name=obj.first_name
    #     print(name)
    #     last=obj.last_name
    #     print(last)
    #     email=obj.email
    #     print(email)
    #     phone=obj.phone_number
    #     print(phone)
    #     age=obj.age
    #     print(age)
    #
    # object=User.objects.filter(age=23)
    # print(object)
    #
    # object=User.objects.get(id=6).delete()
    # print(object)

    # object=User.objects.filter(age=23)
    # print(object)

    # object=User.objects.filter(age=26)
    # for obj in object:
    #     print(obj.first_name)


    object = User.objects.filter(age=23)
    print(len(object))









    # # total=0
    # # for i in range(object):
    # #     total=total+1
    # # print(total)






    response=HttpResponse("hello world")
    return response

def homepage(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        city = request.POST.get('city')
        address = request.POST.get('state')
        image = request.FILES.get('image')


        # Print the form data in the terminal
        print(f"Name: {name}, City: {city}, Address: {address}, Image:{image}")
        if image:
            # Define the path where you want to save the image
            image_path = os.path.join(settings.MEDIA_ROOT, 'images', image.name)

            # Open a file handler and write the image data to it
            with open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

    # print(type(data))
    # names=data.get("name",None)
    # print(names)
    # name=data["name"]
    # print(name)



    return render(request,"Form.html")

@csrf_exempt
def homepage(request):
    if request.method =='GET':
        print("Get method")
    if request.method == 'POST':
        print("Post method")
    if request.method == 'delete':
        print("Delete method")
    if request.method == 'put':
        print("Put method")
    if request.method == 'patch':
        print("Patch method")
    if request.method == 'option':
        print("Option method")
    if request.method == 'head':
        print("Head method")
    if request.method == 'connect':
        print("Connect method")
    if request.method == 'trace':
        print("Trace method")


    return render(request, "Form.html")

@method_decorator(csrf_exempt, name='dispatch')
class Contact(View):
    def get(self,request,*arge,**kwargs):
        print("Get method")
        return render(request,"Form.html")

    def post(self,request,*arge,**kwargs):
        print("Post method")
        return render(request,"Form.html")

    def delete(self,request,*args,**kwargs):
        print("Delete method")
        return render(request,"Form.html")
    def put(self,request,*args,**kwargs):
        print("Put method")
        return render(request,"Form.html")

    def patch(self, request, *args, **kwargs):
        print("Patch method")
        return render(request, "Form.html")

    def option(self, request, *args, **kwargs):
        print("Option method")
        return render(request, "Form.html")

    def head(self, request, *args, **kwargs):
        print("Head method")
        return render(request, "Form.html")

    def connect(self, request, *args, **kwargs):
        print("Connect method")
        return render(request, "Form.html")

    def trace(self, request, *args, **kwargs):
        print("Trace method")
        return render(request, "Form.html")

# genericviev se create user


class CreateUserView(CreateView):
    model = User
    # fields = "__all__"
    # fields = ['first_name','last_name']
    form_class = StudentForm
    template_name = 'student_form.html'
    # success_url = reverse_lazy('create_user')
    success_url = '/student_list'




# class se check

# class CreateUserView(View):
#     def get(self, request):
#         form = StudentForm()
#         return render(request, "user_form.html", {'form': form})
#
#     def post(self, request):
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/student_list')
#         return render(request, "user_form.html", {'form': form})



# modal se save karvana form
# def create_user (request):
#
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/student_list')
#
#     else:
#         form = StudentForm()
#
#     return render(request, "user_form.html", {'form': form})


# form chack karvana


# def create_user(request):
#     if request.method=="GET":
#         return render(request, template_name="user_form.html")
#
#     else:
#         print("hghfhggfhfhffhfh",request.POST)
#         first_name=request.POST["first_name"]
#         last_name=request.POST["last_name"]
#         email=request.POST["email"]
#         phone_number=request.POST["phone_number"]
#         age=request.POST["age"]
#         User.objects.create(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,age=age)
#
#         return redirect("/student_list")
#         return render(request, template_name="user_form.html")

def create_student(request):
    if request.method=="GET":
        student_form = StudentForm()
        return render(request, template_name="student_form.html", context={"form": student_form})

    else:
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        age = request.POST["age"]
        User.objects.create(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, age=age)
# student form use context
        student_form=StudentForm()
        return render(request, template_name="student_form.html",context={"form":student_form})

#use queryset

# list function base

# def student_list(request):
#     students=User.objects.all()
#     student_text = request.GET.get("search")
#     if student_text:
#         students = students.filter(Q(first_name=student_text) | Q(email=student_text))
#         # students = students.filter(first_name__icontains=student_text)
#     return render(request, "student_list.html", {"students": students})
#     # students=User.objects.filter(age=23)
#     # student list show karne ke liye
#     # return render(request,"student_list.html",{"students":students})


# list class base

# this code error
# class student_list(View):
#     def get(self,request):
#         print("student")
#         student_text = request.GET.get("search")
#         students = User.objects.all()
#         students = students.filter(Q(first_name=student_text) | Q(email=student_text))
#         return render(request, "student_list.html", {"students": students})

# class student_list(View):
#     def get(self, request):
#         student_text = request.GET.get('search', '')  # Default to empty string if 'search' is not provided
#         if  student_text:
#             # Filter data if search_text is provided
#             students = User.objects.filter(Q(first_name__icontains= student_text) | Q(email__icontains= student_text))
#
#         else:
#             # Get all users if no search_text is provided
#             students = User.objects.all()
#         return render(request, "student_list.html", {"students": students})


# genericview list


class  student_list(ListView):
    model = User
    template_name = "student_list.html"

    def get(self, request):
        student_text = request.GET.get('search', '')  # Default to empty string if 'search' is not provided
        if student_text:
            # Filter data if search_text is provided
            students = User.objects.filter(Q(first_name__icontains=student_text) | Q(email__icontains=student_text))

        else:
            # Get all users if no search_text is provided
            students = User.objects.all()
        return render(request, "student_list.html", {"students": students})






# delete create user

# def delete(request,id):
#     dele = User.objects.get(id=id)
#     dele.delete()
#     return redirect('/student_list')

# class base delete user
class UserDeleteView(View):
    def get(self, request, id):
        dele = User.objects.get(id=id)
        dele.delete()
        return redirect('/student_list')



# function base update
# def update(request,id):
#
#     if request.method == "GET":
#         update_form = User.objects.filter(id=id).first()
#         return render(request, "forms.html", {"form": update_form})
#     else:
#         object = User.objects.filter(id=id).first()
#         firstname = request.POST.get('first_name')
#         lastname = request.POST.get('last_name')
#         phone_number = request.POST.get('phone_number')
#         email = request.POST.get('email')
#         age = request.POST.get('age')
#         object.first_name = firstname
#         object.last_name = lastname
#         object.phone_number = phone_number
#         object.email = email
#         object.age = age
#         object.save()
#         return redirect('/student_list')

# clas base update data

# class UpdateUserView(View):
#     def get(self, request, id):
#         print('get Method run')
#         user = User.objects.get(id=id)
#         print(user)
#         form =  StudentForm(instance=user)
#         return render(request, "student_form.html", {'form': form})
#
#     def post(self, request, id):
#         print('Post Method run')
#         user = User.objects.get(id=id)
#         form =  StudentForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('/student_list')
#         return render(request, "student_list.html", {'form': form, 'user': user})


# genericview updete

class UpdateUserView(UpdateView):
    model=User
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = '/student_list'


# def confirm_delete(request,id):
#     if request.method=="GET":
#         context={"id":id}
#         return render(request,"delete_page.html",context)

# genericview base delete

class ConfirmDelete(DeleteView):
    model = User
    template_name = 'student_form.html'
    success_url = '/student_list'


# django forms



    # django forms use modals










# def create_table(request):
#     student_data=[{"f_name":"rahul","l_name":"kumawat","age":23,"email":"rahul@gmail.com","mobile":9680711542,"address":"jaipur"},
#                   {"f_name":"deepandra","age":25,"l_name":"kumawat","email":"deepu12@gmail.com","mobile":865822452152,"address":"chomu"}]
#     return templates.TemplateResponse(
#         request=request,name="table.html",context={"title": "home page","students":student_data})


