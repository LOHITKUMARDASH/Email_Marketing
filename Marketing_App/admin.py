from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(NewUser)
admin.site.register(product)
admin.site.register(invoice_settings)
admin.site.register(fileuploads)
admin.site.register(Invoice)
admin.site.register(group)
admin.site.register(template)
admin.site.register(customers)

