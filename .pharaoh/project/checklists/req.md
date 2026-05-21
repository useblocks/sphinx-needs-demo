---
applies_to: req
required_before: [reviewed]
---

# Requirement review checklist

- [ ] Body uses a single `shall` clause expressing observable behavior
- [ ] Body does not describe implementation (package names, function names, internal data structures)
- [ ] Scope is a single observable behavior, not a conjunction
- [ ] `:source_doc:` references an existing doc file (if set)
- [ ] At least one `spec` refines this requirement (else it is untracked work)
