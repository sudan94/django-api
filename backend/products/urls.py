from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/',views.ProductDetailAPIView.as_view())
]


# ProductDetailAPIView.as_view()
""""

"""