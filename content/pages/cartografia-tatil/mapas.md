Title: Mapas Geográficos Táteis
Slug: mapas-tateis
Section: cartografia-tatil
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

<a href="{static}{{ url }}" class="col text-center">
    <div class="text-center">{{ title }}</div>
    {% for img in imgs %}
    {% set url = '/materiais/didaticos/cartografia-tatil/atlas-geografico-tatil/' + img %}
    <img src="{static}{{url}}" style="max-width: 50%; object-fit: cover"/>
    {% endfor %}
</a>
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
        'África': {
            'Físico': [
                {
                    'title': 'Acetato',
                    'imgs': ['africa-fisico-acetato.jpg'],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': ['africa-fisico-baixa-visao.jpg'],
                    'size': '22,3x33,5cm',
                },
            ],
            'Político - Norte': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'africa-politico-norte-acetato.jpg',
                        'africa-politico-norte-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'africa-politico-norte-baixa-visao.jpg',
                        'africa-politico-norte-baixa-visao-legenda-1.jpg',
                        'africa-politico-norte-baixa-visao-legenda-2.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Político - Centro-Sul': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'africa-politico-centro-sul-acetato.jpg',
                        'africa-politico-centro-sul-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'africa-politico-centro-sul-baixa-visao.jpg',
                        'africa-politico-centro-sul-baixa-visao-legenda-1.jpg',
                        'africa-politico-centro-sul-baixa-visao-legenda-2.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Vegetação': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'africa-vegetacao-acetato.jpg',
                        'africa-vegetacao-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'africa-vegetacao-baixa-visao.jpg',
                        'africa-vegetacao-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
        },
        'América Central Continental': {
            'Físico': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'america-central-continental-fisico-acetato.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'america-central-continental-fisico-baixa-visao.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Político': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'america-central-continental-politico-acetato.jpg',
                        'america-central-continental-politico-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'america-central-continental-politico-baixa-visao.jpg',
                        'america-central-continental-politico-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
        },
        'América Central Insular': {
            'Físico': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'america-central-insular-fisico-acetato.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'america-central-insular-fisico-baixa-visao.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Político': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'america-central-insular-politico-acetato.jpg',
                        'america-central-insular-politico-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'america-central-insular-politico-baixa-visao.jpg',
                        'america-central-insular-politico-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
        },
        'América do Norte': {
            'Físico': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'america-do-norte-fisico-acetato.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'america-do-norte-fisico-baixa-visao.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
        },
    }
%}

{% for map, data in maps.items() %}
{{ map_list(map, data) }}
{% endfor %}
