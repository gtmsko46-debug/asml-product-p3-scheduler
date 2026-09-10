from asml_product_p3_scheduler import schedule_facility
from asml_product_p3_scheduler.loader import reset_loader_cache
import pytest

@pytest.fixture(autouse=True)
def _e(monkeypatch):
    monkeypatch.delenv("ASML_BENCH_ROOT", raising=False)
    reset_loader_cache()

def test_smoke():
    r = schedule_facility({"n_tools": 3})
    assert len(r.tool_kw) == 3
    assert r.facility_wafers_per_day > 0
