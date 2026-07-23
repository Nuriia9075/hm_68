from django.urls import path
from calculator.views import add, subtract, multiply, divide

app_name = "calculator"
urlpatterns = [
    path('add/', add, name='add'),
    path('subtract/', subtract , name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide')
]