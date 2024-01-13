from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, get_verification, RegisterInfo, UserListView, \
    UserUpdateView, UserDetailView, UserDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verification_check/', RegisterInfo.as_view(), name='verification_check'),
    path('email_verify/<str:verification_code>/', get_verification, name='verification'),
    path('verification_approve/', TemplateView.as_view(
            template_name='users/verification_approve.html'), name='verification_approve'),
    path('verification_reject/', TemplateView.as_view(
                template_name='users/verification_reject.html'), name='verification_reject'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('user_update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user_detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user_delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
