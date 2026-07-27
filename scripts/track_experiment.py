#!/usr/bin/env python3
"""
AutoTune — experiment tracker.

Records each tuning run with timestamp, model, method, config,
and results. Produces a comparison report.
"""

import json
import time
from pathlib import Path

EXPERIMENTS_FILE = Path("results/experiments.json")


def record(model: str, method: str, config: dict, metrics: dict):
    """Append an experiment record."""
    entries = []
    if EXPERIMENTS_FILE.exists():
        entries = json.loads(EXPERIMENTS_FILE.read_text())
    entries.append({
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "model": model,
        "method": method,
        "config": config,
        "metrics": metrics,
    })
    EXPERIMENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    EXPERIMENTS_FILE.write_text(json.dumps(entries, indent=2))
    return entries


def report(out_path: str = "results/latest_report.json"):
    """Generate comparison report from all experiments."""
    if not EXPERIMENTS_FILE.exists():
        print("No experiments yet.")
        return
    entries = json.loads(EXPERIMENTS_FILE.read_text())
    report_data = {"total_runs": len(entries), "experiments": entries}
    Path(out_path).write_text(json.dumps(report_data, indent=2))
    print(f"Report → {out_path}")
    return report_data
