from django.urls import path
from .views import LoginAPIView, LogoutAPIView, SignupAPIView, ForgotPasswordAPIView, ChangePasswordAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('forgot-password/', ForgotPasswordAPIView.as_view(), name='forgot_password'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='change_password'),
]