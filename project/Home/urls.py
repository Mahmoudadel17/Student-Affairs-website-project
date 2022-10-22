from django.urls import path
from .import views

urlpatterns = [
    path('first',views.indexFirst,name='first'), # first page in prject
    path('Page1',views.indexPage1,name='page1'), # go to login page (page1)
    path('HomePage',views.indexHome,name='Home'), # go to home page from nav bar (indexHome)
    
    path('',views.LogoinPage,name='Home2'), # go to home page from login page
    path('Page1',views.LogoutPage,name='logout'), # logout

]
 