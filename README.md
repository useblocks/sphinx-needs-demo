# Sphinx-Needs-Demo

**View rendered documentation at
https://sphinx-needs-demo.readthedocs.io**

This a demo documentation project to show the usage of Sphinx-Needs
in the context of an Automitve SW development documentation.

## Online IDE support

### Gitpod
A preconfigured VS Code IDE instance is available on Gitpod, which allows you
to play around with the docs, build it and view the outcome in
the browser.

Just start it by following this link:
https://gitpod.io/#https://github.com/useblocks/sphinx-needs-demo

It does not cost anything, but an account creation may be needed.

### Codespaces

Just start it by clicking this badge:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/useblocks/sphinx-needs-demo/)

## Development Container

This project includes a preconfigured development container (devcontainer) setup, making it easy to get started with a consistent development environment.

To learn how to use the devcontainer, see the detailed instructions in [.devcontainer/README.md](.devcontainer/README.md).

## Schema Validation

This project demonstrates [Sphinx-Needs Schema Validation](https://sphinx-needs.readthedocs.io/en/latest/schema/index.html) for enforcing data quality and consistency across requirements, specifications, implementations, and test cases.

Key validation features:
- **ID Pattern Validation**: Ensures consistent naming conventions for all need types
- **Required Fields**: Enforces mandatory fields for automotive ADAS requirements
- **Link Validation**: Validates relationships between different need types
- **Status Checks**: Ensures valid status values across all needs

See [docs/SCHEMA_VALIDATION.md](docs/SCHEMA_VALIDATION.md) for complete documentation.
