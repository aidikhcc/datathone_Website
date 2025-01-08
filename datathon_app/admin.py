from django.contrib import admin
from .models import Participant, Sponsor

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'nationality', 'event_choice', 
                   'payment_status', 'registration_date')
    list_filter = ('event_choice', 'payment_status', 'nationality',
                  'wadi_rum_trip', 'falafel_dinner', 'kickboxing_session')
    search_fields = ('full_name', 'email', 'phone')
    readonly_fields = ('registration_date', 'last_updated')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'email', 'phone', 'nationality')
        }),
        ('Event Details', {
            'fields': ('event_choice', 'payment_status', 'skills')
        }),
        ('Social Media', {
            'fields': ('slack_username', 'discord_username', 'linkedin', 'twitter'),
            'classes': ('collapse',)
        }),
        ('Social Activities', {
            'fields': ('wadi_rum_trip', 'falafel_dinner', 'kickboxing_session')
        }),
        ('System Fields', {
            'fields': ('registration_date', 'last_updated'),
            'classes': ('collapse',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('email',)
        return self.readonly_fields


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'tier', 'contact_person', 'is_active')
    list_filter = ('tier', 'is_active')
    search_fields = ('name', 'contact_person', 'contact_email')
    
    fieldsets = (
        ('Sponsor Information', {
            'fields': ('name', 'logo', 'website', 'description', 'tier')
        }),
        ('Contact Details', {
            'fields': ('contact_person', 'contact_email', 'contact_phone')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('created_at', 'updated_at')
        return ()
