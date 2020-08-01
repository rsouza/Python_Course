from django.db import models
from django.forms import ModelForm, ValidationError


# Create your models here.

class Grafico(models.Model):
    tipo = models.CharField(max_length=16, choices=[('l','linha'),('b','barra')])
    dadosx = models.CharField(max_length=1000,null=False)
    dadosy = models.CharField(max_length=1000,null=False)

class FormularioDoGrafico(ModelForm):
    class Meta:
        model = Grafico
        fields = ['tipo', 'dadosx', 'dadosy']
        labels = {
            'tipo': 'Tipo',
            'dadosx': "Valores de x",
            'dadosy': "Valores de y"
        }
        # help_texts = {
        #     'tipo': 'Escolha o tipo do gráfico',
        #     'dadosx': 'Entre com os valores de x'
        # }
        # error_messages = {
        #     'tipo': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }

    def clean_dadosx(self):
        dadosx = self.cleaned_data['dadosx']

        try:
            x = [float(i) for i in dadosx.strip(',').split(',')]
        except:
            raise ValidationError("Formataçao inválida para valores de x")
        return dadosx

    def clean_dadosy(self):
        dadosy = self.cleaned_data['dadosy']
        try:
            y = [float(i) for i in dadosy.strip(',').split(',')]
        except:
            raise ValidationError("Formataçao inválida para valores de y")
        return dadosy
