from django.contrib import admin

from .models import Pet, OriginPlace, Tag, MemberManagement
# Register your models here.
admin.site.register(Pet)
admin.site.register(OriginPlace)
admin.site.register(Tag)
admin.site.register(MemberManagement)