# asml-product-p3-scheduler

**Facility wafers/day under split multi-kW bunch trains — who gets photons when a train drops. Waits FEL-03 research feed for physics KEEP; Spec proceeds now.**

| | |
|--|--|
| Spec | [`SPEC.md`](SPEC.md) · asml-bench [#46](https://github.com/gtmsko46-debug/asml-bench/issues/46) |
| Factory | [FACTORY.md](https://github.com/gtmsko46-debug/asml-bench/blob/main/products/FACTORY.md) |
| Stage | **Spec (M0)** — package/build waits bay |

```bash
# after M1
pip install -e '.[dev]'
```

Sandbox hill-climbs live on asml-bench (`labs/p3-scheduler/scheduler.py (scaffold; FEL-03 bind when ready)`); set `ASML_BENCH_ROOT` to pick up live weights once the loader exists.
