"""EmailMarketing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Marketing_App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.logins, name='logins'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('clients', views.clients, name='clients'),
    path('page', views.page, name='page'),
    path('admin_register', views.admin_register, name='admin_register'),
    path('admin_details', views.admin_details, name='admin_details'),
    path('adminview/<int:id>', views.adminview, name='adminview'),
    path('update_admin', views.update_admin, name='update_admin'),
    path('invoice', views.invoice, name='invoice'),
    path('productlist', views.productlist, name='productlist'),
    path('add_product/<int:id>', views.add_product, name='add_product'),
    path('update_product', views.update_product, name='update_product'),
    path('payment_details', views.payment_details, name='payment_details'),
    path('product_delete', views.product_delete, name='product_delete'),
    path('product_validity', views.product_validity, name='product_validity'),
    path('admin_buy_product', views.admin_buy_product, name='admin_buy_product'),
    path('templates', views.templates, name='templates'),
    path('view_template/<int:id>', views.view_template, name='view_template'),
    path('temp_delete', views.temp_delete, name='temp_delete'),
    path('settingss/<int:id>', views.settingss, name='settingss'),

    path('invoice_letter/<int:id>', views.invoice_letter, name='invoice_letter'),

    #Admin Part Url
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('admin_invoice', views.admin_invoice, name='admin_invoice'),
    path('client_register', views.client_register, name='client_register'),
    path('admin_client', views.admin_client, name='admin_client'),
    path('admin_clientview/<int:id>', views.admin_clientview, name='admin_clientview'),
    path('update_client', views.update_client, name='update_client'),
    path('admin_productlist', views.admin_productlist, name='admin_productlist'),
    path('admin_product/<int:id>', views.admin_product, name='admin_product'),
    path('admin_update_product', views.admin_update_product, name='admin_update_product'),
    path('admin_product_delete', views.admin_product_delete, name='admin_product_delete'),
    path('client_buy_product', views.client_buy_product, name='client_buy_product'),
    path('admin_payment_details', views.admin_payment_details, name='admin_payment_details'),
    path('admin_customerlist', views.admin_customerlist, name='admin_customerlist'),
    path('admin_template', views.admin_template, name='admin_template'),
    path('admin_setting', views.admin_setting, name='admin_setting'),
    path('client_dashboard', views.client_dashboard, name='client_dashboard'),

    # Client Part Url
    path('client_dashboard', views.client_dashboard, name='client_dashboard'),
    path('client_productlist', views.client_productlist, name='client_productlist'),
    path('customerlist', views.customerlist, name='customerlist'),
    path('customerlists/<str:name>', views.customerlists, name='customerlists'),
    path('add_email/<int:id>', views.add_email, name='add_email'),
    path('email_delete', views.email_delete, name='email_delete'),
    path('client_managegroup', views.client_managegroup, name='client_managegroup'),
    path('contact/<int:id>',views.contact, name='contact'),
    path('client_group_delete',views.client_group_delete, name='client_group_delete'),
    path('client_template', views.client_template, name='client_template'),
    path('client_template_details/<int:cid>', views.client_template_details, name='client_template_details'),
    path('update_client_template_details', views.update_client_template_details, name='update_client_template_details'),
    path('send_email/<int:uid>', views.send_email, name='send_email'),
]

