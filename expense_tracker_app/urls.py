from django.urls import path
from . import views
urlpatterns = [
    
    path('dashboard',views.dashboard,name='dashboard'),
    path('add_transaction',views.add_transaction,name='add_transaction'),
    path('transaction_list',views.transaction_list,name='transaction_list'),
    path('',views.login_view,name='login_view'),
    path('register',views.register,name='register'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('dlt_data',views.dlt_data,name='dlt_data'),
    
    
]
