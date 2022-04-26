from django.urls import path

from authapp.views import LoginUserView, RegisterUserView, Logout, ProfileFormView

app_name = 'authapp'
urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),

    path('verify/<str:email>/<str:activate_key>', RegisterUserView.verify, name='verify')
]