# Schema Validation Setup

This project uses [Sphinx-Needs Schema Validation](https://sphinx-needs.readthedocs.io/en/latest/schema/index.html) to enforce data quality and consistency across all needs objects.

## Configuration

Schema validation is configured in two files:

### 1. `ubproject.toml` Configuration

The following settings in `docs/ubproject.toml` enable schema validation:

```toml
# docs/ubproject.toml
[needs]
schema_definitions_from_json = "schemas.json"
schema_severity = "warning"
schema_debug_active = false
```

- **`schema_definitions_from_json`**: Points to the JSON file containing schema definitions
- **`schema_severity`**: Minimum severity level to report (options: `violation`, `warning`, `info`)
- **`schema_debug_active`**: Enable detailed debugging output for schema validation

### 2. `schemas.json` Schema Definitions

The `docs/schemas.json` file contains all validation rules organized by:
- **ID Patterns**: Ensures consistent ID naming conventions
- **Status Validation**: Enforces valid status values
- **Link Validation**: Validates relationships between need types
- **Required Fields**: Enforces mandatory fields for specific contexts

## Validation Rules

### ID Pattern Validation (Severity: info)

Ensures consistent naming patterns for different need types:

- **Requirements**: `R_*`, `SWREQ_*`, or `REQ_*` (e.g., `REQ_001`, `SWREQ_042`)
- **Specifications**: `S_*` or `SPEC_*` (e.g., `SPEC_100`)
- **Implementations**: `I_*`, `IMPL_*`, or `GH_PR_*` (e.g., `IMPL_005`, `GH_PR_3`)
- **Tests**: `T_*` or `TEST_*` (e.g., `TEST_001`)
- **Persons**: `P_*` or uppercase names (e.g., `P_JOHN`, `PETER`)
- **SW Architecture**: `SWARCH_*` (e.g., `SWARCH_001`)
- **SW Requirements**: `SWREQ_*` or `GH_ISSUE_*` (e.g., `SWREQ_001`, `GH_ISSUE_12`)

### Automotive ADAS Requirements (Severity: warning)

For requirements in the `automotive-adas` documentation:

1. **Status Required**: Must have a valid status (`open`, `in progress`, `closed`, `passed`, `failed`)
2. **Release Required**: Must be linked to at least one release

### Network Link Validation (Severity: info)

Validates proper linking between need types:

- **Specifications → Requirements**: Specs should link to requirements via `reqs`
- **Implementations → Specifications**: Implementations should link to specs via `implements`
- **Tests → Specs/Implementations**: Test cases should link to specs or implementations

### Metadata Validation (Severity: info)

- **Persons**: Should have a `role` defined
- **Teams**: Should have at least one person assigned via `persons`

## Checking Validation Results

### During Build

Validation warnings appear during `sphinx-build`:

```bash
cd docs
uv run sphinx-build -b html . _build/html
```

or using `rye`

```bash
rye run docs
```

Look for an output like:
```
WARNING: Need 'REQ_005' has validation errors:
  Severity:       warning
  Field:          release
  Need path:      REQ_005
  Schema path:    automotive-req-release-required[8] > local > required
  User message:   Requirements in automotive-adas must be linked to a release
  Schema message: 'release' is a required property
```

### Schema Violations Report

Schema violations are also exported to `_build/html/schema_violations.json` for programmatic analysis.

## Modifying Schema Rules

### Adding a New Validation Rule

1. Edit `docs/schemas.json`
2. Add a new schema object to the `"schemas"` array:

```json
{
  "id": "my-new-rule",
  "severity": "warning",
  "message": "Custom validation message",
  "select": {
    "$ref": "#/$defs/type-req"
  },
  "validate": {
    "local": {
      "properties": {
        "my_field": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": ["my_field"]
    }
  }
}
```

### Reusable Schema Definitions

Use `$defs` section for reusable components:

```json
{
  "$defs": {
    "my-common-pattern": {
      "properties": {
        "status": { "enum": ["open", "closed"] }
      }
    }
  }
}
```

Reference with `"$ref": "#/$defs/my-common-pattern"`

### Severity Levels

- **`violation`**: Critical issues that should block builds
- **`warning`**: Important issues that need attention
- **`info`**: Informational messages for best practices

Change the global minimum severity in `ubproject.toml`:
```toml
schema_severity = "violation"  # Only show violations, suppress warnings/info
```

## Resources

- [Sphinx-Needs Schema Validation Documentation](https://sphinx-needs.readthedocs.io/en/latest/schema/index.html)
- [JSON Schema Reference](https://json-schema.org/understanding-json-schema/)
- Project's `schemas.json` for examples
