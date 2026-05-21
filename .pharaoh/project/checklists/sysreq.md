---
applies_to: sysreq
required_before: [reviewed]
---

# System requirement review checklist

- [ ] Body uses a single `shall` clause describing observable system behavior
- [ ] Wording is allocation-free (does not pre-bind hardware or software boundaries unless required)
- [ ] `:source_doc:` references the originating document (if set)
- [ ] At least one `swreq` or `arch` element decomposes this requirement
