from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Any, Mapping
from .loader import get_schedule

ASSUMPTION_CARD = "beam-split-first-mirror-v1"

@dataclass
class FacilityPlan:
    tool_kw: list[float]
    wafers_per_day: list[float]
    facility_wafers_per_day: float
    peak_fluence_proxy: float
    fluence_margin: float
    ablation_flag: bool
    assumption_card_id: str = ASSUMPTION_CARD
    fel03_note: str = "Physics KEEP waits FEL-03."
    scheduler_source: str = "reference"
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def schedule_facility(row: Mapping[str, Any] | None = None) -> FacilityPlan:
    source, fn = get_schedule()
    out = fn(dict(row or {}))
    return FacilityPlan(
        tool_kw=[float(x) for x in out["tool_kw"]],
        wafers_per_day=[float(x) for x in out["wafers_per_day"]],
        facility_wafers_per_day=float(out["facility_wafers_per_day"]),
        peak_fluence_proxy=float(out["peak_fluence_proxy"]),
        fluence_margin=float(out["fluence_margin"]),
        ablation_flag=bool(out["ablation_flag"]),
        assumption_card_id=str(out.get("assumption_card_id", ASSUMPTION_CARD)),
        fel03_note=str(out.get("fel03_note", "Physics KEEP waits FEL-03.")),
        scheduler_source=source,
    )
