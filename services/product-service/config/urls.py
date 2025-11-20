from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.urls import path, include

def health_check(request):
    return JsonResponse({'status': 'healthy', 'service': 'products-service'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check),
    path('api/', include('apps.products.urls')),
]
