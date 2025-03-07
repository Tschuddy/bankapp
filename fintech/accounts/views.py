from django.shortcuts import render
from django.views import View

# Create your views here.


class HomepageView(View):
    def get(self, request):
        return render(request, 'blog/index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'blog/login.html')
    

class OtpVerifyView(View):
    def get(self, request):
        return render(request, 'blog/otpverify.html')
    
class SignupView(View):
    def get(self, request):
        return render(request, 'blog/signup.html')
    



class Send(View):
    def get(self, request):
        return render(request, 'blog/send.html')
    
class Password(View):
    def get(self, request):
        return render(request, 'blog/password.html')

class Receive(View):
    def get(self, request):
        return render(request, 'blog/receive.html')


# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')

# def team(request):
#     return render(request, 'team.html')

# def careers(request):
#     return render(request, 'careers.html')

# def reviews(request):
#     return render(request, 'reviews.html')

# def login(request):
#     return render(request, 'login.html')

# def register(request):
#     return render(request, 'register.html')

