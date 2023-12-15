from django.urls import path
from . import views
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/',views.Index.as_view(),name='index'),
    path('register/',views.Register,name='register'),
    path('login/',views.User_login.as_view(),name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('delete_mode/<int:id>',views.Delete_model.as_view(),name='delete_model'),
    path('edit_album/<int:id>',views.Edit_album.as_view(),name='edit_album'),
]