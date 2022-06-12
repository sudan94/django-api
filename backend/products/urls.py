from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/',views.ProductDetailAPIView.as_view()),
    path('<int:pk>/update',views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete',views.product_destroy_view),

    path('create/',views.product_create_view),
    path('',views.product_list_create_view)


]


# ProductDetailAPIView.as_view()
""""

"""