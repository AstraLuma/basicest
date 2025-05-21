set windows-powershell := true

# Show this help
@help:
  just --list


# Set up dev environment
install:
  poetry install --all-extras --all-groups


# Build the included site
build:
  poetry run basicest site -r site/requirements.txt

# Run a webserver on the included site
serve:
  poetry run basicest-serve site --open-browser --watch src -r site/requirements.txt

# Build the image
docker:
  docker build .