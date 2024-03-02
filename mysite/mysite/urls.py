from django.contrib import admin
from django.urls import path
from myapp.views import (Login, Logout, Register, ProductListView, ProductCreateView, ProductDetailView,
                         ProductUpdateView, PurchaseListView, PurchaseCreateView)
# from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('add/<int:pk>/', PurchaseCreateView.as_view(), name='add'),
    path('my_profile/', PurchaseListView.as_view(), name='profile'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)