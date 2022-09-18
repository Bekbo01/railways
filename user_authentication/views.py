from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

# modules needed for user authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#for pasword reset
from django.contrib.auth import views
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from django.conf import settings
from tasks.models import Task
from user_authentication.models import User
# importing the use model
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from depo.models import Depo
User = get_user_model()


# importing the forms
from .forms import LoginForm, RegisterForm
from django.shortcuts import get_object_or_404
from depo.models import Depo, DepoCopy

# Create your views here.

def home(request):
    conf = dict()
    if request.user.is_authenticated:
        if request.user.user_position == 'Дежурный ДЕПО':
            depo = DepoCopy.objects.get(member=request.user)
            tasks = [i.task for i in Depo.objects.filter(depochoice=depo)]
        else:
            tasks = Task.objects.filter(user_position=request.user)
        conf['tasks'] = tasks
    return render(request, 'index.html', conf)

def profile(request):
    conf = dict()
    conf['depo'] = None
    if request.user.user_position == 'Дежурный ДЕПО':
        depo = DepoCopy.objects.get(member=request.user)
        conf['depo'] = depo
        tasks = len([i.task for i in Depo.objects.filter(depochoice=depo)])
    else:
        tasks = Task.objects.filter(user_position=request.user).count()
    conf['task_count'] = tasks


    return render(request, 'cabinet.html', conf)

def task(request, pk):
    conf = dict()
    if request.user.is_authenticated:
        task = get_object_or_404(Task, pk = pk)
        conf['task'] = task
        t = get_object_or_404(Task, pk=pk)
        dep = Depo.objects.filter(task=t)
        conf['depo'] = dep
    return render(request, 'tasks.html', conf)

def machine_approve(request,pk,  pk_depo):
    if request.user.is_authenticated:
        t = get_object_or_404(Depo, pk = pk_depo)
        t.machine_eng_get = True
        t.save()
    return redirect(request.META['HTTP_REFERER'])


def machine_unapprove(request, pk,pk_depo):
    if request.user.is_authenticated:
        t = get_object_or_404(Depo, pk = pk_depo)
        t.machine_eng_pop = True
        t.save()
    return redirect(request.META['HTTP_REFERER'])


def depo_approve(request, pk,pk_depo):
    if request.user.is_authenticated:
        t = get_object_or_404(Depo, pk = pk_depo)
        t.depo_eng_get = True
        t.save()
    return redirect(request.META['HTTP_REFERER'])

def depo_unapprove(request, pk, pk_depo):
    if request.user.is_authenticated:
        t = get_object_or_404(Depo, pk = pk_depo)
        t.depo_eng_pop = True
        t.save()
    return redirect(request.META['HTTP_REFERER'])

def roadmap(request, pk, lk):
    conf = dict()
    if request.user.is_authenticated:
        t = get_object_or_404(Task, pk=lk)
        dep = Depo.objects.filter(task=t)
        conf['depo'] = dep
    return render(request, 'road.html', conf)




# routes for user registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            # form.save only works when form is created from a model
            form.save()
            messages.success(request, 'succesfully created account')
            return redirect('login')
        else:
            # rendering the template again if the form is not valid with the prepopulated data.
            return render(request, 'register.html', {'form': form})

    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def login_user(request):
    # redirect user to home if already logged in
    if request.user.is_authenticated:
        messages.info(request, 'You Are Already Logged In')
        return redirect('/home')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            username = User.objects.filter(email = form.cleaned_data.get('email')).first()
            # the authenticate function returns the user object if the user is found else it returns none
            user = authenticate(username=username, password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
                messages.success(request, 
                f'successfully logged in as {user.username}')
                return redirect('/home')
            else:
                messages.error(request, 'Invalid credentials')
                # form.add_error('user not found')
                return redirect('/login')

        # if form is not valid render the template again with pre populated data
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


@login_required
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'successfully logged out')
        return redirect('/home')


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    email_content = {
                    "email":user.email,
                    'domain': settings.DOMAIN,
                    'site_name': settings.SITE_NAME,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': settings.PROTOCOL,
                    }
                    email = render_to_string(email_template_name, email_content)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
            else:
                messages.error(request, 'email not found in our database')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})
