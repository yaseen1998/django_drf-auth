
from django.urls import path
from .views import AddListView,DetailAddView

urlpatterns = [
    path('',AddListView.as_view(),name= 'add_data'),
    path('<int:pk>',DetailAddView.as_view(),name = 'detail_data')
]