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

<div class="col text-center">
    <div class="text-center">{{ title }}</div>
    {% for img in imgs %}
    {% set url = '/materiais/didaticos/cartografia-tatil/atlas-geografico-tatil/' + img %}
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
                        'america-central/acetato/america-central-continental-fisico-acetato.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'america-central/baixa-visao/america-central-continental-fisico-baixa-visao.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Político': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'america-central/acetato/america-central-continental-politico-acetato.jpg',
                        'america-central/acetato/america-central-continental-politico-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'america-central/baixa-visao/america-central-continental-politico-baixa-visao.jpg',
                        'america-central/baixa-visao/america-central-continental-politico-baixa-visao-legenda.jpg',
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
                        'america-central/acetato/america-central-insular-fisico-acetato.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'america-central/baixa-visao/america-central-insular-fisico-baixa-visao.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Político': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'america-central/acetato/america-central-insular-politico-acetato.jpg',
                        'america-central/acetato/america-central-insular-politico-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'america-central/baixa-visao/america-central-insular-politico-baixa-visao.jpg',
                        'america-central/baixa-visao/america-central-insular-politico-baixa-visao-legenda.jpg',
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
        'Antártida': {
            'Físico': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'antartida-fisico-acetato.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'antartida-fisico-baixa-visao.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Vegetação': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'antartida-vegetacao-acetato.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'antartida-vegetacao-baixa-visao.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
        },
        'Ásia': {
            'Físico': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'asia/acetato/asia-fisico-acetato.jpg',
                        'asia/acetato/asia-fisico-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Vegetação': [
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'asia/baixa-visao/asia-fisico-baixa-visao.jpg',
                        'asia/baixa-visao/asia-fisico-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
        },
        'Ásia - Norte': {
            'Político': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'asia/acetato/asia-norte-politico-acetato.jpg',
                        'asia/acetato/asia-norte-politico-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'asia/baixa-visao/asia-norte-politico-baixa-visao.jpg',
                        'asia/baixa-visao/asia-norte-politico-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
        },
        'Ásia - Oriente Médio': {
            'Político': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'asia/acetato/asia-oriente-medio-politico-acetato-1.jpg',
                        'asia/acetato/asia-oriente-medio-politico-acetato-2.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'asia/baixa-visao/asia-oriente-medio-politico-baixa-visao-1.jpg',
                        'asia/baixa-visao/asia-oriente-medio-politico-baixa-visao-2.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Vegetação': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'asia/acetato/asia-oriente-medio-vegetacao-acetato.jpg',
                        'asia/acetato/asia-oriente-medio-vegetacao-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'asia/baixa-visao/asia-oriente-medio-vegetacao-baixa-visao.jpg',
                        'asia/baixa-visao/asia-oriente-medio-vegetacao-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
        },
        'Ásia - Sul': {
            'Político': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'asia/acetato/asia-sul-politico-acetato-1.jpg',
                        'asia/acetato/asia-sul-politico-acetato-2.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'asia/baixa-visao/asia-sul-politico-baixa-visao.jpg',
                        'asia/baixa-visao/asia-sul-politico-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Vegetação': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'asia/acetato/asia-sul-vegetacao-acetato.jpg',
                        'asia/acetato/asia-sul-vegetacao-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'asia/baixa-visao/asia-sul-vegetacao-baixa-visao.jpg',
                        'asia/baixa-visao/asia-sul-vegetacao-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
        },
        'Brasil': {
            'Bacias Hidrográficas': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'brasil-bacias-hidrograficas-acetato.jpg',
                        'brasil-bacias-hidrograficas-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'brasil-bacias-hidrograficas-baixa-visao.jpg',
                        'brasil-bacias-hidrograficas-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Vegetação': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'brasil-vegetacao-acetato.jpg',
                        'brasil-vegetacao-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'brasil-vegetacao-baixa-visao.jpg',
                        'brasil-vegetacao-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Climas': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'brasil-climas-acetato.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'brasil-climas-baixa-visao.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Geologia': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'brasil-geologia-acetato.jpg',
                        'brasil-geologia-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'brasil-geologia-baixa-visao.jpg',
                        'brasil-geologia-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Massas de Ar': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'brasil-massas-de-ar-acetato.jpg',
                        'brasil-massas-de-ar-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'brasil-massas-de-ar-baixa-visao.jpg',
                        'brasil-massas-de-ar-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'População': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'brasil-populacao-acetato.jpg',
                        'brasil-populacao-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'brasil-populacao-baixa-visao.jpg',
                        'brasil-populacao-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Relevo': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'brasil-relevo-acetato.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'brasil-relevo-baixa-visao.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
        },
        'Oceania': {
            'Físico': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'oceania/acetato/oceania-fisico-acetato.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'oceania/baixa-visao/oceania-fisico-baixa-visao.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Político': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'oceania/acetato/oceania-politico-acetato.jpg',
                        'oceania/acetato/oceania-politico-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'oceania/baixa-visao/oceania-politico-baixa-visao.jpg',
                        'oceania/baixa-visao/oceania-politico-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Vegetação': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'oceania/acetato/oceania-vegetacao-acetato.jpg',
                        'oceania/acetato/oceania-vegetacao-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'oceania/baixa-visao/oceania-vegetacao-baixa-visao.jpg',
                        'oceania/baixa-visao/oceania-vegetacao-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
        },
        'Mundo': {
            'Placas Tectônicas': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'placas-tectonicas-acetato.jpg',
                        'placas-tectonicas-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'placas-tectonicas-baixa-visao.jpg',
                        'placas-tectonicas-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'População Total': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'populacao-total-acetato.jpg',
                        'populacao-total-acetato-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'populacao-total-baixa-visao.jpg',
                        'populacao-total-baixa-visao-legenda.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
            'Zonas Térmicas': [
                {
                    'title': 'Acetato',
                    'imgs': [
                        'populacao-total-acetato.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
                {
                    'title': 'Baixa Visão',
                    'imgs': [
                        'populacao-total-baixa-visao.jpg',
                    ],
                    'size': '22,3x33,5cm',
                },
            ],
        },
        'Moçambique': {
            'Mapas Táteis': [
                {
                    'title': 'Países de Língua Portuguesa',
                    'imgs': [
                        'mocambique/thumbnails/paises-de-lingua-portuguesa-thumbnail.png',
                        'mocambique/thumbnails/paises-de-lingua-portuguesa-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Localização na África',
                    'imgs': [
                        'mocambique/thumbnails/mapa-africa-thumbnail.png',
                        'mocambique/thumbnails/mapa-africa-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Rodovias e Cidades Principais',
                    'imgs': [
                        'mocambique/thumbnails/rodovias-e-cidades-thumbnail.png',
                        'mocambique/thumbnails/rodovias-e-cidades-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Tipos de Clima',
                    'imgs': [
                        'mocambique/thumbnails/clima-thumbnail.png',
                        'mocambique/thumbnails/clima-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Grupos Étnicos',
                    'imgs': [
                        'mocambique/thumbnails/grupos-etnicos-thumbnail.png',
                        'mocambique/thumbnails/grupos-etnicos-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Bacias Hidrográficas',
                    'imgs': [
                        'mocambique/thumbnails/bacias-hidrograficas-thumbnail.png',
                        'mocambique/thumbnails/bacias-hidrograficas-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Hipsometria',
                    'imgs': [
                        'mocambique/thumbnails/hipsometria-thumbnail.png',
                        'mocambique/thumbnails/hipsometria-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Principais Indústrias',
                    'imgs': [
                        'mocambique/thumbnails/principais-industrias-thumbnail.png',
                        'mocambique/thumbnails/principais-industrias-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'População',
                    'imgs': [
                        'mocambique/thumbnails/populacao-thumbnail.png',
                        'mocambique/thumbnails/populacao-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Províncias',
                    'imgs': [
                        'mocambique/thumbnails/provincias-thumbnail.png',
                        'mocambique/thumbnails/provincias-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Principais Recursos Minerais',
                    'imgs': [
                        'mocambique/thumbnails/recursos-minerais-thumbnail.png',
                        'mocambique/thumbnails/recursos-minerais-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Vegetação',
                    'imgs': [
                        'mocambique/thumbnails/vegetacao-thumbnail.png',
                        'mocambique/thumbnails/vegetacao-legenda-thumbnail.png',
                    ],
                },
            ],
            'Baixa Visão': [
                {
                    'title': 'Países de Língua Portuguesa',
                    'imgs': [
                        'mocambique/thumbnails/paises-de-lingua-portuguesa-thumbnail.png',
                        'mocambique/thumbnails/paises-de-lingua-portuguesa-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Localização na África',
                    'imgs': [
                        'mocambique/thumbnails/mapa-africa-thumbnail.png',
                        'mocambique/thumbnails/mapa-africa-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Rodovias e Cidades Principais',
                    'imgs': [
                        'mocambique/thumbnails/rodovias-e-cidades-thumbnail.png',
                        'mocambique/thumbnails/rodovias-e-cidades-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Tipos de Clima',
                    'imgs': [
                        'mocambique/thumbnails/clima-thumbnail.png',
                        'mocambique/thumbnails/clima-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Grupos Étnicos',
                    'imgs': [
                        'mocambique/thumbnails/grupos-etnicos-thumbnail.png',
                        'mocambique/thumbnails/grupos-etnicos-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Bacias Hidrográficas',
                    'imgs': [
                        'mocambique/thumbnails/bacias-hidrograficas-thumbnail.png',
                        'mocambique/thumbnails/bacias-hidrograficas-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Hipsometria',
                    'imgs': [
                        'mocambique/thumbnails/hipsometria-thumbnail.png',
                        'mocambique/thumbnails/hipsometria-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Principais Indústrias',
                    'imgs': [
                        'mocambique/thumbnails/principais-industrias-thumbnail.png',
                        'mocambique/thumbnails/principais-industrias-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'População',
                    'imgs': [
                        'mocambique/thumbnails/populacao-thumbnail.png',
                        'mocambique/thumbnails/populacao-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Províncias',
                    'imgs': [
                        'mocambique/thumbnails/provincias-thumbnail.png',
                        'mocambique/thumbnails/provincias-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Principais Recursos Minerais',
                    'imgs': [
                        'mocambique/thumbnails/recursos-minerais-thumbnail.png',
                        'mocambique/thumbnails/recursos-minerais-legenda-thumbnail.png',
                    ],
                },
                {
                    'title': 'Vegetação',
                    'imgs': [
                        'mocambique/thumbnails/vegetacao-thumbnail.png',
                        'mocambique/thumbnails/vegetacao-legenda-thumbnail.png',
                    ],
                },
            ],
        },
    }
%}

{% for map, data in maps.items() %}
{{ map_list(map, data) }}
{% endfor %}
