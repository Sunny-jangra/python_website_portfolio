from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),

    # ✅ Like + Comment
    path('projects/<int:pk>/like/', views.toggle_like, name='toggle_like'),
    path('projects/<int:pk>/comment/', views.add_comment, name='add_comment'),

    # ✅ pages
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
]
