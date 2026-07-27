#!/bin/bash
# AutoTune_Lab — Setup reference symlinks
# Tạo link đến các source repo audio processing (bỏ qua nếu chưa có)

REF_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REF_DIR" || exit 1

declare -A MAP
MAP[opentune]="https://github.com/bemtorres/opentune"
MAP[rubberband]="https://github.com/breakfastquay/rubberband"
MAP[soundtouch]="https://www.surina.net/soundtouch/"
MAP[freeverb]="https://github.com/mmckegg/freeverb"
MAP[juce]="https://github.com/juce-framework/JUCE"
MAP[hachi-tune]="https://github.com/KCKT0112/HachiTune"

echo "AutoTune_Lab References Setup"
echo "=============================="
echo ""
echo "Clone repos locally then run:"
echo "  bash setup_references.sh"
echo ""
echo "Targets:"
for name in "${!MAP[@]}"; do
    echo "  $name -> ${MAP[$name]}"
done
