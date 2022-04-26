from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView

from cars.accounts.forms import LoginForm, ProfileForm, RegisterForm
from cars.accounts.models import Profile
from cars.web_cars.models import Car


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('show index')
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('show index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

# FBV - register:

# def register_user(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('show index')
#     else:
#         form = RegisterForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'accounts/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('show index')


# class ProfileDetailsView(FormView):
#     template_name = 'accounts/profile-details.html'
#     form_class = ProfileForm
#     success_url = reverse_lazy('profile details')
#     object = None
#
#     # def get_form(self, form_class=None):
#     #     """
#     #     Check if the user already saved contact details. If so, then show
#     #     the form populated with those details, to let user change them.
#     #     """
#     #     try:
#     #         profile = Profile.objects.get(user=self.request.user)
#     #         return form_class(instance=profile, **self.get_form_kwargs())
#     #     except Profile.DoesNotExist:
#     #         return form_class(**self.get_form_kwargs())
#
#     def get_form(self, form_class=None):
#         """Return an instance of the form to be used in this view."""
#         if form_class is None:
#             form_class = self.get_form_class()
#         return form_class(**self.get_form_kwargs())
#
#     def get(self, request, *args, **kwargs):
#         self.object = Profile.objects.get(pk=self.request.user.id)
#         return super().get(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         self.object = Profile.objects.get(pk=self.request.user.id)
#         if form.is_valid():
#             form.save(kwargs.get('pk'))
#         return super().post(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         self.object.profile_image = form.cleaned_data['profile_image']
#         self.object.first_name = form.cleaned_data['first_name']
#         self.object.last_name = form.cleaned_data['last_name']
#         self.object.save()
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         user_cars = Car.objects.filter(user_id=self.request.user.id)
#
#         context['profile'] = self.object
#         context['cars'] = user_cars
#
#         return context

class ProfileDetailsView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/profile-details.html'
    form_class = ProfileForm
    model = Profile
    success_url = reverse_lazy('profile details')

    def get_object(self, queryset=None):
        return Profile.objects.get(user_id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_cars = Car.objects.filter(user_id=self.request.user.id)

        user_total_cars = len(user_cars)

        context['cars'] = user_cars
        context['user_total_cars'] = user_total_cars

        return context

# FBV - profile_details:

# @login_required
# def profile_details(request):
#     profile = Profile.objects.get(pk=request.user.id)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile details')
#     else:
#         form = ProfileForm(instance=profile)
#
#     user_cars = Car.objects.filter(user_id=request.user.id)
#
#     context = {
#         'form': form,
#         'cars': user_cars,
#         'profile': profile,
#     }
#     return render(request, 'accounts/profile-details.html', context)
