Title: Atlas do Rio Grande do Sul
Section: cartografia-tatil
save_as: cartografia-tatil/atlas-e-mapas/atlas-do-rio-grande-do-sul.html
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
    {% set url = '/materiais/didaticos/cartografia-tatil/atlas-rs/' + img %}
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
                    'imgs': ['rs-clima-tatil.jpg', 
                             'rs-clima-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['rs-clima-baixa-visao.jpg',
                             'rs-clima-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Densidade Demográfica': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['rs-densidade-demografica-tatil.jpg',
                             'rs-densidade-demografica-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['rs-densidade-demografica-baixa-visao.jpg',
                             'rs-densidade-demografica-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Hidrografia': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['rs-hidrografia-tatil.jpg',
                             'rs-hidrografia-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['rs-hidrografia-baixa-visao.jpg',
                             'rs-hidrografia-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Região': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['rs-regiao-tatil.jpg',
                             'rs-regiao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['rs-regiao-baixa-visao.jpg',
                             'rs-regiao-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Relevo': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['rs-relevo-tatil.jpg',
                             'rs-relevo-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['rs-relevo-baixa-visao.jpg',
                             'rs-relevo-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Rodoviário': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['rs-rodoviario-tatil.jpg',
                             'rs-rodoviario-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['rs-rodoviario-baixa-visao.jpg',
                             'rs-rodoviario-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Vegetação': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['rs-vegetacao-tatil.jpg',
                             'rs-vegetacao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['rs-vegetacao-baixa-visao.jpg',
                             'rs-vegetacao-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
        }
    }
%}

{% for map, data in maps.items() %}
{{ map_list(map, data) }}
{% endfor %}
