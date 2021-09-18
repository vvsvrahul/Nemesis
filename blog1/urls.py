from django.urls import path
from blog1 import views
app_name = 'blog1'
urlpatterns = [
            # path('',views.landing,name= 'landing'),
            path('loggedin/',views.next1,name= 'after'),
            path('signup/',views.registration,name='signup'),
            path('congo/',views.congo,name='congo'),
            path('',views.userlogin,name='login'),
            path('blogs/',views.postmaker,name='blogs'),
            path('update/<str:pk>',views.update,name='update'),
            path('delete/<str:pk>',views.Delete,name='delete'),
            path('logout/',views.userlogout,name='logout'),
      


]
