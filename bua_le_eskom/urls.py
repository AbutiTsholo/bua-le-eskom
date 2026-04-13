
from django.contrib import admin
from django.urls import path
from reports import views as report_views
from notifications import views as notif_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', report_views.login_view, name='login'),
    path('home/', report_views.home, name='home'),
    path('report/', report_views.report_fault, name='report_fault'),
    path('notifications/', notif_views.notifications, name='notifications'),
    path('register/', report_views.register, name='register'),
    path('logout/', report_views.logout_view, name='logout'),
    path('track/', report_views.track_fault, name='track_fault'),
]
