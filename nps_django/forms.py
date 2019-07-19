from django import forms
from .models import Pass
from django.core.exceptions import ValidationError

class PassForm(forms.ModelForm):
  class Meta:
    model = Pass
    fields = ['pass_id', 'online_registration_name', 'type', 'expiration_date', 'zip_code', 'email', 'phone_num']
    widgets = {
            'expiration_date': forms.SelectDateWidget()
        }
  
  def clean(self):
    cleaned_data = super().clean()
    expiration_date = cleaned_data.get("expiration_date")
    type = cleaned_data.get("type")

    if type != "Senior Lifetime" and not expiration_date:
      error_message = "Please enter an expiration date. The only pass type without an expiration date are Senior Lifetime passes."
      raise ValidationError(error_message, code='invalid')