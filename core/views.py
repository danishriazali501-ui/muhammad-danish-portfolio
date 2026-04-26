from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Skill, Project, Service, ContactMessage
from .serializers import SkillSerializer, ProjectSerializer, ServiceSerializer, ContactMessageSerializer


def home(request):
    skills = Skill.objects.filter(is_active=True)
    projects = Project.objects.filter(is_active=True)
    services = Service.objects.filter(is_active=True)
    context = {
        'skills': skills,
        'projects': projects,
        'services': services,
    }
    return render(request, 'main/index.html', context)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.filter(is_active=True)
    serializer_class = SkillSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


@api_view(['POST'])
def contact_api(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Message received — I will respond within 24 hours.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def portfolio_data(request):
    skills = Skill.objects.filter(is_active=True)
    projects = Project.objects.filter(is_active=True)
    services = Service.objects.filter(is_active=True)
    data = {
        'skills': SkillSerializer(skills, many=True).data,
        'projects': ProjectSerializer(projects, many=True).data,
        'services': ServiceSerializer(services, many=True).data,
    }
    return Response(data)
