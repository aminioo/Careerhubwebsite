from django import forms

from .models import Apply, Job, Category




class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name' ,'email','website','cv','cover_letter']



class JobForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select a category",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Job
        fields = [
            'title', 'company_name', 'company_description', 'location',
            'job_type', 'job_level', 'description', 'requirements',
            'responsibilities', 'vacancy', 'salary',
            'experience_min', 'experience_max', 'category', 'image',
            'is_featured', 'is_active', 'skills'
        ]
        exclude = ('owner', 'slug')