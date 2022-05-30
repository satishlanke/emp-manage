from django.urls import path

from . import views
app_name = 'Bench'
urlpatterns = [
    # path('', views.home, name='home'),
    # path('bench/', views.bench_emp, name='bench_emp'),
    path('manage_emp/', views.manage_emp, name='manage_emp'),
    path('create_emp/', views.create_emp, name='create_emp'),
    path('delete_emp/<int:id>', views.delete_emp, name='delete_emp'),
    path('edit_emp/<int:id>', views.edit_emp, name='edit_emp'),
    
]