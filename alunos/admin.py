from django.contrib import admin
from .models import Estado
from .models import Cidade
from .models import Pessoa

admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Pessoa)