# ChainForge LLM Provider

A custom provider connecting two powerful tools for LLM experimentation:
- **[ChainForge](https://github.com/ianarawjo/ChainForge)** ([docs](https://www.chainforge.ai/docs/)): A visual tool for testing and evaluating language models. It lets you design prompt templates, run experiments across multiple models, and analyze results - all through an intuitive drag-and-drop interface. Think of it as a visual laboratory for prompt engineering and model evaluation.
- **[LLM](https://github.com/simonw/llm)** ([docs](https://llm.datasette.io/)): Simon Willison's excellent command-line tool that provides seamless access to both cloud and local language models. It's become the daily driver for many developers working with LLMs.

This integration brings LLM's extensive model support to ChainForge's visual experimentation environment.

## Why LLM?

LLM has become an essential tool in the LLM ecosystem because it:
- Consistently provides day-one support for new models
- Makes daily interactions with LLMs frictionless through both CLI and Python API
- Maintains a robust plugin ecosystem for cloud and local models
- Features clear documentation and responsive maintenance
- Takes an open source, community-driven approach

## Why This Provider?

1. **Single Point of Configuration**: 
   - Manage all your API keys and models in one place via LLM
   - No need to reconfigure credentials in ChainForge
   - New models become available instantly through LLM's plugin system

2. **Comprehensive Model Support**:
   - Cloud APIs: OpenAI, Anthropic, Mistral, and more
   - Local models: Ollama, GGUF, MLC, GPT4All
   - See the full [plugin directory](https://llm.datasette.io/en/stable/plugins/directory.html)

3. **Visual Experimentation**:
   - Design and test prompt templates
   - Compare responses across different models
   - Set up automated evaluation pipelines
   - Visualize results

## Quick Start

1. Install the tools:
```bash
# Install LLM
brew install llm

# Install ChainForge in a virtual environment
mkdir chainforge-project && cd chainforge-project
uv venv --system-site-packages  # or: python -m venv venv --system-site-packages
source .venv/bin/activate       # or: source venv/bin/activate
pip install chainforge
```

2. Set up your models (only once):
```bash
# Cloud APIs
llm keys set openai
llm keys set anthropic

# Local models
llm install llm-ollama  # For Ollama
llm install llm-gguf    # For GGUF models
```

3. Connect ChainForge:
   - Start ChainForge: `chainforge serve`
   - Open `localhost:8000`
   - Settings → Custom Providers → Add `llm_provider.py`
   - Select "LLM CLI" in model dropdowns

## Troubleshooting

- **Models not showing**: Re-add the provider
- **LLM not found**: Check `which llm` and PATH
- **Access issues**: Verify keys with `llm keys list`

## Credits

This provider combines:
- [LLM](https://github.com/simonw/llm) by Simon Willison - a tool that's fundamentally changed how many of us work with language models
- [ChainForge](https://github.com/ianarawjo/ChainForge) by Ian Arawjo et al.

## License

MIT License