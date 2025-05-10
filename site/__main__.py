import re

import markupsafe

from __basicest__ import project


# Excuse me, I'm just going to invoke an eldritch being real quick
TITLE_PATTERN = re.compile(r"<h1>(.*?)</h1>")


def htmltitle(contents):
    if match := TITLE_PATTERN.search(contents):
        return markupsafe.Markup(match.group(1))
    else:
        return ""


project.jinja.filters['htmltitle'] = htmltitle
