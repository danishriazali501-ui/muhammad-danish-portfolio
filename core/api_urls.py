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
]
