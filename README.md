# 🔧 AutoTune_Lab

**Automated Model Optimization & Tuning Laboratory**

AutoTune_Lab is a comprehensive lab for automated model tuning, quantization, inference optimization, and benchmarking. It leverages a curated set of reference repos from the AI ecosystem to provide a unified workflow for finding the optimal model configuration.

## 📂 Structure

```
AutoTune_Lab/
├── references/          # Symlinks to upstream repos (read-only)
│   ├── olive/           # Microsoft Olive — model optimization toolkit
│   ├── optimum/         # HuggingFace Optimum — inference/training optimization
│   ├── autoawq/         # Auto AWQ — automated GPTQ quantization
│   ├── tvm/             # Apache TVM — compiler-based autotuning
│   ├── auto-pytorch/    # AutoML for PyTorch
│   ├── optimization/    # General optimization tools
│   ├── galore/          # GaLore optimizer
│   ├── litgpt/          # Lightning GPT
│   ├── torchao/         # PyTorch quantization & sparsity
│   ├── torchtune/       # PyTorch LLM fine-tuning
│   ├── flash-attention/ # IO-aware attention (2-4x faster)
│   ├── bitsandbytes/    # 8-bit/4-bit quantization
│   ├── exllamav2/       # Fast quantized inference
│   ├── peft/            # Parameter-efficient fine-tuning
│   ├── sglang/          # Fast LLM serving
│   ├── llama-factory/   # One-stop fine-tuning platform
│   ├── axolotl/         # Streamlined fine-tuning toolkit
│   ├── tokenlab/        # Token usage & cost tracker
│   ├── routerlab/       # Multi-provider AI routing
│   ├── benchlab/        # Multi-provider benchmarking
│   └── evaluation/      # Evaluation benchmarks (LM harness, MTEB, etc.)
├── scripts/             # Automation scripts
├── configs/             # Tuning configs (per model, per hardware)
├── benchmarks/          # Benchmark results & reports
├── results/             # Tuned model outputs & comparison reports
└── docs/                # Workflow documentation
```

## 🎯 Core Workflows

### 1. Quantization Pipeline
```bash
# Compare quantization methods on a target model
python scripts/quantize_compare.py --model meta-llama/Llama-3-8B --methods awq,gptq,bitsandbytes
```

### 2. Inference Optimization
```bash
# Auto-tune inference config for target hardware
python scripts/infer_autotune.py --model path/to/model --hardware RTX4090 --target latency_ms
```

### 3. Hyperparameter Search
```bash
# Optuna-based hyperparameter optimization
python scripts/hp_search.py --config configs/llama3_8b.yaml --trials 50
```

### 4. Benchmark & Compare
```bash
# Full benchmark across providers/configs
python scripts/benchmark_all.py --model path/to/model --configs configs/ --out results/
```

## 🔗 Reference Repos

| Repo | Role in AutoTune | Key APIs |
|------|-----------------|----------|
| **Olive** | End-to-end model optimization pipeline | `olive optimize`, `olive finetune` |
| **Optimum** | Hardware-specific optimization | `optimum.onnxruntime`, `optimum.bettertransformer` |
| **AutoAWQ** | Automated AWQ quantization | `AutoAWQForCausalLM`, `awq_config` |
| **TVM** | Compiler-level autotuning | `tvm.autotvm`, `tvm.tir` |
| **TorchAO** | PyTorch native quantization | `torchao.quantize`, `torchao.sparsity` |
| **BitsAndBytes** | 4/8-bit quantization | `BitsAndBytesConfig(load_in_4bit=True)` |
| **ExLlamaV2** | Fast quantized inference | `ExLlamaConfig`, `ExLlamaTokenizer` |
| **GaLore** | Memory-efficient training | `GaLoreAdamW`, `GaLoreOptimizer` |
| **PEFT** | LoRA/QLoRA fine-tuning | `LoraConfig`, `get_peft_model` |
| **SGlang** | High-performance serving | `sglang engine`, `sglang benchmark` |

## 🛠️ Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set model path
export MODEL_PATH=meta-llama/Llama-3-8B

# 3. Run auto-quantization sweep
python scripts/quantize_compare.py --model $MODEL_PATH --output results/

# 4. Run inference benchmark
python scripts/benchmark_all.py --model results/best_quant/ --out results/bench/
```

## 📊 Evaluation Metrics

| Metric | Tool | Target |
|--------|------|--------|
| Inference Latency | sglang / llama.cpp | < 50ms/token |
| Memory Usage | nvidia-smi / torch.cuda | < 8GB VRAM |
| Perplexity | lm-evaluation-harness | < baseline + 5% |
| Quality (MMLU) | lm-evaluation-harness | > baseline - 2% |
| Cost/Token | TokenLab | Minimize |

## 📝 Notes

- All reference repos are **read-only symlinks** — modifications happen in `scripts/` and `configs/`
- Results are versioned in `results/` with timestamps
- Each optimization run produces a comparison report in `benchmarks/`
