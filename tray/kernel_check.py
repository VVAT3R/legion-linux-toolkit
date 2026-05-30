# Kernel version tracking for LLL (LenovoLegionLinux) compatibility
# Auto-detects by checking if LLL kernel module is loaded and working.

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "lib"))
import lll_adapter as lll

_kernel_check_result = {"checked": False, "works": None}

def get_kernel_version() -> str:
    try:
        import subprocess
        return subprocess.run(["uname", "-r"], capture_output=True, text=True, timeout=3).stdout.strip()
    except:
        try:
            return Path("/proc/sys/kernel/osrelease").read_text().split()[0]
        except:
            return "unknown"

def check_lll_works() -> bool:
    global _kernel_check_result
    if _kernel_check_result["checked"]:
        return _kernel_check_result["works"]
    works = lll.is_lll_available()
    _kernel_check_result = {"checked": True, "works": works}
    return works

def get_fan_status_message() -> str:
    kver = get_kernel_version()
    works = check_lll_works()
    if works:
        return f"✅ LLL active — Kernel {kver}"
    else:
        if lll.is_lll_loaded():
            return f"⚠️ LLL loaded but no device bound — Kernel {kver}"
        else:
            return f"⚠️ LLL not available — Kernel {kver}"
