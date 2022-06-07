from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/',views.ProductDetailAPIView.as_view()),
    path('create/',views.product_create_view),
    path('',views.product_list_create_view)


]


# ProductDetailAPIView.as_view()
""""

"""