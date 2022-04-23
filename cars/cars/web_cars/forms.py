from django import forms

from cars.web_cars.models import Car


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('user', )

        labels = {
            'car_brand': 'Car Brand',
            'car_model': 'Car Model',
            'type': 'Type',
            'engine': 'Engine',
            'hp': 'HP',
            'transmission': 'Transmission',
            'year': 'Year',
            'image': 'Image',
            'mileage': 'Mileage',
        }

        widgets = {
            'car_brand': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Car Brand'
                }
            ),
            'car_model': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Car Model'
                }
            ),
            'hp': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Horse Power'
                }
            ),
            'year': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Year Of Production'
                }
            ),
            'mileage': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Mileage'
                }
            ),
        }


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class DeleteCarForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Car
        fields = '__all__'


