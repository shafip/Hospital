from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('logout/', views.home,name="home"),
    path('department/', views.department,name='department'),
    path('doctor/', views.adddoctors,name='doctor'),
    path('booking/', views.bookingview,name='booking'),
    path('patientview/', views.viewpatient,name='patient'),

    # path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),

    path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='login/login.html'), name="login"),
    path('', auth_view.LogoutView.as_view(template_name='login/guest.html'), name="logout"),
]