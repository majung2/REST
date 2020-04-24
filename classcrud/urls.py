from django.urls import path
from . import views

urlpatterns = [
    path('',views.BlogView.as_view(),name="list"),
    path('newblog/',views.BlogCreate.as_views(),name="new"),
    path('delete/<int:pk>',views.BlogDetail.as_views(),name='detail'),
    path('update/<int:pk>',views.BlogUpdate.as_views(),name='change'),
    paht('delete/<int:pk>',views.BlogDelete.as_views(),name='del'),

]
