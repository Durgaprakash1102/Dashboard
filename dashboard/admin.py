from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
# Register your models here.
admin.site.register(Customer)
admin.site.register(Loan)