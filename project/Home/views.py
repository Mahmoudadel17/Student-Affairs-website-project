from django.shortcuts import redirect, render
from .models import loginForm
from django.contrib.auth import authenticate, login,logout


def indexFirst(request):
    return render(request,'Home/first.html')

def indexPage1(request):
    return render(request,'Home/page1.html')
 
def indexHome(request):
    return render(request,'Home/indexHome.html')




def LogoinPage(request):
    l = loginForm.objects.all()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 

        for x in l:
            if x.username == username:
                if x.password == password:
                    print('login complete')
                    user = authenticate(request,username=username,password=password)
                    login(request,user) 
                    return render(request,'Home/indexHome.html')
                else:
                    print('Error password')
                    return redirect('page1')
            else:
                print('Error username')
                return redirect('page1')
    else:
        return redirect('page1')

        

def LogoutPage(request):
    logout(request)
    return redirect('page1')


