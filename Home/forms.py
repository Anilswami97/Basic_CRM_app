from django import forms
from Home.models import Record
# Create your forms here

class CreateRecord(forms.ModelForm):
    first_name = last_name = phone = city = city = state = zipcode = forms.CharField(
        widget= forms.TextInput(attrs={'class':'form-control my-2 border border-3'})
    )

    
    email = forms.CharField(
        widget= forms.EmailInput(attrs={'class':'form-control my-2 border border-3'})
    )
    class Meta:
        model = Record
        fields = ["first_name", "last_name", "email", "phone", "address", "city", "state", "zipcode"]

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}), 
            'address' : forms.Textarea(attrs={'class':'form-control my-2 border border-3', 'rows':3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data