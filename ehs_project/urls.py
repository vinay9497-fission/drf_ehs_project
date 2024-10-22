from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ehs_app.urls')),  # This line includes the API routes from ehs_app
]
