from django.contrib import admin
from .models import Owner, Pet, Appointment

class PetInline(admin.TabularInline):
    model = Pet
    extra = 1


class AppointmentInline(admin.TabularInline):
    model = Appointment
    extra = 1


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')
    inlines = [PetInline]


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'owner', 'birth_date')
    list_filter = ('species',)
    inlines = [AppointmentInline]


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pet', 'date', 'reason', 'created_at')
    list_filter = ('date',)


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Appointment, AppointmentAdmin)