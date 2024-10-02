"""
URL configuration for DashboardNew project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from dashboard.views import signup, verify_otp, login_view, dashboard
from dashboard.views import team_1_dashboard, team_2_dashboard, team_3_dashboard, team_4_dashboard, super_admin_dashboard, logout_view,home
from dashboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('team-1-dashboard/', team_1_dashboard, name='team_1_dashboard'),
    path('team1/update/<int:customer_id>/', update_interest_status, name='update_interest_status'),
    path('team-2-dashboard/', team_2_dashboard, name='team_2_dashboard'),
    path('update-eligibility-status/<int:customer_id>/',update_eligibility_status, name='update_eligibility_status'),
    path('team-3-dashboard/', team_3_dashboard, name='team_3_dashboard'),
    path('update-emi-status/<str:loan_id>/', update_emi_status, name='update_emi_status'),
    path('extend-due-date/<str:loan_id>/', extend_due_date, name='extend_due_date'),
    path('critical-loans/', critical_loans, name='critical_loans'),
    path('update-visit-details/<int:loan_id>/', update_visit_details, name='update_visit_details'),
    path('mark-emi-cleared/<int:loan_id>/', mark_emi_cleared, name='mark_emi_cleared'),
    path('team-4-dashboard/', team_4_dashboard, name='team_4_dashboard'),
    path('upload-loan-details/', upload_loan_details, name='upload_loan_details'),
    path('upload-customer-details/', upload_customer_details, name='upload_customer_details'),
    path('manager_view-customers/', manager_view_customers, name='manager_view_customers'),
    path('manager_view-loans/', manager_view_loans, name='manager_view_loans'),
    path('manager_view-users/', manager_view_users, name='manager_view_users'),
    path('create_users/',manager_create_user,name='manager_create_users'),
    path('delete_user/<int:user_id>/', manager_delete_user, name='manager_delete_user'),
    path('super-admin-dashboard/', super_admin_dashboard, name='super_admin_dashboard'),
     path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
    path('create-user/', create_user, name='create_user'),
     path('view-customers/', view_customers, name='view_customers'),
    path('view-loans/', view_loans, name='view_loans'),
    path('view-users/', view_users, name='view_users'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),
    path('popup/', popup_view, name='popup'),
]
