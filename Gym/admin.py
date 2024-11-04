from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Member,Trainer,Notification,Attendance



@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

  list_display = ('members_ID','active', 'first_name', 'last_name', 'address', 'age', 'pricing','start_date','end_date')

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'phone_number', 'address', 'active')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email_address',  'message','send_time')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['member',  'date', 'time', 'present']
    search_fields = ['member__first_name', 'member__last_name']