from django.contrib import admin

from .models import Pet, Tag, MemberManagement, Money, Register,Event

# Register your models here.
admin.site.register(Pet)
# admin.site.register(OriginPlace)
admin.site.register(Tag)
admin.site.register(MemberManagement)


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_pwd', 'user_email')


admin.site.register(Register, RegisterAdmin)


class MoneyAdmin(admin.ModelAdmin):
    list_display = ('time', 'category', 'item', 'price')


admin.site.register(Money, MoneyAdmin)
