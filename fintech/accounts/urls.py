from django.urls import path
from .views import HomepageView, LoginView, OtpVerifyView, Send
from .views import SignupView, Password, Receive
from .emailverification import Email_VerificationView




urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('login', LoginView.as_view(), name='login'),
    path('otpverify', OtpVerifyView.as_view(), name='otpverify'),
    path('signup', SignupView.as_view(), name='signup'),
    path('email_verify', Email_VerificationView.as_view(), name='verify'),
    path('send/', Send.as_view(), name='send'),
    path('password/', Password.as_view(), name='password'),
    path('receive/', Receive.as_view(), name='receive'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('team/', views.team, name='team'),
    # path('careers/', views.careers, name='careers'),
    # path('reviews/', views.reviews, name='reviews'),
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    
]