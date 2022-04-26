from django.urls import path
from mainapp.views import products, ProductDetail, ProductsList

app_name = 'mainapp'
urlpatterns = [
    # path('', products, name='products'),
    path('', ProductsList.as_view(), name='products'),
    path('category/<int:id_category>/', ProductsList.as_view(), name='category'),
    path('detail/<int:pk>', ProductDetail.as_view(), name='detail'),

]
