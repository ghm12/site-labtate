Title: Cartografia Tátil - Publicações Acadêmicas
Slug: academicas

{%
    macro pub(title, other='', url='', urltype=None)
-%}
### {{title}}

<p>{{other}}</p>

{%- if url -%}
    Link{%- if urltype %}
        ({{urltype|upper}})
    {%- endif -%}: <a href={{url}}>{{url}}</a>
{%- endif -%}

{%-
    endmacro
%}

{{ pub(title='Test', other='published here', url='localhost://here', urltype='PDF') }}
