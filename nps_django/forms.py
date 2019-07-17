from django import forms
from .models import Pass

class PassForm(forms.ModelForm):
  class Meta:
    model = Pass
    fields = ['pass_id', 'online_registration_name', 'type', 'expiration_date', 'zip_code', 'email', 'phone_num']
    widgets = {
            'expiration_date': forms.SelectDateWidget()
        }