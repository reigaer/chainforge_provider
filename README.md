# ChainForge LLM provider

I use Simon Willison's **[LLM](https://github.com/simonw/llm)** ([docs](https://llm.datasette.io/)) as my primary tool for interacting with language models. This provider connects it to **[ChainForge](https://github.com/ianarawjo/ChainForge)** ([docs](https://www.chainforge.ai/docs/)), allowing me to use my LLM-configured models in ChainForge's visual environment for testing and evaluation.

## Why this integration?

I created this because:
- LLM provides quick access to new models through its plugin system
- It handles all my API keys and model configurations in one place
- ChainForge offers great tools for testing and evaluation
- Together, they create a practical workflow for model experimentation

## Quick start

1. Install LLM globally (if not already installed):
```bash
# Install LLM using Homebrew
brew install llm

# Configure your models
llm keys set openai
llm keys set anthropic

# Add any desired plugins
llm install llm-ollama  # For Ollama
llm install llm-gguf    # For GGUF models
```

2. Set up ChainForge with system access to LLM:
```bash
# Create project directory
mkdir chainforge-project
cd chainforge-project

# Create virtual environment with system access
uv venv --system-site-packages
source .venv/bin/activate

# Install ChainForge
pip install chainforge

# Verify LLM is accessible
which llm
llm --version
```

3. Connect ChainForge to LLM:
   - Start ChainForge: `chainforge serve`
   - Open `localhost:8000`
   - Settings → Custom Providers → Add `llm_provider.py`
   - Select "LLM CLI" in model dropdowns

## Troubleshooting

- **Models not showing**: Re-add the provider
- **LLM not found**: Ensure virtual environment was created with `--system-site-packages`
- **Access issues**: Check `llm keys list` in terminal

## Credits

- [LLM](https://github.com/simonw/llm) by Simon Willison
- [ChainForge](https://github.com/ianarawjo/ChainForge) by Ian Arawjo et al.

## License

MIT License
