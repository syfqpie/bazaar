"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

from dj_rest_auth.jwt_auth import get_refresh_view
from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework_simplejwt.views import TokenVerifyView

from customers.views import CustomerViewSet, CustomerRegisterView
from users.views import CustomUserViewSet
from vendors.views import VendorViewSet, VendorRegisterView
from utils.auth.views import (
    MyLoginView, MyRegisterView, MyVerifyEmailView,
    MyResendVerificationView, MyPasswordChangeView,
    MyPasswordResetView, MyPasswordResetConfirmView
)


class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    """
    Nested default router extended from NestedRouterMixin and DefaultRouter 
    """
    pass


router = NestedDefaultRouter()

# Customers
customers_router = router.register(
    r'customers', CustomerViewSet
)

# Users
users_router = router.register(
    r'users', CustomUserViewSet
)

# Vendors
vendors_router = router.register(
    r'vendors', VendorViewSet
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/registration/', MyRegisterView.as_view(), name='public_register'),
    path('auth/registration/customer/', CustomerRegisterView.as_view(), name='customer_register'),
    path('auth/registration/vendor/', VendorRegisterView.as_view(), name='vendor_register'),
    path('auth/registration/verify-email/', MyVerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
        name='account_confirm_email'),
    path('auth/registration/resend-verification/', MyResendVerificationView.as_view(), name='resend_verification'),
    path('auth/login/', MyLoginView.as_view(), name='rest_login'),
    path('auth/logout/', MyLoginView.as_view(), name='rest_logout'),
    path('auth/password/change/', MyPasswordChangeView.as_view(), name='password_change'),
    path('auth/password/reset/', MyPasswordResetView.as_view(), name='rest_password_reset'),
    path(r'auth/password/reset/confirm/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    re_path(r'v1/', include(router.urls)),
]
