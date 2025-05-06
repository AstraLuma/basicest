import pathlib

from basicest import Project, BUILD_OUTPUT

root = pathlib.Path.cwd()
project = Project(root=root, dest=root / BUILD_OUTPUT)
project.do_the_build()
