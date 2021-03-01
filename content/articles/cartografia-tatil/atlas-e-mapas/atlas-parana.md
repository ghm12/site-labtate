Title: Atlas do Paraná
Section: cartografia-tatil
save_as: cartografia-tatil/atlas-e-mapas/atlas-do-parana.html
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
    {% set url = '/materiais/didaticos/cartografia-tatil/atlas-pr/' + img %}
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
        'Paraná': {
            'Clima': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['pr-clima-tatil.jpg', 
                             'pr-clima-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['pr-clima-baixa-visao.jpg',
                             'pr-clima-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Densidade Demográfica': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['pr-densidade-demografica-tatil.jpg',
                             'pr-densidade-demografica-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['pr-densidade-demografica-baixa-visao.jpg',
                             'pr-densidade-demografica-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Hidrografia': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['pr-hidrografia-tatil.jpg',
                             'pr-hidrografia-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['pr-hidrografia-baixa-visao.jpg',
                             'pr-hidrografia-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Região': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['pr-regiao-tatil.jpg',
                             'pr-regiao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['pr-regiao-baixa-visao.jpg',
                             'pr-regiao-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Relevo': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['pr-relevo-tatil.jpg',
                             'pr-relevo-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['pr-relevo-baixa-visao.jpg',
                             'pr-relevo-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Rodoviário': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['pr-rodoviario-tatil.jpg',
                             'pr-rodoviario-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['pr-rodoviario-baixa-visao.jpg',
                             'pr-rodoviario-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Vegetação': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['pr-vegetacao-tatil.jpg',
                             'pr-vegetacao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['pr-vegetacao-baixa-visao.jpg',
                             'pr-vegetacao-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
        }
    }
%}

{% for map, data in maps.items() %}
{{ map_list(map, data) }}
{% endfor %}
