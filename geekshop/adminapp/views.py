from django.http import HttpResponseRedirect

# Create your views here.
from django.urls import reverse_lazy
from adminapp.forms import UserAdminRegisterForm, UserAdminUpdateForm, CategoriesAdminCreateForm, \
    CategoriesAdminUpdateForm, ProductAdminCreateForm, ProductAdminUpdateForm
from authapp.models import User
from mainapp.models import ProductCategories, Product
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, TemplateView, CreateView
from adminapp.mixin import BaseClassContextMixin, CustomDispatchMixin, UserDispatchMixin


class IndexTemplateView(TemplateView, BaseClassContextMixin):
    template_name = 'adminapp/admin.html'
    title = 'GeekShop | Admin'


class AdminUsersView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    context_object_name = 'users'
    title = 'GeekShop | Admin | Users'


class AdminUserCreate(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    title = 'GeekShop | Admin | Create User'
    success_url = reverse_lazy('adminapp:admin_users')


class AdminUserUpdate(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminUpdateForm
    title = 'GeekShop | Admin | Edit User'
    success_url = reverse_lazy('adminapp:admin_users')


class AdminUserActivateDeactivate(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminUpdateForm
    success_url = reverse_lazy('adminapp:admin_users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AdminUserDelete(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminUpdateForm
    success_url = reverse_lazy('adminapp:admin_users')


class AdminCategoryView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-categories-read.html'
    context_object_name = 'categories'
    title = 'GeekShop | Admin | Categories'


class AdminCategoryCreate(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-categories-create.html'
    form_class = CategoriesAdminCreateForm
    title = 'GeekShop | Admin | Create Category'
    success_url = reverse_lazy('adminapp:admin_categories')


class AdminCategoryUpdate(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-categories-update-delete.html'
    form_class = CategoriesAdminUpdateForm
    title = 'GeekShop | Admin | Edit Category'
    success_url = reverse_lazy('adminapp:admin_categories')


class AdminCategoryActivateDeactivate(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-categories-update-delete.html'
    form_class = CategoriesAdminUpdateForm
    success_url = reverse_lazy('adminapp:admin_categories')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AdminCategoryDelete(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-categories-update-delete.html'
    form_class = CategoriesAdminUpdateForm
    success_url = reverse_lazy('adminapp:admin_categories')


class AdminProductView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-read.html'
    context_object_name = 'products'
    title = 'GeekShop | Admin | Products'


class AdminProductCreate(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-create.html'
    form_class = ProductAdminCreateForm
    title = 'GeekShop | Admin | Create Product'
    success_url = reverse_lazy('adminapp:admin_products')


class AdminProductUpdate(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = ProductAdminUpdateForm
    title = 'GeekShop | Admin | Edit Product'
    success_url = reverse_lazy('adminapp:admin_products')


class AdminProductActivateDeactivate(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = ProductAdminUpdateForm
    success_url = reverse_lazy('adminapp:admin_products')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class AdminProductDelete(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = ProductAdminUpdateForm
    success_url = reverse_lazy('adminapp:admin_products')


