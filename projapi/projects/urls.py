from django.urls import path, re_path, include
from .views import projects_list, fa_list
from .apiviews import ProjectsAPIview, FAAPIView, ProjectsList

urlpatterns = [
    path("projects/", projects_list, name="projects"),
    path("fa/", fa_list, name="fa"),
    path("projectsAPI/", ProjectsAPIview.as_view(), name="projectsAPI"),
    path("faAPI/", FAAPIView.as_view(), name = "faAPI"),

    path("projectsGeneric/<int:pk>/", ProjectsList.as_view(), name="projectsGeneric")

]