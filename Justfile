set windows-powershell := true

# Show this help
@help:
  just --list


# Set up dev environment
install:
  poetry install


# Build the included site
build:
  poetry run basicest site

# Run a webserver on the included site
serve:
  poetry run python -m http.server -d site/_build -b 127.0.0.1 0