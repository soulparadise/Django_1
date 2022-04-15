from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from adminapp.forms import UserAdminRegisterForm, UserAdminUpdateForm, CategoriesAdminCreateForm, \
    CategoriesAdminUpdateForm
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test

from mainapp.models import ProductCategories


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    context = {
        'title': 'GeekShop | Admin'
    }
    return render(request, 'adminapp/admin.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {'title': 'GeekShop | Admin | Users',
               'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {'title': 'GeekShop | Admin | Create User',
               'form': form
               }
    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, id):
    user_select = User.objects.get(id=id)
    if request.method == "POST":
        form = UserAdminUpdateForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
    else:
        form = UserAdminUpdateForm(instance=user_select)
    context = {'title': 'GeekShop | Admin | Edit User',
               'form': form,
               'user_select': user_select
               }
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('adminapp:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_user_activate(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('adminapp:admin_users'))


def admin_categories(request):
    context = {'title': 'GeekShop | Admin | Categories',
               'categories': ProductCategories.objects.all()}
    return render(request, 'adminapp/admin-categories-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_create(request):
    if request.method == 'POST':
        form = CategoriesAdminCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_categories'))
        else:
            print(form.errors)
    else:
        form = CategoriesAdminCreateForm()
    context = {'title': 'GeekShop | Admin | Create Category',
               'form': form
               }
    return render(request, 'adminapp/admin-categories-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_update(request, id):
    category_select = ProductCategories.objects.get(id=id)
    if request.method == "POST":
        form = CategoriesAdminUpdateForm(data=request.POST, instance=category_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_categories'))
    else:
        form = CategoriesAdminUpdateForm(instance=category_select)
    context = {'title': 'GeekShop | Admin | Edit Category',
               'form': form,
               'category_select': category_select
               }
    return render(request, 'adminapp/admin-categories-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, id):
    category = ProductCategories.objects.get(id=id)
    category.is_active = False
    category.save()
    return HttpResponseRedirect(reverse('adminapp:admin_categories'))

@user_passes_test(lambda u: u.is_superuser)
def admin_category_activate(request, id):
    category = ProductCategories.objects.get(id=id)
    category.is_active = True
    category.save()
    return HttpResponseRedirect(reverse('adminapp:admin_categories'))