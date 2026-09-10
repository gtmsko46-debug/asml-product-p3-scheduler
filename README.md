# asml-product-p3-scheduler

> **Champion FREEZE (2026-09-10):** no new hills / no new tickets. This README is the ship surface — polish docs only. See asml-bench `corpus/notes/champion-freeze-2026-09-10-product-ship.md`.

Facility wafers/day under shared FEL split. Card: `beam-split-first-mirror-v1`. Physics KEEP waits FEL-03.

```python
from asml_product_p3_scheduler import schedule_facility
plan = schedule_facility({"n_tools": 4, "priorities": [2, 1, 1, 1]})
```

M1 SEED. Parent #46.
