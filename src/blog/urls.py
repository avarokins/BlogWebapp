from django.urls import path
from .views import (
    blog_detail_view,
    blog_list_view,
    blog_create_view,
    blog_update_view,
    blog_delete_view
    )

urlpatterns = [
    path('', blog_list_view),
    path('<str:slug>/', blog_detail_view),
    path('<str:slug>/edit/', blog_update_view),
    path('<str:slug>/delete/', blog_delete_view),
]
