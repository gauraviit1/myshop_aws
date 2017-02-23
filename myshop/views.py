from myshop.forms import UserRegistrationForm
from django.shortcuts import render, redirect
import requests
from django.contrib import messages
from django.conf import settings


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                              data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            if result['success']:
                # Create a new user object but avoid saving it yet
                new_user = user_form.save(commit=False)
                # Set the chosen password
                new_user.set_password(user_form.cleaned_data['password'])
                # Save the User object
                new_user.save()
                messages.success(request, 'New user added with success!')
                return render(request, 'registration/register_done.html',
                              {'new_user': new_user})

            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('register')
    else:
        user_form = UserRegistrationForm()
        return render(request, 'registration/register.html',
                      {'user_form': user_form})
