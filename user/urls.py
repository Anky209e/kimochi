from django.urls import path,include
from . import views
urlpatterns = [
    
    path('profile/<str:username>/',views.profile),
    path('register/',views.register_account),
    

]