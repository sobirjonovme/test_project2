from django.urls import include, path

urlpatterns = [
    path("users/", include("apps.users.urls")),
    path("task2/", include("apps.task2.urls")),
]
