from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.SimpleRouter()

urlpatterns = [
    path('', lambda req: redirect('/admin/')),

    path(
        'admin/password_reset/',
        auth_views.PasswordResetView.as_view(from_email=settings.ADMIN_EMAIL),
        name='admin_password_reset',
    ),
    path(
        'admin/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),

    path('api/v1/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/v1/', include((router.urls, 'api_v1'))),

    path('admin/', admin.site.urls)
]
