from django.urls import path

from . import views


urlpatterns = [
    path('productlist/', views.ProductsListAPIView.as_view()),
    path('history_remove/', views.HistoryRemoveView.as_view()),
    path('history_detail/', views.HistoryDetailView.as_view()),
    path('history_add/', views.HistoryAddView.as_view()),
    # path('history_add2/', views.H),
    path('product_view/', views.ProductCreateAPIView.as_view()),
    path('product_delete/', views.ProductDeleteAPIView.as_view()),
    path('history_clear/', views.HistoryClearView.as_view()),
]