from django.urls import path
from .import views

urlpatterns = [
    path('View',views.indexView,name='view'),
    path('Add',views.indexAdd,name='add'),
    path('Update',views.indexUpdate,name='update'), 
    path('Search',views.indexSearch,name='search'),

    path('',views.indexStudentAdd,name='studentAdd'),
    path('deletes/<int:id>',views.deletes,name='delete'),
    path('deletev/<int:id>',views.deletev,name='delete'),
    
    path('update/<int:id>',views.indexStudentUpdate,name='studentUpdate'),
    path('update/updaterow/<int:id>',views.indexStudentUpdateRow,name='studentUpdaterow'),


 
]
 