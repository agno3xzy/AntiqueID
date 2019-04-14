from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Administrator)
admin.site.register(Classification)
admin.site.register(ExpertHasClassification)
admin.site.register(User)
admin.site.register(Mainpage)
admin.site.register(Commodity)
admin.site.register(Expert)
admin.site.register(ExpertHasCommodity)

