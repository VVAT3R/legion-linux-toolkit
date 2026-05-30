#!/usr/bin/env bash
# ══════════════════════════════════════════════════════════════════════════════
# Legion Linux Toolkit — Updater (LLL backend)
# ══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

RED='\033[0;31m'; GREEN='\033[0;32m'; CYAN='\033[0;36m'
NC='\033[0m'
ok()   { echo -e "  ${GREEN}✓${NC}  $*"; }
info() { echo -e "  ${CYAN}→${NC}  $*"; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "\n${CYAN}Updating Legion Linux Toolkit (LLL backend)…${NC}\n"

# Pull latest toolkit code
git -C "$SCRIPT_DIR" fetch origin
git -C "$SCRIPT_DIR" reset --hard origin/main

# Re-run installer
exec bash "$SCRIPT_DIR/install.sh"
