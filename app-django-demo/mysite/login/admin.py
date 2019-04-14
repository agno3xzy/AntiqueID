from django.contrib import admin
from .models import User
from .models import Mainpage
from .models import Commodity
from .models import Expert
from .models import ExpertHasCommodity
# Register your models here.

admin.site.register(User)
admin.site.register(Mainpage)
admin.site.register(Commodity)
admin.site.register(Expert)
admin.site.register(ExpertHasCommodity)
