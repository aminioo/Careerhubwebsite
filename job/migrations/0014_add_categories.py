from django.db import migrations

def add_categories(apps, schema_editor):
    Category = apps.get_model('job', 'Category')
    categories = [
        {
            'name': 'Information Technology',
            'description': 'Jobs in software development, IT support, and technology management',
            'icon': 'fa-laptop-code'
        },
        {
            'name': 'Marketing & Sales',
            'description': 'Jobs in digital marketing, sales, and business development',
            'icon': 'fa-chart-line'
        },
        {
            'name': 'Finance & Accounting',
            'description': 'Jobs in banking, accounting, and financial analysis',
            'icon': 'fa-money-bill-wave'
        },
        {
            'name': 'Healthcare',
            'description': 'Jobs in medical, nursing, and healthcare administration',
            'icon': 'fa-heartbeat'
        },
        {
            'name': 'Education',
            'description': 'Jobs in teaching, training, and educational administration',
            'icon': 'fa-graduation-cap'
        },
        {
            'name': 'Engineering',
            'description': 'Jobs in mechanical, electrical, and civil engineering',
            'icon': 'fa-cogs'
        },
        {
            'name': 'Design & Creative',
            'description': 'Jobs in graphic design, UI/UX, and creative arts',
            'icon': 'fa-palette'
        },
        {
            'name': 'Customer Service',
            'description': 'Jobs in customer support and service management',
            'icon': 'fa-headset'
        },
        {
            'name': 'Human Resources',
            'description': 'Jobs in HR management, recruitment, and employee relations',
            'icon': 'fa-users'
        },
        {
            'name': 'Operations & Logistics',
            'description': 'Jobs in supply chain, operations management, and logistics',
            'icon': 'fa-truck'
        },
        {
            'name': 'Legal',
            'description': 'Jobs in law, compliance, and legal services',
            'icon': 'fa-balance-scale'
        },
        {
            'name': 'Research & Science',
            'description': 'Jobs in scientific research and laboratory work',
            'icon': 'fa-flask'
        },
        {
            'name': 'Media & Communications',
            'description': 'Jobs in journalism, public relations, and media production',
            'icon': 'fa-broadcast-tower'
        },
        {
            'name': 'Hospitality & Tourism',
            'description': 'Jobs in hotels, restaurants, and travel services',
            'icon': 'fa-hotel'
        },
        {
            'name': 'Construction & Real Estate',
            'description': 'Jobs in construction, property management, and real estate',
            'icon': 'fa-building'
        }
    ]
    
    for category in categories:
        Category.objects.get_or_create(
            name=category['name'],
            defaults={
                'description': category['description'],
                'icon': category['icon']
            }
        )

def remove_categories(apps, schema_editor):
    Category = apps.get_model('job', 'Category')
    Category.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('job', '0013_auto_20250427_0022'),
    ]

    operations = [
        migrations.RunPython(add_categories, remove_categories),
    ] 