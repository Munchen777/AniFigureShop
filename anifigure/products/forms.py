import re


from django import forms
from .models import Order


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('promocode', 'phone_number', )

    first_name = forms.CharField(max_length=75)
    last_name = forms.CharField(max_length=75)
    delivery_address = forms.CharField(widget=forms.Textarea)
    # requires_delivery = forms.ChoiceField(choices=[
    #     ("0", False), 
    #     ("1", True)
    #     ]
    # )

    def clean_phone_number(self):
        data: str = self.cleaned_data['phone_number']
        # if not data.isdigit():
        #     raise forms.ValidationError("Номер телефона должен содеражать только цифры")

        # Шаблон ориентирован на российские номера + городские с кодом из 3 цифр
        pattern = re.compile(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,15}$')
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")
        return data
