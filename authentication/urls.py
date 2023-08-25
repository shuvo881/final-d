from django.urls import path
from .views import login_view, register_view, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, logout_view
from dashboard.views import dashboard_view


urlpatterns = [
    path('', login_view, name='login_view'),
    path('signup/', register_view, name='register_view'),
    path('logout/', logout_view, name='logout_view'),


    # password recovery urls
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # --------------
    path('dashboard', dashboard_view, name='dashboard_view')

]
