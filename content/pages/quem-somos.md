Title: Quem somos
Slug: quem-somos

{%
    macro person(name, prefix='', pic='sem-foto.jpg', occup='', cv=None)
-%}
<div class="person">
    <div
        class="left ball"
        alt="Foto de {{name}}"
        style="background-image: url('/img/pessoal/{{pic}}')"
    ></div>
    <div class="left text">
        <b>{{prefix}} {{name}}</b>
        <br>

        {% if occup -%}
            {{ occup }}
            <br>
        {%- endif %}

        {% if cv -%}
            <a href="{{cv}}">Currículo Lattes</a>
        {%- endif %}
    </div>
</div>
{%-
    endmacro
%}

{%
    macro people_list(category, people)
-%}
## {{ category }}

<div class="people-list">
    {% for person_data in people -%}
        {{ person(**person_data) }}
    {%- endfor %}
</div>
{%-
    endmacro
%}

{{
    people_list(
        'Fundadora',
        [
            {
                'name': 'Ruth Emília Nogueira',
                'prefix': 'Prof. Doutora',
                'pic': 'ruth.jpg',
                'cv': 'http://lattes.cnpq.br/6095042026143286',
            },
        ]
    )
}}

{{
    people_list(
        'Coordenadora',
        [
            {
                'name': 'Rosemy da Silva Nascimento',
                'prefix': 'Prof. Doutora',
                'occup': 'Coordenadora Pedagógica e Institucional',
                'pic': 'rosemy.jpg',
                'cv': 'http://lattes.cnpq.br/2298176439926963',
            },
        ]
    )
}}

{{
    people_list(
        'Pesquisadores',
        [
            {
                'name': 'Simone de Mamann Ferreira',
                'prefix': 'Prof. MSc.',
                'occup': 'Coordenadora Pedagógica',
                'pic': 'simone-mamann.jpg',
                'cv': 'https://www.escavador.com/sobre/4385857/simone-de-mamann-ferreira',
            },
            {
                'name': 'Harrysson Luiz da Silva',
                'pic': 'harrysson.jpg',
                'cv': 'http://buscatextual.cnpq.brbuscatextual/visualizacv.do?id=K4783843Z9',
            },
            {
                'name': 'Daiana Zanelato',
                'pic': 'daiana.jpg',
                'cv': 'https://www.escavador.com/sobre/3056005/daiana-zanelato-dos-anjos',
            },
        ]
    )
}}

{{
    people_list(
        'Doutorandos',
        [
            {
                'name': 'Adilson Basquerote',
                'pic': 'adilson.jpg',
                'cv': 'https://www.escavador.com/sobre/7968423/adilson-tadeu-basquerote-silva',
            },
            {
                'name': 'Luiz de Vasconcellos Ferreira Sobrinho',
                'pic': 'luiz-vasconcellos.jpg',
                'cv': 'https://www.escavador.com/sobre/3383782/luiz-de-vasconcellos-ferreira-sobrinho',
            },
            {
                'name': 'Tamara Régis',
                'pic': 'tamara-regis.jpg',
                'cv': 'https://www.escavador.com/sobre/8244236/tamara-de-castro-regis',
            },
            {
                'name': 'Gabriela Geron',
                'pic': 'gabriela-geron.jpg',
                'cv': 'http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4404279H7',
            },
            {
                'name': 'João Daniel Martins',
                'pic': 'joao-daniel-martins.jpg',
                'cv': 'http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K4315719Z5',
            },
        ]
    )
}}

{{
    people_list(
        'Mestrandos',
        [
            {
                'name': 'Sabrina de Assunção',
                'pic': 'sabrina-assuncao.jpg',
            },
            {
                'name': 'Tarso Dornelles',
                'pic': 'sem-foto.jpg',
            },
            {
                'name': 'Eduardo Segundo',
                'pic': 'sem-foto.jpg',
            },
        ]
    )
}}

{{
    people_list(
        'Graduandos Bolsistas',
        [
            {
                'name': 'Luana Rampinelli Quaresma',
                'pic': 'luana-quaresma.jpg',
                'cv': 'http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K8822674J1',
            },
            {
                'name': 'Victor Ventura da Luz',
                'pic': 'victor-ventura.jpg',
                'cv': 'http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K2713600Z2',
            },
            {
                'name': 'Celso Afonso Palhares Madrid Filho',
                'pic': 'celso-madrid.jpg',
            },
            {
                'name': 'Clara Nascimento Wanderley',
                'pic': 'sem-foto.jpg',
            },
            {
                'name': 'Alexandre Julio Silva',
                'pic': 'sem-foto.jpg',
                'cv': '',
            },
            {
                'name': 'Thiago Afonso Peron',
                'pic': 'thiago-afonso.jpg',
                'cv': 'http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K8741267J4',
            },
        ]
    )
}}
