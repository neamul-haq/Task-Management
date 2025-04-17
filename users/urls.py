from django.urls import path
from users.views import sign_up, sign_in, sign_out, activate_user, admin_dashboard, assign_role,create_group, group_list, view_task
from users.views import CustomLoginView, ProfileView, ChangePassword
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView 
# from django.views.generic import TemplateView

urlpatterns = [
    path('sign-up/', sign_up, name='sign-up'),
    # path('sign-in/', sign_in, name='sign-in'),
    path('sign-in/', CustomLoginView.as_view(), name='sign-in'),
    # path('sign-out/', sign_out, name='logout'),
    path('sign-out/', LogoutView.as_view(), name='logout'),
    path('activate/<int:user_id>/<str:token>/', activate_user),
    path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('admin/<int:user_id>/assign-role/', assign_role, name='assign-role'),
    path('admin/create-group/', create_group, name='create-group'),
    path('admin/group-list/', group_list, name='group-list'),
    path('admin/show-tasks/', view_task, name='show-tasks' ),
    #path('profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # path('password-change/', PasswordChangeView.as_view(
    #     template_name='accounts/password_change.html'), name='password-change'),
    path('password-change/', ChangePassword.as_view(), name='password-change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password-change-done')
]