import html2text as html2text
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = authenticate(request=request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('dashboard_view'))  # Redirect to dashboard view after login
            else:
                error_message = "Invalid username or password"
                return render(request, 'authentication/login.html', {'error_message': error_message})

        except Exception as e:
            # Print the exception to the console or log file for debugging
            print("Exception during authentication:", e)
            error_message = "An error occurred during authentication"
            return render(request, 'authentication/login.html', {'error_message': error_message})

    success_message = request.session.pop('success_message', None)
    return render(request, 'authentication/login.html', {'success_message': success_message})


def logout_view(request):
    logout(request)
    return redirect('login_view')


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration completed. You can now log in.")
            success_message = "Registration Completed"
            request.session['success_message'] = success_message
            login_page_url = reverse('login_view')  # Generate URL
            return redirect(login_page_url)
    else:
        form = RegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})


# password rest views create blow

class PasswordResetView(PasswordResetView):
    def html_to_text(html):
        # Create an instance of the HTML2Text converter
        h = html2text.HTML2Text()
        h.ignore_links = True  # To ignore hyperlinks and only keep the plain text
        return h.handle(html)

    try:
        template_name = 'authentication/password_reset_form.html'
        html_email_massage = html_to_text('authentication/password_reset_email.html')
        success_url = reverse_lazy('password_reset_done')

    except Exception as e:
        print("PasswordResetView Exceptions: ", e)


class PasswordResetDoneView(PasswordResetDoneView):
    try:
        template_name = 'authentication/password_reset_done.html'
    except Exception as e:
        print("PasswordResetDoneView Exceptions: ", e)


class PasswordResetConfirmView(PasswordResetConfirmView):
    try:
        template_name = 'authentication/password_reset_confirm.html'
        success_url = reverse_lazy('password_reset_complete')
    except Exception as e:
        print("PasswordResetConfirmView Exceptions: ", e)


class PasswordResetCompleteView(PasswordResetCompleteView):
    try:
        template_name = 'authentication/password_reset_complete.html'
    except Exception as e:
        print("PasswordResetCompleteView Exceptions: ", e)
