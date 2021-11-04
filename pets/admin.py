from django.contrib import admin

from .models import Pet, Tag, MemberManagement, Money, Register,Event

# Register your models here.
admin.site.register(Pet)
# admin.site.register(OriginPlace)
admin.site.register(Tag)
admin.site.register(MemberManagement)
admin.site.register(Money)
admin.site.register(Event)


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_pwd', 'user_email')


admin.site.register(Register, RegisterAdmin)
