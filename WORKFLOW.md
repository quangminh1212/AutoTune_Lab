# AutoTune_Lab Workflow Guide

## Pipeline
1. **Config** → Define model + hardware + quantization targets in `configs/`
2. **Quantize** → `python scripts/quantize_compare.py --model <model> --methods awq gptq bitsandbytes`
3. **Benchmark** → `python scripts/benchmark_all.py --model <quantized_path> --out results/`
4. **Compare** → Check `results/` for JSON reports
5. **Deploy** → Best config deployed via RouterLab routing

## Rules
- Never commit model weights (`.safetensors`, `.bin`, `.gguf`)
- Always version configs with experiments
- Each run → one entry in `results/experiments.json`
- Reference repos = read-only symlinks only
