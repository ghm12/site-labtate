from dataclasses import dataclass
from pathlib import Path
from pprint import pprint
from sys import argv
from textwrap import dedent


@dataclass
class Article:
    title: str
    other: str
    url: str = ''
    urltype: str = ''
    section: str = 'cartografia-tatil'


def as_path(title: str):
    return (
        title.lower()
            .replace(' ', '-')
            .replace('/', '-')
    )


def read_file(path: Path) -> str:
    with open(path) as f:
        return f.read()


def save_article(article: Article, path: Path):
    with open(path, 'w') as f:
        f.write(dedent(f'''
            title: {article.title}
            other: {article.other}
            url: {article.url}
            urltype: {article.urltype}
            section: {article.section}\n
        ''').strip())


if __name__ == '__main__':
    articles = []

    article = None

    for line in read_file(argv[1]).splitlines():
        if not line:
            if article is not None:
                articles.append(article)
                article = None
            continue

        if article:
            article.urltype = line
            continue

        print(line)
        title, *other = line.split('.', maxsplit=1)

        other = ''.join(other).replace('In: ', '')

        article = Article(
            title=f'{title}.',
            other=other,
            section='cartografia-escolar'
        )

    for article in articles:
        save_article(article, f'pubs/{as_path(article.title)}md')
