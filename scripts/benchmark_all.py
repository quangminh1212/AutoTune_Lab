#!/usr/bin/env python3
"""
AutoTune — Inference benchmark runner.

Tests multiple model configs (quantized/fp16) on a set of
benchmark prompts and reports latency, throughput, memory.
"""

import argparse
import json
import time
import torch
from pathlib import Path


def benchmark_model(model_path: str, prompts: list[str], warmup: int = 3, runs: int = 10):
    """Run inference benchmark on a model, return metrics."""
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, device_map="auto", torch_dtype=torch.bfloat16
    )
    model.eval()

    # Warmup
    for _ in range(warmup):
        inputs = tokenizer(prompts[0], return_tensors="pt").to("cuda")
        with torch.no_grad():
            model.generate(**inputs, max_new_tokens=128)

    latencies = []
    for prompt in prompts:
        inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
        torch.cuda.synchronize()
        start = time.perf_counter()
        with torch.no_grad():
            out = model.generate(**inputs, max_new_tokens=128)
        torch.cuda.synchronize()
        elapsed = time.perf_counter() - start
        tokens = out.shape[1] - inputs.input_ids.shape[1]
        latencies.append(elapsed / tokens)

    mem_gb = torch.cuda.max_memory_allocated() / 1024 / 1024 / 1024
    return {
        "latency_ms_per_token": round(sum(latencies) / len(latencies) * 1000, 2),
        "throughput_tokens_per_sec": round(1.0 / (sum(latencies) / len(latencies)), 2),
        "peak_memory_gb": round(mem_gb, 2),
        "device": torch.cuda.get_device_name(0),
    }


def main():
    parser = argparse.ArgumentParser(description="Inference autotune benchmark")
    parser.add_argument("--model", required=True, help="Model path or name")
    parser.add_argument("--config", default="configs/llama3_8b.yaml", help="Config YAML")
    parser.add_argument("--out", default="results/benchmark.json", help="Output path")
    args = parser.parse_args()

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    prompts = [
        "Explain the concept of quantum computing in simple terms.",
        "Write a Python function for binary search.",
        "What are the main differences between REST and GraphQL?",
    ]

    print(f"Benchmarking: {args.model}")
    metrics = benchmark_model(args.model, prompts)

    with open(out_path, "w") as f:
        json.dump({"model": args.model, **metrics}, f, indent=2)
    print(f"Results → {out_path}")
    for k, v in metrics.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
