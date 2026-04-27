from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'skills', views.SkillViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'services', views.ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', views.contact_api, name='contact_api'),
    path('portfolio-data/', views.portfolio_data, name='portfolio_data'),
    # Additional JSON APIs
    path('contact-json/', views.contact_json, name='contact_json'),
    path('projects-json/', views.projects_api, name='projects_json'),
    path('skills-json/', views.skills_api, name='skills_json'),
    path('visitors/', views.visitor_count_api, name='visitors'),
    path('resume/download/', views.download_resume, name='resume'),
]
