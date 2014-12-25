from django import forms
from rango.models import Page, Category
#import pdb;pdb.set_trace()
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=120, help_text="Please enter the category name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Association between model and ModelForm
        model = Category

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title")
    url = forms.URLField(max_length=200, help_text="Please enter the url")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Page
        fields = ('title', 'url' , 'views')



        
