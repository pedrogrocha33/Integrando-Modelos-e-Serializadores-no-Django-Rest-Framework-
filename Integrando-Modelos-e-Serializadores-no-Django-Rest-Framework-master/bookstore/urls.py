import debug_toolbar
from bookstore import views
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    re_path(r"^bookstore/(?P<version>(v1|v2))/pedido/", include("order.urls"), name="lista_de_pedidos"),
    re_path(r"^bookstore/(?P<version>(v1|v2))/order/(?P<pk>[^/.]+)/$", views.order_detail, name="order-detail"),
    re_path(r"^bookstore/(?P<version>(v1|v2))/produto/", include("product.urls"), name="lista_de_produtos"),
    re_path(r"^bookstore/(?P<version>(v1|v2))/produto/(?P<pk>[^/.]+)/$", views.product_detail, name="detalhe_do_produto"),
    re_path(r"^bookstore/(?P<version>(v1|v2))/categoria/$", views.category_list, name="lista_de_categorias"),
    re_path(r"^bookstore/(?P<version>(v1|v2))/categoria/(?P<pk>[^/.]+)/$", views.category_detail, name="categoria-detalhe"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("update_server/", views.update, name="update"),
    path('', views.hello_world, name='home'),
]