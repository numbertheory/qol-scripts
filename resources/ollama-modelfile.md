# Ollama Modelfile Reference

## Basic Workflow
1. Write a `Modelfile`
2. Build: `ollama create <name> -f ./Modelfile`
3. Run:   `ollama run <name>`

## Directives
FROM <model|path>       Base model (llama3.2, ./model.gguf) [Required]
PARAMETER <key> <val>   Set runtime inference parameter
SYSTEM """<prompt>"""   System instructions & persona (triple quotes)
TEMPLATE """<format>""" Go prompt template (e.g. ChatML)
ADAPTER <path>          Path to LoRA adapter (.bin or .gguf)
LICENSE """<text>"""    Model distribution license
MESSAGE <role> <msg>    Seed few-shot conversation history

## Key Parameters
temperature <float>     0.0-2.0 (lower = deterministic/code, higher = creative)
top_p <float>           Nucleus sampling cutoff (default: 0.9)
top_k <int>             Token candidate pool size (default: 40)
num_ctx <int>           Context window size in tokens (4096, 8192, 16384)
stop "<string>"         Stop token (repeatable, e.g. stop "<|im_end|>")
repeat_penalty <float>  Penalize repetition (default: 1.1)

## Minimal Example (Python Specialist)
FROM llama3.2
PARAMETER temperature 0.2
PARAMETER num_ctx 8192
SYSTEM """
You are an expert Python engineer. Output clean, typed Python code.
Do not include conversational filler unless requested.
"""

## GGUF Import Example
FROM ./model.Q4_K_M.gguf
TEMPLATE """<|im_start|>system
{{ .System }}<|im_end|>
<|im_start|>user
{{ .Prompt }}<|im_end|>
<|im_start|>assistant
"""
PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"

## Useful Commands
ollama create <name> -f Modelfile   Build model from file
ollama show --modelfile <name>      Inspect existing model's Modelfile
ollama list                         List local models
ollama rm <name>                    Delete local model
