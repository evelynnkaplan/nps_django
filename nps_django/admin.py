from django.contrib import admin

from .models import Pass, Passholder, Park, Visit

class PassAdmin(admin.ModelAdmin):
  autocomplete_fields = ['passholder_primary']
  list_display = ['pass_id', 'passholder_primary', 'zip_code', 'type', 'valid', 'expiration_date']
  list_filter = ['type']
  search_fields = ['passholder_primary__first_name', 'passholder_primary__last_name', 'pass_id', 'email', 'online_registration_name']

  def get_fields(self, request, obj=None):
    if obj is None or (obj.type != 'Standard' and obj.type != 'Military'):
      return ['pass_id', 'passholder_primary', 'online_registration_name', 'type', 'expiration_date', 'zip_code', 'email', 'phone_num', 'cost']
    elif obj.type == 'Standard' or obj.type == 'Military':
      return ['pass_id', 'passholder_primary', 'passholder_secondary', 'online_registration_name', 'type', 'expiration_date', 'zip_code', 'email', 'phone_num', 'cost']

class PassInline(admin.TabularInline):
  model = Pass
  exclude = ['passholder_secondary']
  extra = 1

class ParkAdmin(admin.ModelAdmin):
  search_fields = ['name']
  list_filter = ['state']

class VisitAdmin(admin.ModelAdmin):
  autocomplete_fields = ['passholder', 'park']
  list_filter = ['park', 'park__state', 'date']

class VisitInline(admin.TabularInline):
  model = Visit
  extra = 1

class PassholderAdmin(admin.ModelAdmin):
  search_fields = ['first_name', 'last_name']
  list_display = ['first_name', 'last_name']
  inlines = [PassInline, VisitInline]


admin.site.register(Pass, PassAdmin)
admin.site.register(Passholder, PassholderAdmin)
admin.site.register(Park, ParkAdmin)
admin.site.register(Visit, VisitAdmin)