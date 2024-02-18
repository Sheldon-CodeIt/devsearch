from django.urls import path
from . import views

# alternative imports:
# from . import views --> path(...., views.project) 
# from views import projects, project

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project")
]
