from django.urls import path
from . import views
urlpatterns = [
    path('',views.show , name='show'),
    path('edit_musician/<int:id>',views.Edit_musician.as_view() , name='edit_musician'),
]