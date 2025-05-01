import pathlib

import jinja2
import jinjax

PROJECT_ROOT = pathlib.Path.cwd()
COMPONENTS_FOLDER = "_components"
BUILD_OUTPUT = "_build"
PARSABLE_FILES = ('.html', '.xml')
DESTINATION = PROJECT_ROOT / BUILD_OUTPUT

catalog = jinjax.Catalog()
catalog.add_folder(PROJECT_ROOT / COMPONENTS_FOLDER)


# FIXME: clean up destination

for dirpath, dirnames, filenames in PROJECT_ROOT.walk():
    if COMPONENTS_FOLDER in dirnames:
        dirnames.remove(COMPONENTS_FOLDER)
    if BUILD_OUTPUT in dirnames:
        dirnames.remove(BUILD_OUTPUT)
    relpath = dirpath.relative_to(PROJECT_ROOT)
    buildpath = DESTINATION / relpath
    buildpath.mkdir(parents=True, exist_ok=True)
    for filename in filenames:
        srcfile = dirpath / filename
        relfile = relpath / filename
        buildfile = buildpath / filename
        if srcfile.suffix in PARSABLE_FILES:
            contents = catalog.render(str(relfile.with_suffix('')), _source=srcfile.read_text())
            buildfile.write_text(contents)
        else:
            buildfile.write_bytes(srcfile.read_bytes())