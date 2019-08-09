Title: Cartografia Tátil - Publicações Acadêmicas
Slug: academicas

{%
    macro pub(title, other='', url='', urltype=None)
-%}

<h3>{{title}}</h3>

<p>{{other}}</p>

{%- if url -%}
    Link{%- if urltype %}
        ({{urltype|upper}})
    {%- endif -%}: <a href="/materiais/publicacoes/{{url}}">{{url}}</a>
{%- endif -%}

{%-
    endmacro
%}

{%
    macro pub_list(pubs)
-%}


<hr>

{% for _pub in pubs -%}
{{ pub(**_pub) }}

<hr>
{%- endfor %}

{%-
    endmacro
%}

{{
    pub_list([
        {
            'title': 'Aprender/Ensinar Cartografia: Material Didático Acessível na Web.',
            'other': 'XXV Congresso Brasileiro de Cartografia, III Congresso Brasileiro de Geoprocessamento I Congresso Brasileiro de Geointeligência, 2011, Curitiba.',
            'url': 'Aprender e Ensinar Cartografia - Material Didático Acessível Na Web.pdf',
            'urltype': 'PDF',
        },
        {
            'title': 'Contribuição para o ensino-aprendizagem de Geografia: a padronização de mapas táteis.',
            'other': 'XIV Encuentro de Geografos de America latina – XIV EGAL, 2013, Lima, Peru.',
            'url': 'Contribuição para o Ensino-Aprendizagem de Geografia - A padronização de mapas táteis.pdf',
            'urltype': 'PDF',
        },
        {
            'title': '',
            'other': '',
            'url': '',
            'urltype': 'PDF',
        },
        {
            'title': '',
            'other': '',
            'url': '',
            'urltype': 'PDF',
        },
    ])
}}
