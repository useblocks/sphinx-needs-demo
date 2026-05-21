---
applies_to: fsr
required_before: [reviewed]
---

# Functional safety requirement review checklist

- [ ] Body uses a single `shall` clause expressing a safety-relevant behavior
- [ ] `:derives_from:` names at least one real `safety_goal` ID
- [ ] ASIL inheritance / decomposition rationale is stated (if ASIL differs from parent)
- [ ] Allocation to component / sub-system is explicit
