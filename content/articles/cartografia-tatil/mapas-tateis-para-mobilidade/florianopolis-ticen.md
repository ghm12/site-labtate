Title: Terminal Centro de Florianópolis (TICEN)
Section: cartografia-tatil
save_as: cartografia-tatil/mapas-tateis-para-mobilidade/florianopolis-ticen.html
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
    {% set url = '/materiais/didaticos/cartografia-tatil/mapas-tateis-para-mobilidade/' + img %}
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
        'Terminal Centro de Florianópolis': {
            '': [
                {
                    'title': '',
                    'imgs': ['florianopolis-ticen-1.jpg',
                             'florianopolis-ticen-2.jpg',
                             'florianopolis-centro-legenda.jpg'],
                    'size': '33,5x50,5cm',
                },
            ]
        }
    }
%}

{% for map, data in maps.items() %}
{{ map_list(map, data) }}
{% endfor %}