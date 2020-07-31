Title: Brasil - Poligono das Secas
Section: cartografia-tatil
save_as: cartografia-tatil/mapas-tateis-para-o-ensino/brasil-poligono-das-secas.html
Tags: recursos-didaticos

(Clique nas imagens para abri-la)

{%
    macro map_list(region, categories)
-%}
## {{region}}

{% for category, maps in categories.items() %}

### {{ category }}

<div class="row justify-content-md-center">
{% for map in maps %}
    {% set title = map['title'] %}
    {% set imgs = map['imgs'] %}
    {% set size = map['size'] %}

<div class="col text-center">
    <div class="text-center">{{ title }}</div>
    {% for img in imgs %}
    {% set url = '/materiais/didaticos/cartografia-tatil/mapas-tateis-para-o-ensino/' + img %}
    <a href="{static}{{ url }}">
    <img src="{static}{{url}}" style="max-width: 50%; object-fit: cover"/>
    </a>
    {% endfor %}
</div>
{% if loop.index % 2 == 0 %}
<div class="w-100">
</div>
{% endif %}
    {% endfor %}
</div>
<br>
<br>
{% endfor %}

{%
    endmacro
-%}

{%
    set maps = {
        'Brasil - Poligono das Secas': {
            '': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['brasil-poligono-das-secas-tatil.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['brasil-poligono-das-secas-baixa-visao.jpg',
                             'brasil-poligono-das-secas-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa Microcapsulado',
                    'imgs': ['brasil-poligono-das-secas-microcapsulado.jpg',
                             'brasil-poligono-das-secas-microcapsulado-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ]
        }
    }
%}

{% for map, data in maps.items() %}
{{ map_list(map, data) }}
{% endfor %}
