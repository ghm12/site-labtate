Title: Mapas Geográficos Táteis
Slug: mapas-tateis
Section: cartografia-tatil
Tags: recursos-didaticos


{%
    macro map_list(region, categories)
-%}
## {{region}}

(Clique nas imagens para abri-la)

{% for category, maps in categories.items() %}

### {{ category }}

<div class="row d-flex flex-row">
{% for kind, url in maps %}
    {% set url = '/materiais/didaticos/cartografia-tatil/atlas-geografico-tatil/' + url %}
<a href="{static}{{ url }}" class="col">
    <h4>{{ kind }}</h4>
    <img src="{static}{{url}}" style="max-width: 50%; object-fit: cover"/>
</a>
    {% endfor %}
</div>
<br>
<br>
{% endfor %}

{%
    endmacro
-%}

{{
    map_list('África', {
        'Físico': [
            ('Acetato', 'africa-fisico-acetato.jpg'),
            ('Baixa Visão', 'africa-fisico-baixa-visao.jpg'),
        ],
        'Político - Centro Sul': [
            ('Baixa Visão (Sem Legenda)', 'africa-politico-norte-baixa-visao.jpg'),
            ('Baixa Visão (Legenda 1)', 'africa-politico-norte-baixa-visao-legenda-1.jpg'),
            ('Baixa Visão (Legenda 2)', 'africa-politico-norte-baixa-visao-legenda-2.jpg'),
        ]
    })
}}
