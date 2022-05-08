from django.urls import path

from adminapp.views import IndexTemplateView, AdminUsersView, AdminUserCreate, AdminUserUpdate, \
    AdminUserActivateDeactivate, AdminUserDelete, AdminCategoryView, AdminCategoryCreate, AdminCategoryUpdate, \
    AdminCategoryActivateDeactivate, AdminCategoryDelete, AdminProductView, AdminProductCreate, AdminProductUpdate, \
    AdminProductActivateDeactivate, AdminProductDelete

app_name = 'adminapp'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('users/', AdminUsersView.as_view(), name='admin_users'),
    path('user-create/', AdminUserCreate.as_view(), name='admin_user_create'),
    path('user-update/<int:pk>/', AdminUserUpdate.as_view(), name='admin_user_update'),
    path('user-activate-deactivate/<int:pk>/', AdminUserActivateDeactivate.as_view(),
         name='admin_user_activate_deactivate'),
    path('user-delete/<int:pk>/', AdminUserDelete.as_view(), name='admin_user_delete'),
    path('categories/', AdminCategoryView.as_view(), name='admin_categories'),
    path('category-create/', AdminCategoryCreate.as_view(), name='admin_category_create'),
    path('category-update/<int:pk>/', AdminCategoryUpdate.as_view(), name='admin_category_update'),
    path('category-activate-deactivate/<int:pk>/', AdminCategoryActivateDeactivate.as_view(),
         name='admin_category_activate_deactivate'),
    path('category-delete/<int:pk>/', AdminCategoryDelete.as_view(), name='admin_category_delete'),
    path('products/', AdminProductView.as_view(), name='admin_products'),
    path('product-create/', AdminProductCreate.as_view(), name='admin_product_create'),
    path('product-update/<int:pk>/', AdminProductUpdate.as_view(), name='admin_product_update'),

    path('product-activate-deactivate/<int:pk>/', AdminProductActivateDeactivate.as_view(), name='admin_product_activate_deactivate'),
    path('product-delete/<int:pk>/', AdminProductDelete.as_view(), name='admin_product_delete'),

]
