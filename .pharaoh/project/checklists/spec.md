---
applies_to: spec
required_before: [reviewed]
---

# Specification review checklist

- [ ] `:reqs:` (or `:links:`) names at least one parent `req`
- [ ] Body refines exactly one observable behavior of the parent requirement
- [ ] Body uses precise wording (no "should/may/usually")
- [ ] At least one `impl` implements this spec
- [ ] At least one `test` verifies this spec
