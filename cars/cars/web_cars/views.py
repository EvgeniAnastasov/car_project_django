from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView

from cars.web_cars.forms import AddCarForm, EditCarForm, DeleteCarForm
from cars.web_cars.models import Car, Like

UserModel = get_user_model()


def show_index(request):

    cars = Car.objects.all()

    context = {
        'cars': cars,
    }

    return render(request, 'home-with-profile.html', context)


def like_car(request, pk):
    car = Car.objects.get(pk=pk)
    like_object_by_user = car.like_set.filter(user_id=request.user.id).first()
    if like_object_by_user:
        like_object_by_user.delete()
    else:
        like = Like(
            car=car,
            user=request.user,
        )
        like.save()
    return redirect('car details', car.id)


class CarAddView(CreateView):
    form_class = AddCarForm
    template_name = 'add-car.html'
    success_url = reverse_lazy('show index')

    def form_valid(self, form):
        car = form.save(commit=False)
        car.user = self.request.user
        car.save()

        return super().form_valid(form)

# FBV - car_add

# @login_required
# def car_add(request):
#     if request.method == 'POST':
#         form = AddCarForm(request.POST, request.FILES)
#         if form.is_valid:
#             car = form.save(commit=False)
#             car.user = request.user
#             car.save()
#             return redirect('show index')
#     else:
#         form = AddCarForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'add-car.html', context)


@login_required
def car_details(request, pk):

    car = Car.objects.get(pk=pk)

    car.likes_count = car.like_set.count()

    is_owner = car.user == request.user

    is_liked_by_user = car.like_set.filter(user_id=request.user.id).exists()

    context = {
        'car': car,
        'car_brand': car.car_brand,
        'car_model': car.car_model,
        'type': car.type,
        'engine': car.engine,
        'hp': car.hp,
        'transmission': car.transmission,
        'year': car.year,
        'image': car.image,
        'mileage': car.mileage,

        'is_owner': is_owner,
        'is_liked': is_liked_by_user,
    }
    return render(request, 'car-details.html', context)

# class CarDetailsView(DetailView):
#     model = Car
#     template_name = 'car-details.html'
#     context_object_name = 'car'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         # context.update({
#         #     # 'car': car,
#         #     'car_brand': car.car_brand,
#         #     'car_model': car.car_model,
#         #     'type': car.type,
#         #     'engine': car.engine,
#         #     'hp': car.hp,
#         #     'transmission': car.transmission,
#         #     'year': car.year,
#         #     'image': car.image,
#         #     'mileage': car.mileage,
#         # })
#
#         return context


class EditCarView(UpdateView):
    model = Car
    template_name = 'car-edit.html'
    form_class = EditCarForm
    success_url = reverse_lazy('show index')

# FBV - car_edit

# def car_edit(request, pk):
#     car = Car.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = EditCarForm(request.POST, request.FILES, instance=car)
#         if form.is_valid:
#             form.save()
#             return redirect('show index')
#     else:
#         form = EditCarForm(instance=car)
#
#     context = {
#         'form': form,
#         'car': car,
#     }
#
#     return render(request, 'car-edit.html', context)


class DeleteCarView(DeleteView):
    model = Car
    template_name = 'car-delete.html'
    # form_class = DeleteCarForm
    success_url = reverse_lazy('show index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     car = Car.objects.get(pk=pk)
    #
    #     context['car'] = car
    #
    #     return context

# FBV - car_delete:

# def car_delete(request, pk):
#     car = Car.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = DeleteCarForm(request.POST, instance=car)
#         if form.is_valid:
#             form.save()
#             return redirect('show index')
#     else:
#         form = DeleteCarForm(instance=car)
#
#     context = {
#         'form': form,
#         'car': car,
#     }
#
#     return render(request, 'car-delete.html', context)
