Title: Atlas de Santa Catarina
Section: cartografia-tatil
save_as: cartografia-tatil/atlas-e-mapas/atlas-de-santa-catarina.html
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
    {% set url = '/materiais/didaticos/cartografia-tatil/atlas-sc/' + img %}
    <a href="{static}{{ url }}">
    <img src="{static}{{url}}" style="max-width: 40%; object-fit: cover"/>
    </a>
    {% endfor %}
</div>
{% if loop.index % 1 == 0 %}
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
        'Santa Catarina': {
            'Clima': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sc-clima-tatil.jpg', 
                             'sc-clima-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sc-clima-baixa-visao.jpg',
                             'sc-clima-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Densidade Demográfica': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sc-densidade-demografica-tatil.jpg',
                             'sc-densidade-demografica-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sc-densidade-demografica-baixa-visao.jpg',
                             'sc-densidade-demografica-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Hidrografia': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sc-hidrografia-tatil.jpg',
                             'sc-hidrografia-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sc-hidrografia-baixa-visao.jpg',
                             'sc-hidrografia-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Região': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sc-regiao-tatil.jpg',
                             'sc-regiao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sc-regiao-baixa-visao.jpg',
                             'sc-regiao-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Relevo': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sc-relevo-tatil.jpg',
                             'sc-relevo-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sc-relevo-baixa-visao.jpg',
                             'sc-relevo-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Rodoviário': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sc-rodoviario-tatil.jpg',
                             'sc-rodoviario-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sc-rodoviario-baixa-visao.jpg',
                             'sc-rodoviario-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Vegetação': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sc-vegetacao-tatil.jpg',
                             'sc-vegetacao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sc-vegetacao-baixa-visao.jpg',
                             'sc-vegetacao-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
        }
    }
%}

{% for map, data in maps.items() %}
{{ map_list(map, data) }}
{% endfor %}
