set windows-powershell := true

# Show this help
@help:
  just --list


# Set up dev environment
install:
  poetry install


# Build the included site
build:
  poetry run basicest demo