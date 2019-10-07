from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'), 

    
    # *******************************************************
    # begin xo so 
    path('readDataXoSo', views.readDataXoSo, name='readDataXoSo'), 
    path('startJob', views.startJob, name='startJob'), 
    # *******************************************************
    # begin xo so 

    # *******************************************************
    # begin Company 
    path('createDataCompany', views.createDataCompany, name='createDataCompany'),
    path('readDataCompany', views.readDataCompany, name='readDataCompany'),
    path('updateDataCompany', views.updateDataCompany, name='updateDataCompany'),
    path('deleteDataCompany', views.deleteDataCompany, name='deleteDataCompany'),
    path('findDataCompany', views.findDataCompany, name='findDataCompany'),
    path('searchDataAgencyOfCompany', views.searchDataAgencyOfCompany,
         name='searchDataAgencyOfCompany'),
    # end Company
    # ******************************************************* 
]
