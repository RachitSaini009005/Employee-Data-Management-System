from django.shortcuts import render ,HttpResponse
from .models import Employee , Role , Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render (request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render (request,'all_emp.html',context)

def add_emp(request):
   
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        Role= (request.POST['Role'])
        # hire_date = (hire_date.POST())
        new_emp = Employee(first_name=first_name , last_name=last_name,salary=salary,bonus=bonus,phone= phone,dept_id = dept , Role_id= Role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")
 
    elif request.method =='GET':
        return render (request,'add_emp.html')

    else:
        return HttpResponse("exception occured.Employee not added successully")
    

# def add_emp(request):
#     if request.method=="POST":
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         salary = int(request.POST['salary'])
#         bonus = int(request.POST['bonus'])
#         phone = request.POST['phone']
#         dept = int(request.POST['dept'])
#         Role = request.POST['Role']
#         # hire_date = hire_date.POST()
#         new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone = phone,Role_id=Role,dept_id=dept,hire_date=datetime.now())
#         new_emp.save()
#         return HttpResponse("Employee added sucessfully")
#     elif request.method=="GET":
#         return render(request,"add_emp.html")
    
#     else:
#         return HttpResponse("Exception occured Employee not added successfully")
# def add_emp(request):
#     if request.method =="POST":
#         first_name= request.POST["first_name"]
#         last_name = request.POST["last_name"]
#         salary = request.POST["salary"]
#         dept = request.POST["dept"]
#         Role = request.POST["Role"]
#         phone = request.POST["phone"]
#         new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,dept_id=dept,Role_id=Role,phone=phone,hire_date = datetime.now())
#         new_emp.save()
        
#         return HttpResponse("Employee Added Successfully")
#     elif request.method=="GET":
#         return render(request,"add_emp.html")
#     else: 
#         return HttpResponse("Exception occured Employee not added Succuessfully")

# -----------------------------------------------------------------------------------------------------

# def remove_emp(request , emp_id=0):
#     if emp_id:
#         try:
#            entered_emp_to_removed= Employee.objects.get(id=emp_id)
#            entered_emp_to_removed.delete()
#            return HttpResponse("employee removed sucessfully")
#         except:
#            return HttpResponse("please enter the valid id")

#     emps = Employee.objects.all()
#     context ={
#         'emps':emps
#     }
#     # print(context)
#     return render (request,'remove_emp.html',context)
#     # return render (request,'remove_emp.html')


# def remove_emp(request,emp_id=0):
#     if emp_id:
#         try:
#             entered_emp_to_removed = Employee.objects.get(id=emp_id)
#             print(entered_emp_to_removed)
#             entered_emp_to_removed.delete()
#             return HttpResponse("Employee removed Suceessfully")
#         except:
#             return HttpResponse("Please enter the valid ud")
#     emps = Employee.objects.all()
#     context={
#         'emps':emps
#     }
#     return render(request,'remove_emp.html',context)

def remove_emp(request,emp_id=0):
    if emp_id :
        try:
            entered_emp_to_removed = Employee.objects.get(id=emp_id)
            entered_emp_to_removed.delete()
            return HttpResponse("Employee removed sucessfully")
        except:
            return HttpResponse("Enter valid emp id")
    emps= Employee.objects.all()
    context={
    "emps":emps
     }
    return render(request,'remove_emp.html',context)
# def remove_emp(request, emp_id= 0):
#     if emp_id:
#         try:
#             entered_emp_to_removed = Employee.objects.get(id = emp_id)
#             print(entered_emp_to_removed)
#             entered_emp_to_removed.delete()
#             return HttpResponse("Employee removed Sucessfully")
#         except:
#             return HttpResponse("please enter the valid id")
        
#     emps = Employee.objects.all()

#     context = {
#     'emps':emps
#     }
#     print(context)
#     return render(request,'remove_emp.html',context)
    
def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request. POST['dept']
        Role= request.POST['Role']
        emps = Employee.objects.all()

        if name:
            emps =emps.filter(Q(first_name__icontains = name)| Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(Q(dept__name__icontains= dept))
        if Role:
            emps = emps.filter(Q(Role__name__icontains= Role))

        context ={
            'emps': emps
        }
        return render(request,'all_emp.html',context)
    elif request.method =='GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("An exception occured")