#!/bin/bash
# Setup reference symlinks — run once after clone.
# Skips targets that don't exist on this machine.

REF_DIR="$(cd "$(dirname "$0")" && pwd)"

declare -A MAP
MAP[olive]="/c/Dev/AI_PowerUp/training/olive"
MAP[optimum]="/c/Dev/AI_PowerUp/training/optimum"
MAP[autoawq]="/c/Dev/AI_PowerUp/training/AutoAWQ"
MAP[tvm]="/c/Dev/AI_PowerUp/training/tvm"
MAP[auto-pytorch]="/c/Dev/AI_PowerUp/training/framework/auto-pytorch"
MAP[optimization]="/c/Dev/AI_PowerUp/training/optimization"
MAP[galore]="/c/Dev/AI_PowerUp/training/galore"
MAP[litgpt]="/c/Dev/AI_PowerUp/training/litgpt"
MAP[torchao]="/c/Dev/AI_PowerUp/training/framework/torchao"
MAP[torchtune]="/c/Dev/AI_PowerUp/training/framework/torchtune"
MAP[flash-attention]="/c/Dev/AI_PowerUp/training/flash-attention"
MAP[bitsandbytes]="/c/Dev/AI_PowerUp/training/bitsandbytes"
MAP[exllamav2]="/c/Dev/AI_PowerUp/training/exllamav2"
MAP[peft]="/c/Dev/AI_PowerUp/training/peft"
MAP[sglang]="/c/Dev/AI_PowerUp/training/sglang"
MAP[llama-factory]="/c/Dev/AI_PowerUp/training/LLaMA-Factory"
MAP[axolotl]="/c/Dev/AI_PowerUp/training/axolotl"
MAP[benchlab]="/c/Dev/AI_BenchLab"
MAP[evaluation]="/c/Dev/AI_PowerUp/evaluation"
MAP[tokenlab]="/c/Dev/TokenLab"
MAP[routerlab]="/c/Dev/RouterLab"

cd "$REF_DIR" || exit 1

for name in "${!MAP[@]}"; do
    target="${MAP[$name]}"
    if [ -e "$target" ]; then
        ln -sf "$target" "$name"
        echo "  [OK] $name → $target"
    else
        echo "  [--] $name (target missing: $target)"
    fi
done

echo "Done. $(ls -1 | grep -v README.md | wc -l) symlinks created."
