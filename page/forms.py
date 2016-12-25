from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder':'Nombre','class':'u-full-width'})
    )
    contact_email = forms.EmailField(
        required=True,
        label="",
        widget=forms.EmailInput(attrs={'placeholder':'Email','class':'u-full-width'})
    )
    content = forms.CharField(
        required=True,
        label="",
        widget=forms.Textarea(attrs={'placeholder':'Mensaje','class':'u-full-width'})
    )
