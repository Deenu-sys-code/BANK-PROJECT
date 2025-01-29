from django.urls import path
from . import views 

urlpatterns=[
    path('',views.app_reg,name='app_reg'),
    path('log/',views.app_log,name='app_log'),
    path('cs/',views.Customer_login,name='UI'),
    path('cc/',views.Customer_Creation,name='Customer_Creation'),
    path('bi/',views.Bank_UI,name='Bank_UI'),
    path('da/',views.Deposit_Amount,name='Deposit_Amount'),
    path('logout/',views.Logout_user,name='Logout_user'),
    path('wa/',views.Withdrawn_amount,name='Withdrawn_amount'),
    path('th/',views.Transaction_history,name='Transaction_history'),
    path('ba/',views.Balance,name='Balance'),
    path('ho/',views.Home,name='Home'),
    path('st/',views.Statement,name='Statement')

]