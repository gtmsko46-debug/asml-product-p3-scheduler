# asml-product-p3-scheduler

Facility wafers/day under shared FEL split. Card: `beam-split-first-mirror-v1`. Physics KEEP waits FEL-03.

```python
from asml_product_p3_scheduler import schedule_facility
plan = schedule_facility({"n_tools": 4, "priorities": [2, 1, 1, 1]})
```

M1 SEED. Parent #46.
