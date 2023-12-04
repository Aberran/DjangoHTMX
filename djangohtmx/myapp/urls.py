from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('submit-form', views.submit_form, name="submit-form"),
    path('more-info/<int:id>', views.more_info, name="more-info"),
    path('delete-card/<int:id>', views.delete_card, name="delete-card"),
]
