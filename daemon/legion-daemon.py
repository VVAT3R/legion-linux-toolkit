#!/usr/bin/env python3
"""
Legion Linux Toolkit — Daemon Stub
====================================
Hardware control is delegated to LLL's legiond.
This stub exists for compatibility but legiond should be used instead.

To use LLL's daemon instead:
  sudo systemctl enable --now legiond.service

Or install LLL: https://github.com/johnfanv2/LenovoLegionLinux
"""

import os, sys, logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s  %(message)s")
log = logging.getLogger("legion")

sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))
import lll_adapter as lll

LEGION_SYS_BASEPATH = "/sys/module/legion_laptop/drivers/platform:legion/legion"

PROFILES = {
    "quiet":       {"governor": "powersave",   "boost": "0", "epp": "power"},
    "balanced":    {"governor": "powersave",   "boost": "1", "epp": "balance_power"},
    "performance": {"governor": "performance", "boost": "1", "epp": "performance"},
    "custom":      {"governor": "performance", "boost": "1", "epp": "performance"},
}

def apply_profile(name: str):
    if name not in PROFILES:
        log.error(f"Unknown profile: {name}")
        return
    p = PROFILES[name]
    lll.write_powermode(name)
    for g in Path("/sys/devices/system/cpu").glob("cpu[0-9]*/cpufreq/scaling_governor"):
        try: g.write_text(p["governor"])
        except: pass
    boost = Path("/sys/devices/system/cpu/cpufreq/boost")
    if boost.exists():
        try: boost.write_text(p["boost"])
        except: pass
    epp_glob = list(Path("/sys/devices/system/cpu").glob("cpu[0-9]*/cpufreq/energy_performance_preference"))
    for e in epp_glob:
        try: e.write_text(p["epp"])
        except: pass
    log.info(f"Applied profile: {name} ({p['governor']}, boost={p['boost']})")

def get_current_profile() -> str:
    return lll.read_powermode()

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("ERROR: Run as root (sudo)", file=sys.stderr)
        sys.exit(1)
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd in PROFILES:
            apply_profile(cmd)
        elif cmd == "status":
            print(f"Profile: {get_current_profile()}")
            print(f"LLL loaded: {lll.is_lll_loaded()}")
            print(f"LLL bound: {lll.is_lll_device_bound()}")
        else:
            print(f"Unknown: {cmd}")
    else:
        print("Legion Linux Toolkit Daemon (LLL backend)")
        print("Use LLL's legiond for full daemon functionality:")
        print("  sudo systemctl enable --now legiond.service")
        print()
        print("Or run one-shot commands:")
        print(f"  {sys.argv[0]} quiet|balanced|performance|custom")
        print(f"  {sys.argv[0]} status")
