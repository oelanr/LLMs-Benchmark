# LLMs-Benchmark

Small Jupyter notebook benchmark (bench.ipynb) created during an internship to compare latency and responses between two LLMs from the same provider and generation but with different parameter counts (example: Llama-3.2 1B vs 3B). The experiments cover multiple task types and prompt-engineering variations.

Contents
- bench.ipynb — runs scenarios (few-shot QA, summarization, chain-of-thought, arithmetic, etc.), measures per-request latency, saves timestamped CSVs, and shows simple plots.

Quickstart
1. Clone:
   `git clone https://github.com/oelanr/LLMs-Benchmark.git`
2. Setup:
  ` python -m venv .venv`
  ` source .venv/bin/activate`
   `pip install jupyterlab python-dotenv pandas matplotlib aisuite`
3. Add API creds in a `.env` (used by `aisuite`), then run jupyter lab and open bench.ipynb

What it does (brief)
- Benchmarks two or more models listed in the `llms` variable (provider:model strings).
- Calls models via `aisuite` client, records wall-clock execution time and responses.
- Saves results to `llm_comparison_<timestamp>.csv`.
- Plots mean execution time per model.
- Includes experiments across many task types and prompt-engineering setups to compare robustness, latency, and response differences between parameter counts.

Notes
- Execution time includes network latency and service processing.
- Adjust `llms`, prompts, and `max_length` as needed. Be mindful of API rate limits and cost.

License
- Add a LICENSE file if you want to publish/redistribute.
