from django.contrib import admin
from django.urls import path
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('encyclopedia/', views.encyclopedia, name='encyclopedia'),
    path('recycle/', views.recycle_bin, name='recycle_bin'),
    
    # روابط الأكشن
    path('clear_history/', views.clear_history, name='clear_history'), # <-- الجديد أهو
    path('delete/<int:id>/', views.soft_delete, name='soft_delete'),
    path('restore/<int:id>/', views.restore_scan, name='restore_scan'),
    path('hard_delete/<int:id>/', views.hard_delete, name='hard_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)