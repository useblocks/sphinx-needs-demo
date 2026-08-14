# Variant Configuration for ADAS Project

This directory contains variant configuration files for building the ADAS documentation with different regional and vehicle configurations.

## Available Variants

### EU Left (`eu_left.json`)
- **Region:** Europe
- **Speed Unit:** km/h
- **Highway Speed Limit:** 130 km/h
- **Steering Side:** Left
- **Driver Position:** Left

### EU Right (`eu_right.json`)
- **Region:** Europe
- **Speed Unit:** km/h
- **Highway Speed Limit:** 130 km/h
- **Steering Side:** Right
- **Driver Position:** Right

### America (`america.json`)
- **Region:** America
- **Speed Unit:** mph
- **Highway Speed Limit:** 75 mph
- **Steering Side:** Left
- **Driver Position:** Left

## Building with Variants

The variant is selected solely via the `needs_variant_data_file` config value.
The default (when nothing is passed) is `eu_left`.

### Default Build (EU Left)
```bash
sphinx-build -a -E -b html docs docs/_build/html
```

### EU Right Build
```bash
sphinx-build -a -E -b html -D needs_variant_data_file=variants/eu_right.json docs docs/_build/eu_right
```

### America Build
```bash
sphinx-build -a -E -b html -D needs_variant_data_file=variants/america.json docs docs/_build/america
```

**Hinweis:** Der JSON-Datei-Pfad ist relativ zum `docs/`-Verzeichnis.
Verwende `-D` (großes D) — `-d` (klein) ist der doctree-Cache-Pfad.

## Variant-Affected Needs

The following needs are configured to vary based on the selected variant:

### System Requirements (SYS.2)
- **REQ_017**: Maximum Speed Limit for Adaptive Cruise Control
  - Uses `var.region.speed_limit_highway` and `var.region.speed_unit`
- **REQ_018**: Lane Change Warning Direction
  - Uses `var.vehicle.driver_position` and `var.region.area`

### Software Requirements (SWE.1)
- **SWREQ_028**: Left-Hand Drive Turn Signal Priority (only in left-steering variants)
- **SWREQ_029**: Right-Hand Drive Turn Signal Priority (only in right-steering variants)

### Software Architecture (SWE.2)
- **SWARCH_011**: Camera Positioning Subsystem
  - Uses `var.vehicle.driver_position`, `var.region.area`, and `var.region.speed_unit`

### Unit Tests (SWE.4)
- **TEST_VARIANT_001**: Speed Limit Validation Test
  - Uses `var.region.speed_limit_highway` and conditional blocks per region

## Variant Features Used

1. **Field Value Variants**: `<{ var.region.speed_limit_highway }>`
2. **Prose Variants**: `:variant:\`var.region.speed_unit\``
3. **Conditional Blocks**: `.. if:: var.vehicle.steering_side == "left"`
4. **Filter Support**: Can be used in needtable/needlist filters
