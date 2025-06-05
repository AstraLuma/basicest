import re

import jinja2.ext
import jinja2.nodes
import markupsafe
import pygments
import pygments.lexers
import pygments.formatters

from __basicest__ import project


# Excuse me, I'm just going to invoke an eldritch being real quick
TITLE_PATTERN = re.compile(r"<h1>(.*?)</h1>")


def htmltitle(contents):
    if match := TITLE_PATTERN.search(contents):
        return markupsafe.Markup(match.group(1))
    else:
        return ""


project.jinja.filters['htmltitle'] = htmltitle

def pygments_highlight(contents, lang):
    if lang:
        lexer = pygments.lexers.get_lexer_by_name(lang)
    else:
        lexer = pygments.lexers.guess_lexer(contents)
    return pygments.highlight(str(contents), lexer, pygments.formatters.HtmlFormatter())


project.jinja.filters['pygments_highlight'] = pygments_highlight


class PygmentsExtension(jinja2.ext.Extension):

    tags = {"pygments_css"}

    def parse(self, parser: "Parser") -> jinja2.nodes.Node:
        formatter = pygments.formatters.HtmlFormatter()
        lineno = next(parser.stream).lineno

        node = jinja2.nodes.Output([jinja2.nodes.TemplateData(formatter.get_style_defs(), lineno=lineno)], lineno=lineno)
        return node

project.jinja.add_extension(PygmentsExtension)