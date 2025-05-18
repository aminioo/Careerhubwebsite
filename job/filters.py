import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    salary_min = django_filters.NumberFilter(field_name='salary', lookup_expr='gte')
    salary_max = django_filters.NumberFilter(field_name='salary', lookup_expr='lte')
    
    class Meta:
        model = Job
        fields = '__all__'
        exclude = [
            'owner', 'published_at', 'image', 'slug',
            'description', 'requirements', 'responsibilities',
            'vacancy', 'is_featured', 'skills',
            'experience', 'experience_min', 'experience_max' , 'company_description','is_active','salary'
        ]