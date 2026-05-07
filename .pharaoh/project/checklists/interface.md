---
applies_to: interface
required_before: [reviewed]
---

# Interface review checklist

- [ ] Operations are listed with explicit parameters and return contracts
- [ ] Pre / post-conditions or error modes are stated where relevant
- [ ] `:provided_by:` names exactly one provider component (or is intentionally blank for an abstract contract)
- [ ] Interface is referenced by at least one consumer (`component :uses:` / `:consumes:`)
