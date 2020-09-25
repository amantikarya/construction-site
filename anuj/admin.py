from django.contrib import admin
from .models import Gallery
from .models import Ourteam
from .models import reviews
from .models import Customer
from .models import projects
# Register your models here.
admin.site.register(Gallery)
admin.site.register(Ourteam)
admin.site.register(reviews)
admin.site.register(Customer)
admin.site.register(projects)