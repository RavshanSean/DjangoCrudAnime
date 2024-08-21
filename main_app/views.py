from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ninja, Weapon


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def ninja_index(request):
    ninjas = Ninja.objects.filter(user=request.user) #each see his cats
    return render(request, 'ninjas/index.html', { 'ninjas': ninjas })

@login_required
def ninja_detail(request, ninja_id):
    ninja = Ninja.objects.get(id=ninja_id)
    weapons_ninja_doesnt_have = Weapon.objects.exclude(id__in = ninja.weapons.all().values_list('id'))
    
    return render(request, 'ninjas/detail.html', {'ninja': ninja, 'weapons': weapons_ninja_doesnt_have})

class NinjaCreate(LoginRequiredMixin, CreateView):
    model = Ninja
    fields = ['name', 'clan', 'description', 'age', 'chakra']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class NinjaUpdate(LoginRequiredMixin, UpdateView):
    model = Ninja
    fields = ['name', 'clan', 'description', 'age', 'chakra']

class NinjaDelete(LoginRequiredMixin, DeleteView):
    model = Ninja
    success_url = '/ninjas/'

class WeaponCreate(LoginRequiredMixin, CreateView):
    model = Weapon
    fields = '__all__'

class WeaponList(LoginRequiredMixin, ListView):
    model = Weapon

class WeaponDetail(LoginRequiredMixin, DetailView):
    model = Weapon
    
class WeaponUpdate(LoginRequiredMixin, UpdateView):
    model = Weapon
    fields = ['name', 'color']

class WeaponDelete(LoginRequiredMixin, DeleteView):
    model = Weapon
    success_url = '/weapons/'

@login_required    
def associate_weapon(request, ninja_id, weapon_id):
    Ninja.objects.get(id=ninja_id).weapons.add(weapon_id)
    return redirect('ninja-detail', ninja_id=ninja_id)

@login_required
def remove_weapon(request, ninja_id, weapon_id):
    ninja = Ninja.objects.get(id=ninja_id)
    weapon = Weapon.objects.get(id=weapon_id)
    ninja.weapons.remove(weapon)
    return redirect('ninja-detail', ninja_id=ninja.id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('ninja-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )