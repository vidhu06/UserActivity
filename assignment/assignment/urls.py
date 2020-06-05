
from django.contrib import admin
from django.urls import path
from UserActivity import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.UserActivityViewSet.as_view())
]
