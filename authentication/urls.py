from django.urls import path
from . views import CreateUserView, LoginView, GetUserByIdView, UpdateUserView, DeleteUserView, ProtectedView, LogoutView

urlpatterns = [
    path('api/register/', CreateUserView.as_view(), name='create-user'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/<int:user_id>/', GetUserByIdView.as_view(), name='get-user-id'),
    path('api/<int:user_id>/update/', UpdateUserView.as_view(), name='update-user'),
    path('api/<int:user_id>/delete/', DeleteUserView.as_view(), name='delete-user'),
    
    # Protected User
    path('api/users/protected/', ProtectedView.as_view(), name='protected'),
    
    # Logout 
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
