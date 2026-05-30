#!/bin/bash
# Legion Linux Toolkit — Sysfs Helper
# Called via pkexec (passwordless via polkit rule) to write to sysfs files.
set -euo pipefail
usage() { echo "Usage: $0 <path> <value>" >&2; exit 1; }
[[ $# -ne 2 ]] && usage
path="$1"; value="$2"
# Sanitize — only allow known sysfs paths
safe_prefixes=(
    /sys/module/legion_laptop/
    /sys/bus/platform/drivers/ideapad_acpi/
    /sys/devices/system/cpu/cpufreq/
    /sys/class/leds/
    /sys/class/backlight/
    /sys/devices/system/cpu/intel_pstate/
)
allowed=0
for pfx in "${safe_prefixes[@]}"; do
    if [[ "$path" == "$pfx"* ]]; then
        allowed=1; break
    fi
done
[[ $allowed -eq 0 ]] && { echo "ERROR: denied path: $path" >&2; exit 1; }
# Sanitize value
value="${value//[^0-9a-zA-Z_\/\-]/}"
echo -n "$value" > "$path"
