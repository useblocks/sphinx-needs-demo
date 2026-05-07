---
applies_to: component
required_before: [reviewed]
---

# Component review checklist

- [ ] Component has a single, named responsibility
- [ ] `:provides:` lists every interface offered to consumers
- [ ] `:consumes:` / `:uses:` lists every interface depended on
- [ ] Component is traceable to at least one architectural element (`arch` / `swarch` / `sys-arch`)
