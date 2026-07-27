# AutoTune_Lab — Hướng dẫn cài đặt

## Yêu cầu
- Windows 10/11
- ASIO driver (khuyên dùng ASIO4ALL)
- Mic karaoke (USB hoặc jack 3.5mm)
- Loa hoặc headphone

## Bước 1: Cài ASIO Driver
```powershell
Tải: https://asio4all.org/
Cài → Restart PC
```

## Bước 2: Cài VST Host (REAPER)
```powershell
Tải: https://www.reaper.fm/download.php
Cài mặc định
```

## Bước 3: Virtual Audio Cable (tùy chọn)
Nếu muốn tách riêng route mic qua VST rồi ra loa:
```powershell
VoiceMeeter Banana (free): https://vb-audio.com/Voicemeeter/banana.htm
```

## Bước 4: Cài OpenTune (Pitch Correction)
**Cách 1 — Download binary:**
Kiểm tra Releases trên https://github.com/bemtorres/opentune

**Cách 2 — Build từ source:**
```powershell
# Cần Visual Studio 2022 + JUCE Projucer
git clone https://github.com/bemtorres/opentune
cd opentune
# Mở .jucer → Projucer → export solution → build
# Copy OpenTune.vst3 vào C:\Program Files\Common Files\VST3\
```

## Bước 5: Cấu hình Chain trong REAPER

### Tạo FX Chain:
1. **File → New project**
2. **Insert → New track**
3. Click **FX** button
4. Add các plugin theo thứ tự:
   ```
   ReaEQ → OpenTune → ReaVerbate → ReaDelay → ReaComp
   ```
5. **Record arm** → Chọn Input: Mic
6. **Output** → Speakers

### Tham số cơ bản:

**ReaEQ:**
- Low Cut: 80Hz (loại bỏ ồn tần thấp)
- High Shelf: +2dB @ 8kHz (thêm độ sáng)

**OpenTune:**
- Retune Speed: 50-70 (tự nhiên), 80-100 (T-Pain)
- Scale: chọn scale phù hợp bài hát (thường C Major)

**ReaVerbate:**
- Room Size: 30-40%
- Mix: 20-30%

**ReaDelay:**
- Delay: 1/8 note
- Feedback: 15-20%

**ReaComp:**
- Ratio: 3:1
- Threshold: -18dB

## Bước 6: Tinh chỉnh
- Buffer size ASIO4ALL: 128 samples
- Test hát → chỉnh EQ theo giọng
- Lưu FX Chain: click FX → Save chain → đặt trong `presets/`
