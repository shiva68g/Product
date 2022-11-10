


from django.urls import path
from .views import *
urlpatterns = [
   path('products' ,Product.as_view()),
   path('productDetailWithId/<int:id>',Product_With_id.as_view()),
]