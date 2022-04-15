from django.urls import path

from adminapp.views import index, admin_users, admin_user_create, admin_user_update, admin_user_delete, \
    admin_user_activate, admin_categories, admin_category_create, admin_category_update, admin_category_delete, \
    admin_category_activate

app_name = 'adminapp'
urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('user-create/', admin_user_create, name='admin_user_create'),
    path('user-update/<int:id>/', admin_user_update, name='admin_user_update'),
    path('user-delete/<int:id>/', admin_user_delete, name='admin_user_delete'),
    path('user-activate/<int:id>/', admin_user_activate, name='admin_user_activate'),
    path('categories/', admin_categories, name='admin_categories'),
    path('category-create/', admin_category_create, name='admin_category_create'),
    path('category-update/<int:id>/', admin_category_update, name='admin_category_update'),
    path('category-delete/<int:id>/', admin_category_delete, name='admin_category_delete'),
    path('category-activate/<int:id>/', admin_category_activate, name='admin_category_activate'),

]
