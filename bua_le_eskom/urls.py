
from django.contrib import admin
from django.urls import path
from reports import views as report_views
from notifications import views as notif_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', report_views.home, name='home'),
    path('report/', report_views.report_fault, name='report_fault'),
    path('notifications/', notif_views.notifications, name='notifications'),
]