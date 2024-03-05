"""bike_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from bike_store_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_home',views.admin_home),
    path('',views.view_index),
    path('loginform_post',views.loginform_post),
    path('view_shops',views.view_shops),
    path('approve_shop/<id>',views.approve_shop),
    path('reject_shop/<id>',views.reject_shop),
    path('add_service',views.add_service),
    path('add_service_post',views.add_service_post),
    path('view_service',views.view_service),
    path('delete_service/<id>',views.delete_service),
    path('view_users',views.view_users),
    path('view_complaints',views.view_complaints),
    path('reply/<id>',views.reply),
    path('reply_post/<id>',views.reply_post),
    path('view_rating',views.view_rating),
    path('add_parts',views.add_parts),
    path('add_parts_post',views.add_parts_post),
    path('view_parts_cat',views.view_parts_cat),
    path('delete_parts_category/<id>',views.delete_parts_category),
    path('change_password',views.change_password),
    path('change_password_post',views.change_password_post),
    path('admin_index',views.admin_index),


###################################################################

    path('shop_home',views.shop_home),
    path('register_shop',views.register_shop),
    path('register_shop_post',views.register_shop_post),
    path('view_profile',views.view_profile),
    path('add_bike',views.add_bike),
    path('add_bike_post',views.add_bike_post),
    path('view_bike',views.view_bike),
    path('update_bike/<id>',views.update_bike),
    path('update_bike_post/<id>',views.update_bike_post),
    path('delete_bike/<id>',views.delete_bike),
    path('view_parts_category',views.view_parts_category),
    path('add_partss',views.add_partss),
    path('add_partss_post',views.add_partss_post),
    path('view_parts',views.view_parts),
    path('update_parts/<id>',views.update_parts),
    path('update_parts_post/<id>',views.update_parts_post),
    path('delete_parts/<id>',views.delete_parts),
    path('view_bike_request',views.view_bike_request),
    path('approve_bike_request/<id>',views.approve_bike_request),
    path('reject_bike_request/<id>',views.reject_bike_request),
    path('view_services',views.view_services),
    path('add_own_Service/<id>',views.add_own_Service),
    path('add_own_Service_post/<sid>',views.add_own_Service_post),
    path('view_service_request',views.view_service_request),
    path('approve_service_request/<id>',views.approve_service_request),
    path('reject_service_request/<id>',views.reject_service_request),
    path('view_part_request',views.view_part_request),
    path('view_part_items/<id>',views.view_part_items),
    path('view_payment_shop',views.view_payment_shop),
    path('shop_index',views.shop_index),



# ========================================================================================================
    path('login_user',views.login_user),
    path('register_user',views.register_user),
    path('view_profile_user',views.view_profile_user),
    path('send_request_service',views.send_request_service),
    path('view_bikes',views.view_bikes),
    path('send_bike_request',views.send_bike_request),
    path('view_partss',views.view_partss),
    path('add_to_cart_parts',views.add_to_cart_parts),
    path('view_previous_order',views.view_previous_order),
    path('send_review',views.send_review),
    path('send_complaint',views.send_complaint),
    path('view_reply',views.view_reply),
    path('logout',views.logout),
    path('view_servicess',views.view_servicess),
    path('view_cart',views.view_cart),
    path('offline_payment',views.offline_payment),
    path('online_payment',views.online_payment),



]
