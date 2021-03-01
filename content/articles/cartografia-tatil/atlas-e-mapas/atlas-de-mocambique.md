Title: Atlas de Moçambique
Section: cartografia-tatil
save_as: cartografia-tatil/atlas-e-mapas/atlas-de-mocambique.html
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
    {% set url = '/materiais/didaticos/cartografia-tatil/atlas-de-mocambique/' + img %}
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
        'Moçambique': {
            'Países de Língua Portuguesa': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['mocambique-mapa-mundi-tatil.jpg', 
                             'mocambique-mapa-mundi-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['mocambique-mapa-mundi-baixa-visao.jpg',
                             'mocambique-mapa-mundi-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ],
            'Localização na África': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['mocambique-africa-tatil.jpg',
                             'mocambique-africa-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['mocambique-africa-baixa-visao.jpg',
                             'mocambique-africa-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Principais Cidades e Rodovias': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['mocambique-cidades-e-rodovias-tatil.jpg',
                             'mocambique-cidades-e-rodovias-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['mocambique-cidades-e-rodovias-baixa-visao.jpg',
                             'mocambique-cidades-e-rodovias-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Clima': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['mocambique-clima-tatil.jpg',
                             'mocambique-clima-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['mocambique-clima-baixa-visao.jpg',
                             'mocambique-clima-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Grupos Étnicos': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['mocambique-grupos-etnicos-tatil.jpg',
                             'mocambique-grupos-etnicos-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['mocambique-grupos-etnicos-baixa-visao.jpg',
                             'mocambique-grupos-etnicos-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Bacias Hidrográficas': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['mocambique-hidrografia-tatil.jpg',
                             'mocambique-hidrografia-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['mocambique-hidrografia-baixa-visao.jpg',
                             'mocambique-hidrografia-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Hipsometria': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['mocambique-hipsometria-tatil.jpg',
                             'mocambique-hipsometria-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['mocambique-hipsometria-baixa-visao.jpg',
                             'mocambique-hipsometria-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Principais Indústrias': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['mocambique-industrias-tatil.jpg',
                             'mocambique-industrias-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['mocambique-industrias-baixa-visao.jpg',
                             'mocambique-industrias-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'População': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['mocambique-populacao-tatil.jpg',
                             'mocambique-populacao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['mocambique-populacao-baixa-visao.jpg',
                             'mocambique-populacao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Províncias': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['mocambique-provincias-tatil.jpg',
                             'mocambique-provincias-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['mocambique-provincias-baixa-visao.jpg',
                             'mocambique-provincias-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Principais Recursos Minerais': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['mocambique-recursos-minerais-tatil.jpg',
                             'mocambique-recursos-minerais-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['mocambique-recursos-minerais-baixa-visao.jpg',
                             'mocambique-recursos-minerais-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
            'Vegetação': [
                {
                    'title': 'Mapa Tátil',
                    'imgs': ['mocambique-vegetacao-tatil.jpg',
                             'mocambique-vegetacao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
                {
                    'title': 'Mapa de Baixa Visão',
                    'imgs': ['mocambique-vegetacao-baixa-visao.jpg',
                             'mocambique-vegetacao-legenda.jpg'],
                    'size': '33,5x50,5cm',
                }
            ],
        }
    }
%}

{% for map, data in maps.items() %}
{{ map_list(map, data) }}
{% endfor %}
