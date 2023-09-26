from django.contrib import admin
from .models import role,userdetail,county,state,city,useraddress,bankdetail

# Register your models here.

class showrole(admin.ModelAdmin):
    list_display = ['id','Usertypename']
admin.site.register(role,showrole)

class showuserdetail(admin.ModelAdmin):
    list_display = ['id','username','userpass','useremail','userphone','urole','u_status']
admin.site.register(userdetail,showuserdetail)

class showcounty(admin.ModelAdmin):
    list_display = ['id','countyname']
admin.site.register(county,showcounty)

class showstate(admin.ModelAdmin):
    list_display = ['id','countyid','statename']
admin.site.register(state,showstate)

class showcity(admin.ModelAdmin):
    list_display = ['id','stateid','cityname']
admin.site.register(city,showcity)

class showuseraddress(admin.ModelAdmin):
    list_display = ['id','userid','buildingname','streetname','pincode','cityname']
admin.site.register(useraddress,showuseraddress)

class showbankdetail(admin.ModelAdmin):
    list_display = ['id','buserdetail','bankname','acnumbr','Endmonth','endyear']
admin.site.register(bankdetail,showbankdetail)
