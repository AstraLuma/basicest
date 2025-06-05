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

# Turns out the default theme has decent contrast in both light and dark modes
pygments_formatter = pygments.formatters.HtmlFormatter(nowrap=True, nobackground=True)


def pygments_highlight(contents, lang):
    if lang:
        lexer = pygments.lexers.get_lexer_by_name(lang)
    else:
        lexer = pygments.lexers.guess_lexer(contents)
    return pygments.highlight(str(contents), lexer, pygments_formatter)


project.jinja.filters['pygments_highlight'] = pygments_highlight


def pygments_css():
    return pygments_formatter.get_style_defs('pre')

project.jinja.globals['pygments_css'] = pygments_css
