from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Task, CustomTask, UserProfile, UserTaskCompletion
from .serializers import TaskSerializer, UserProfileSerializer
from .forms import CustomTaskForm, UserRegisterForm, UserLoginForm
from django.contrib.auth.views import LoginView
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from datetime import date
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
from django.db.models import Sum
from django.utils import timezone


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'

def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Jangan buat UserProfile manual jika signal sudah ada
            messages.success(request, "Akun berhasil dibuat! Silakan login.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    form = UserLoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')  
        else:
            messages.error(request, "Username atau password salah!")  
    
    return render(request, 'login.html', {'form':form})

@login_required
def index(request):
    
    try:
        userprofile = request.user
    except UserProfile.DoesNotExist:
        messages.error(request, "Profil tidak ditemukan, silakan registrasi ulang.")
        return redirect('register')
    return render(request, 'index.html', {'user': userprofile})

    # Menambahkan top_players untuk leaderboard
    top_players = UserProfile.objects.select_related('user').order_by('-exp')[:5]

    return render(request, 'index.html', {'user_profile': user_profile, 'top_players': top_players})



def user_logout(request):
    logout(request)
    return redirect('login')

@csrf_exempt 
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    user_profile = request.user.userprofile

    # Check if the task has already been completed by the user
    if UserTaskCompletion.objects.filter(user=user_profile, task=task).exists():
        messages.warning(request, "Tugas ini sudah selesai sebelumnya.")
        return redirect('task_list')

    # Mark the task as completed for the user
    UserTaskCompletion.objects.create(user=user_profile, task=task)
    user_profile.add_exp(task.exp_reward)
    user_profile.save()
    messages.success(request, f"Tugas '{task.title}' selesai! Kamu mendapatkan {task.exp_reward} EXP!")

    return redirect('task_list')


from .models import Task, CustomTask, UserProfile

@login_required
def task_list(request):
    difficulty_filter = request.GET.get('difficulty', None)
    user_profile = request.user.userprofile

    tasks = Task.objects.all().distinct()
    custom_tasks = CustomTask.objects.filter(user=user_profile).distinct()

    if difficulty_filter:
        tasks = tasks.filter(difficulty=difficulty_filter)
        
    completed_tasks = UserTaskCompletion.objects.filter(user=user_profile).values_list('task_id', flat=True)

    # Send the choices from Task model
    difficulty_choices = Task.DIFFICULTY_CHOICES
    
    return render(request, 'task_list.html', {
        'tasks': tasks,
        'custom_tasks': custom_tasks,
        'difficulty_choices': difficulty_choices,
        'completed_tasks': completed_tasks
    })

def create_custom_task(request):        
    if request.method == 'POST':
        form = CustomTaskForm(request.POST)
        if form.is_valid():
            custom_task = form.save(commit=False)
            custom_task.user = request.user.userprofile
            custom_task.save()
            return redirect('task_list')
    else:
        form = CustomTaskForm()
    return render(request, 'custom_tasks.html', {'form': form})

def delete_custom_task(request, task_id):
    task = get_object_or_404(CustomTask, id=task_id)
    task.delete()
    return redirect('task_list')

def leaderboard(request):
    today = now().date()
    # Filter user dengan exp yang bertambah dalam 7 hari terakhir
    top_users = UserProfile.objects.annotate(
        total_exp=Sum('exp')
    ).order_by('-exp')[:5]

    return render(request, 'tasks/leaderboard.html', {'top_users': top_users})


@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'profile.html', {'profile': profile, 'form': form})


    