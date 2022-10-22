from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Student


@login_required(login_url='Home/page1')

def indexView(request):
    x = Student.objects.all()
    return render(request,'Student/indexView.html',{'stu':x})
 

@login_required(login_url='Home/page1')

def indexAdd(request):
    return render(request,'Student/indexAdd.html')

@login_required(login_url='Home/page1')

def indexUpdate(request):
    return render(request,'Student/indexUpdate.html')

@login_required(login_url='Home/page1')

def indexSearch(request):
    x = Student.objects.all()
    return render(request,'Student/indexSearch.html',{'stu':x.filter(status ='Active')})









@login_required(login_url='Home/page1')
def indexStudentAdd(request):
    x = Student.objects.all()
    if request.method == "POST":
        name = request.POST.get('username')
        Id = request.POST.get('id')
        Date_of_birth = request.POST.get('date_of_birth')
        Department = request.POST.get('department')
        Email = request.POST.get('email')
        Phone = request.POST.get('mobile_number')
        Gpa = request.POST.get('gpa')
        Level = request.POST.get('level')
        Gender = request.POST.get('gender')
        Status = request.POST.get('status')
        for a in x:
            if Id == a.id:
                messages.warning(request,'please enter correct id!')
                return redirect('add')
        
        for a in x:
            if Email == a.Email:
                messages.warning(request,'please enter correct Email!')
                return redirect('add')
        
        y = len(Id)
        if y != 8:
            print(y)
            messages.warning(request,'please enter correct id!')
            return redirect('add')
        
        if Level == '1':
            if Department != 'General':
                messages.warning(request,'please enter correct Level and  Department!')
                return redirect('add')
        if Level == '2':
            if Department != 'General':
                messages.warning(request,'please enter correct Level and  Department!')
                return redirect('add')
        if Level == '3':
            if Department == 'General':
                messages.warning(request,'please enter correct Level and  Department!')
                return redirect('add')
        if Level == '4':
            if Department == 'General':
                messages.warning(request,'please enter correct Level and  Department!')
                return redirect('add')
        
        data = Student(Name=name,id=Id,Date_of_birth=Date_of_birth,Department=Department,Email=Email, MobileNumber=Phone,GPA=Gpa,level=Level,Gender=Gender,status=Status)
        data.save()
        print('complete add student')
        return render(request,'Home/indexHome.html')
    else:
        print('Error method')
        return redirect('add')


@login_required(login_url='Home/page1') 
def indexStudentUpdate(request,id):
    mystudent = Student.objects.get(id=id)
    template = loader.get_template('Student/indexUpdate.html')
    context = {
    'mystudent': mystudent,
    }
    return HttpResponse(template.render(context, request))



@login_required(login_url='Home/page1')
def indexStudentUpdateRow(request,id):
    student = Student.objects.get(id=id)
    
    if  request.method == "POST":
        name = request.POST.get('username')
        Email = request.POST.get('email')
        Phone = request.POST.get('mobile_number')
        Gba = request.POST.get('gpa')
        status = request.POST.get('status')
        Department = request.POST.get('Department')
        Level = request.POST.get('level')

        student.Name = name
        student.Email = Email
        student.MobileNumber = Phone
        student.GBA = Gba
        student.status = status
        student.Department = Department
        student.level = Level  
        student.save()
        
    return HttpResponseRedirect(reverse('Home'))
   
    


@login_required(login_url='Home/page1')
def deletes(request, id):
  student = Student.objects.get(id=id)
  student.delete()
  return HttpResponseRedirect(reverse('search'))
 

@login_required(login_url='Home/page1')
def deletev(request, id):
  student = Student.objects.get(id=id)
  student.delete()
  return HttpResponseRedirect(reverse('view'))
  



