Title: Atlas de Florianópolis
Section: cartografia-tatil
save_as: cartografia-tatil/atlas-e-mapas/atlas-de-florianopolis.html
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
    {% set url = '/materiais/didaticos/cartografia-tatil/atlas-florianopolis/' + img %}
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
        'Florianópolis': {
            'Áreas Protegidas': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['florianopolis-areas-protegidas-tatil.jpg', 
                             'florianopolis-areas-protegidas-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['florianopolis-areas-protegidas-baixa-visao.jpg',
                             'florianopolis-areas-protegidas-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Distritos': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['florianopolis-distritos-tatil.jpg', 
                             'florianopolis-distritos-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['florianopolis-distritos-baixa-visao.jpg',
                             'florianopolis-distritos-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Geologia': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['florianopolis-geologia-tatil.jpg', 
                             'florianopolis-geologia-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['florianopolis-geologia-baixa-visao.jpg',
                             'florianopolis-geologia-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Geomorfologia': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['florianopolis-geomorfo-tatil.jpg', 
                             'florianopolis-geomorfo-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['florianopolis-geomorfo-baixa-visao.jpg',
                             'florianopolis-geomorfo-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Hidrografia': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['florianopolis-hidrografia-tatil.jpg', 
                             'florianopolis-hidrografia-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['florianopolis-hidrografia-baixa-visao.jpg',
                             'florianopolis-hidrografia-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Ilhas': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['florianopolis-ilhas-tatil.jpg', 
                             'florianopolis-ilhas-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['florianopolis-ilhas-baixa-visao.jpg',
                             'florianopolis-ilhas-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Localização': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['florianopolis-localizacao-tatil.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['florianopolis-localizacao-baixa-visao.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Praias': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['florianopolis-praias-tatil.jpg', 
                             'florianopolis-praias-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['florianopolis-praias-baixa-visao.jpg',
                             'florianopolis-praias-baixa-visao-legenda.jpg',
                             'florianopolis-praias-baixa-visao-legenda2.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Rodovias': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['florianopolis-rodovias-tatil.jpg', 
                             'florianopolis-rodovias-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['florianopolis-rodovias-baixa-visao.jpg',
                             'florianopolis-rodovias-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Trilhas': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['florianopolis-trilhas-tatil.jpg', 
                             'florianopolis-trilhas-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['florianopolis-trilhas-baixa-visao.jpg',
                             'florianopolis-trilhas-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Vegetação': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['florianopolis-vegetacao-tatil.jpg', 
                             'florianopolis-vegetacao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['florianopolis-vegetacao-baixa-visao.jpg',
                             'florianopolis-vegetacao-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Território': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['florianopolis-territorio-tatil.jpg', 
                             'florianopolis-territorio-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['florianopolis-territorio-baixa-visao.jpg',
                             'florianopolis-territorio-baixa-visao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
        }
    }
%}

{% for map, data in maps.items() %}
{{ map_list(map, data) }}
{% endfor %}
