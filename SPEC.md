# asml-product-p3-scheduler — Product Spec (M0)

**Parent:** asml-bench [#46](https://github.com/gtmsko46-debug/asml-bench/issues/46)  
**Stage:** Spec → Build → Review → Ship  
**Rule:** Bots orchestrate; all *solver/sandbox* code via lasercode (Foreman→Operator). Docs/spec PRs OK offline.

## Champion job
Facility wafers/day under split multi-kW bunch trains — who gets photons when a train drops. Waits FEL-03 research feed for physics KEEP; Spec proceeds now.

## Public API (target)
```python
from asml_product_p3_scheduler import schedule_facility
plan = schedule_facility(tools=..., bunch_train=..., priorities=...)
```

## Lab bind
| Field | Value |
|-------|-------|
| Sandbox | `labs/p3-scheduler/scheduler.py (scaffold; FEL-03 bind when ready)` |
| Frozen eval | product scheduler eval; bind FEL-03 when dual-KEEP exists |
| Assumption card | `beam-split-facility-v1` |
| Dual-gate | dual-gate after FEL-03 feed; until then Spec/M1 package only |
| HOLDOUT | pin when EI freezes product holdout (no eval edits by solvers) |

## KEEP / promote bar
- Dual-provider KEEP on same frozen eval + digest
- Critic clear (no oracle / metric reuse)
- Repro Bot clean-tree PASS
- Diplomat dual stamp before product `reference_*` sync

## Must not
- Edit `eval.py` / `fixture/*` from solver tickets
- Ship single-provider KEEP as product baseline
- Claim fab-grounded numbers (synthetic cards only)

## Milestones
1. **M0 Spec** — this document + README champion job (this PR)
2. **M1 Package** — importable module + SEED `reference_*` + tests
3. **M2 Dual-gate** — HT pair via Foreman; Critic+Repro+Diplomat
4. **M3 Ship** — `reference_*` sync + ship-queue Issue close

## Bay
Queued behind P1 deepen / P2 HT-1023/1024 unless CoS assigns spare Operator. Spec/docs do not steal bay.
