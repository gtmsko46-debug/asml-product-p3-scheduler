"""SEED facility scheduler from beam-split-first-mirror-v1 — waits FEL-03 KEEP for physics."""
from __future__ import annotations

FACILITY_KW = 5.0
TRANSPORT_LOSS = 0.08
FLUENCE_LIMIT = 0.15
MARGIN_MIN = 1.2


def schedule(row: dict) -> dict:
    n_tools = int(row.get("n_tools", 4))
    priorities = list(row.get("priorities", [1.0] * n_tools))
    if len(priorities) != n_tools:
        priorities = [1.0] * n_tools
    source_kw = float(row.get("facility_source_kw", FACILITY_KW))
    bunch_drop = float(row.get("bunch_drop_frac", 0.0))  # 0..1 capacity lost
    available = source_kw * (1.0 - TRANSPORT_LOSS) * (1.0 - bunch_drop)
    w = sum(max(p, 0.0) for p in priorities) or 1.0
    shares = [available * max(p, 0.0) / w for p in priorities]
    # fluence proxy: equal aperture toy — peak ~ share / n_tools scale
    peak = (max(shares) / max(n_tools, 1)) * 0.05  # synthetic J/cm2 proxy
    margin = FLUENCE_LIMIT / max(peak, 1e-9)
    ablation_flag = margin < MARGIN_MIN
    wafers_per_day = [s * 200.0 for s in shares]  # toy photons→wpd
    return {
        "tool_kw": [float(x) for x in shares],
        "wafers_per_day": [float(x) for x in wafers_per_day],
        "facility_wafers_per_day": float(sum(wafers_per_day)),
        "peak_fluence_proxy": float(peak),
        "fluence_margin": float(margin),
        "ablation_flag": bool(ablation_flag),
        "assumption_card_id": "beam-split-first-mirror-v1",
        "fel03_note": "Physics KEEP waits FEL-03 dual-gate; this is SEED schedule only.",
    }
