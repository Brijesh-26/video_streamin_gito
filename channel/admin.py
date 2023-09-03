from django.contrib import admin
from .models import Channel, Community, CommunityComment

# Register your models here.
admin.site.register(Channel)
admin.site.register(Community)
admin.site.register(CommunityComment)
