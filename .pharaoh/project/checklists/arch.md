---
applies_to: arch
required_before: [reviewed]
---

# Architecture element review checklist

- [ ] Element has a single, named responsibility
- [ ] `:depends_on:` / `:realizes:` correctly capture relations to other architecture elements
- [ ] Element is traceable back to at least one requirement (`req`, `sysreq`, or `swreq`)
- [ ] Decomposition is balanced (not too broad, not too granular)
