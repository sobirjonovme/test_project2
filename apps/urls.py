from django.urls import include, path

urlpatterns = [
    path("users/", include("apps.users.urls")),
    path("task2/", include("apps.task2.urls")),
    # path("task2/", include("apps.task2.urls")),
    path("task4/", include("apps.task4.urls")),
]
