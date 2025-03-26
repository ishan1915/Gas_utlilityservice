from django.contrib import admin
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "request_type", "status", "created_at", "updated_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__username", "request_type", "description")
    ordering = ("-created_at",)

admin.site.register(ServiceRequest, ServiceRequestAdmin)
