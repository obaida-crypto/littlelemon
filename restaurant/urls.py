from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemsView.as_view(), name='single_menu'),
    path('booking/',include(router.urls)),
    
]  