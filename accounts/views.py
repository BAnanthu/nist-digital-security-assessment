from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from Smarthive import settings
from accounts.models import Userdetails
from report.models import Assesmeent


class SignIn(View):

    def post(self, request):
        login_email = request.POST['email']
        login_password = request.POST['password']

        if User.objects.filter(email=login_email).exists():
            user = User.objects.get(email=login_email)
            print(user)
            print(user.check_password(login_password))
            if user.check_password(login_password):

                if user:
                    auth.login(request, user)
                    return redirect(settings.LOGIN_REDIRECT_URL)

            else:

                return render(request, 'accounts/login.html', {'error': "! invalid password "})
        else:

            return render(request, 'accounts/login.html', {'error': "! invalid email "})

    def get(self, request):
        return render(request, 'accounts/login.html', {'error': ""})


class SignUp(View):

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        cnfpassword = request.POST['cnfpassword']
        password = request.POST['password']
        # gender = request.POST['gender']
        # dob = request.POST['dob']
        print("hoii")
        if cnfpassword == password:

            if User.objects.filter(email=email).exists():
                messages.error(request, '! email taken.')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=first_name + last_name, first_name=first_name,
                                                last_name=last_name, email=email, password=password)
                user.save()
                profile = Userdetails(user=user, gender='gender', date_of_birth='1997-08-08',
                                      display_name=first_name + last_name)
                profile.save()

                assesment = Assesmeent(user_id=user)

                assesment.save()
                return redirect('login')
        else:
            messages.error(request, '! email doesn\'t match.')
            return redirect('signup')

    def get(self, request):
        return render(request, 'accounts/signup.html')

def signout(request):
    auth.logout(request)
    return redirect('login')