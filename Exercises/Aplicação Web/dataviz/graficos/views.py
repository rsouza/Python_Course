from django.shortcuts import render, HttpResponse, render_to_response
from django.views import generic
from .models import Grafico, FormularioDoGrafico
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components


# Create your views here.

def index(request):
    context = {'tipos': {'Linha': 'l', 'Barra': 'b'},
               'script': "",
               'div': ""
               }
    if request.method == 'GET':
        context['titulo'] = "Defina um gráfico"
        context['form'] = FormularioDoGrafico()
    elif request.method == 'POST':
        form = FormularioDoGrafico(request.POST)
        context['form'] = form
        if form.is_valid():
            tipo = request.POST.get('tipo', 'l')
            x = request.POST.get('dadosx', [])
            y = request.POST.get('dadosy', [])
            g = Grafico(tipo=tipo, dadosx=x, dadosy=y)
            g.save()
            script, div = cria_grafico(x, y, tipo)
            context.update({'titulo': "Seu gráfico!",
                            'script': script,
                            'div': div
                            })
        else:
            print(form.is_valid())
            pass

    return render(request, 'home.html', context)


def cria_grafico(x, y, tipo):
    x = [float(i) for i in x.strip(',').split(',')]
    y = [float(i) for i in y.strip(',').split(',')]
    if tipo == 'l':
        plot = figure(title="Grafico de linha", x_axis_label='X', y_axis_label='Y', plot_width=800, plot_height=400)
        plot.line(x, y, line_width=2)
    else:
        plot = figure(title="Grafico de Barras", x_axis_label='X', y_axis_label='Y', plot_width=800, plot_height=400)
        plot.vbar(x=x, width=0.9, top=y, bottom=0)

    script, div = components(plot)
    return script, div


class GraficoView(generic.ListView):
    template_name = 'grafico_list.html'
    context_object_name = 'lista_de_graficos'
