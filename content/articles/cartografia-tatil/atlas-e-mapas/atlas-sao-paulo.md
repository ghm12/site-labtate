Title: Atlas de São Paulo
Section: cartografia-tatil
save_as: cartografia-tatil/atlas-e-mapas/atlas-de-sao-paulo.html
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
    {% set url = '/materiais/didaticos/cartografia-tatil/atlas-sp/' + img %}
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
                    'imgs': ['sp-clima-tatil.jpg', 
                             'sp-clima-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sp-clima-baixa-visao.jpg',
                             'sp-clima-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'População': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sp-populacao-tatil.jpg',
                             'sp-populacao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sp-populacao-baixa-visao.jpg',
                             'sp-populacao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'População 2': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sp-populacao-2-tatil.jpg',
                             'sp-populacao-2-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sp-populacao-2-baixa-visao.jpg',
                             'sp-populacao-2-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Hidrografia': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sp-hidrografia-tatil.jpg',
                             'sp-hidrografia-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sp-hidrografia-baixa-visao.jpg',
                             'sp-hidrografia-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Região': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sp-regiao-tatil.jpg',
                             'sp-regiao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sp-regiao-baixa-visao.jpg',
                             'sp-regiao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Relevo': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sp-relevo-tatil.jpg',
                             'sp-relevo-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sp-relevo-baixa-visao.jpg',
                             'sp-relevo-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Rodoviário': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sp-rodoviario-tatil.jpg',
                             'sp-rodoviario-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sp-rodoviario-baixa-visao.jpg',
                             'sp-rodoviario-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Vegetação': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['sp-vegetacao-tatil.jpg',
                             'sp-vegetacao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['sp-vegetacao-baixa-visao.jpg',
                             'sp-vegetacao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
        }
    }
%}

{% for map, data in maps.items() %}
{{ map_list(map, data) }}
{% endfor %}
