# AutoTune_Lab

**Real-time vocal processing for karaoke** — pitch correction, reverb, echo, EQ.

Xử lý giọng hát từ mic real-time trước khi ra loa. Dùng VST plugins (open-source + REAPER stock) chạy trên Windows.

## Flow

```
Mic → [Noise Gate] → [EQ] → [Pitch Correction] → [Reverb] → [Echo/Delay] → [Compressor] → Loa
```

## Quick Start (Windows)

### 1. Cài đặt
```powershell
# ASIO Driver (giảm latency)
https://asio4all.org/

# REAPER (VST host, eval 60 ngày full tính năng)
https://www.reaper.fm/download.php
```

### 2. Pitch Correction — OpenTune
[github.com/bemtorres/opentune](https://github.com/bemtorres/opentune) — zero-latency, granular synthesis, scale snapping.

Build từ source (cần Visual Studio + JUCE Projucer) hoặc download binary từ Releases.

### 3. Load FX Chain trong REAPER
```
Insert track → Arm record (Input: Mic) → FX button → Add:
  ReaEQ → OpenTune → ReaVerbate → ReaDelay → ReaComp
```

### 4. Cấu hình nhanh
| Tham số | Karaoke | Vocal Warm | T-Pain |
|---------|---------|------------|--------|
| Retune Speed | 60 | 50 | 100 |
| Scale | C Major | C Major | C Minor |
| Reverb Mix | 25% | 20% | 35% |
| Delay Feed. | 15% | — | 35% |
| Comp Ratio | 3:1 | 4:1 | 4:1 |

## Presets
Xem `presets/*.yaml` — 3 preset dạng YAML (karaoke_standard, vocal_warm, tpain_effect)
Export .RfxChain từ REAPER để share chain.

## Project Structure
```
├── docs/           # Hướng dẫn cài đặt + presets
├── presets/        # YAML preset cho từng phong cách
├── vst-plugins/    # Symlink đến VST plugins đã cài
├── hosts/          # Symlink đến VST host apps
├── tools/          # Utility scripts (tùy chọn)
└── references/     # Source code tham khảo
```

## References
| Repo | Chức năng |
|------|-----------|
| [bemtorres/opentune](https://github.com/bemtorres/opentune) | Real-time pitch correction VST |
| [breakfastquay/rubberband](https://github.com/breakfastquay/rubberband) | Pitch shifting library (C++) |
| [surina.net/soundtouch](https://www.surina.net/soundtouch/) | Tempo/pitch library |
| [mmckegg/freeverb](https://github.com/mmckegg/freeverb) | Reverb algorithm |
| [juce-framework/JUCE](https://github.com/juce-framework/JUCE) | C++ audio plugin framework |

## Ghi chú
- **Latency ~6ms** với ASIO driver + buffer 128 samples — không cảm nhận được delay
- **Không cần mua plugin**: toàn bộ dùng open-source hoặc stock REAPER
