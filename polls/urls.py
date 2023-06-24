from django.urls import path
from .views import HomeView, VoteView, ResultView, CategoryView, ModalView

app_name = 'polls'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('vote/<int:pk>/', VoteView.as_view(), name='vote'),
    path('result/<str:category>/', ResultView.as_view(), name='result'),
    path('category/<str:category>/', CategoryView.as_view(), name='category'),
    path('modal_content/<int:pk>/', ModalView.as_view(), name='modal_view'),
]
