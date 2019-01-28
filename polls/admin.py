"""
  Programa: models.py
  Autor: Osvaldo Larancuent
  Descripcion: Applicacion de encuestas utilizando Django
  Fecha: 27 de enero de 2019
"""
# Register your models here.
from django.contrib import admin

from .models import Question

admin.site.register(Question)

