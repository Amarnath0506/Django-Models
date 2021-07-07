from django.contrib import admin
from .models import Person, Runner, Person1, Group, Membership

# Register your models here.
admin.site.register(Person)
admin.site.register(Runner)
admin.site.register(Person1)
admin.site.register(Group)
admin.site.register(Membership)