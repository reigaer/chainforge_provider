from chainforge.providers import provider
import subprocess
import json
import os

def get_available_models():
    """Fetch available models from llm CLI"""
    try:
        result = subprocess.run(["llm", "models"], 
                              capture_output=True, 
                              text=True, 
                              check=True)
        
        models = []
        for line in result.stdout.splitlines():
            line = line.strip()
            if line:
                # Split on ':' to separate provider and model
                parts = line.split(':', 1)
                if len(parts) == 2:
                    model_info = parts[1].strip()
                    # Split on space and parentheses to get model name and aliases
                    model_parts = model_info.split(' (', 1)
                    model_name = model_parts[0].strip()
                    if model_name:
                        models.append(model_name)
                        # If there are aliases, add them too
                        if len(model_parts) > 1 and 'aliases:' in model_parts[1]:
                            aliases = model_parts[1].split('aliases:', 1)[1].strip(' )')
                            models.extend([alias.strip() for alias in aliases.split(',')])
        
        # Return unique models, sorted
        return sorted(list(set(models)))
    except Exception as e:
        print(f"Error fetching models: {e}")
        return ['gpt-4-turbo-preview', 'gpt-3.5-turbo', 'claude-3-opus', 'claude-3-sonnet']

@provider(name="llm CLI", emoji="🚀", 
         models=get_available_models(),
         rate_limit="sequential",
         settings_schema={
    "settings": {
        "temperature": {
            "type": "number",
            "title": "temperature",
            "description": "Controls randomness in responses",
            "default": 0.7,
            "minimum": 0,
            "maximum": 2.0,
        },
        "system": {
            "type": "string",
            "title": "system",
            "description": "System prompt for chat models",
            "default": ""
        },
        "max_tokens": {
            "type": "integer",
            "title": "max_tokens",
            "description": "Maximum length of response",
            "default": 1000,
            "minimum": 1,
            "maximum": 4000,
        }
    },
    "ui": {
        "temperature": {
            "ui:help": "Higher values = more random",
            "ui:widget": "range"
        },
        "system": {
            "ui:widget": "textarea",
            "ui:help": "Optional system prompt"
        },
        "max_tokens": {
            "ui:help": "Maximum response length",
            "ui:widget": "range"
        }
    }
})
def llm_completion(prompt: str, 
                  model: str = "gpt-4-turbo-preview",
                  temperature: float = 0.7,
                  system: str = "",
                  max_tokens: int = 1000,
                  chat_history: list = None,
                  **kwargs) -> str:
    """Custom provider using llm CLI tool"""
    try:
        # Start with basic command
        cmd = ["llm", "prompt", "-m", model]
        
        # Add options using environment variables for parameters
        os.environ["LLM_TEMPERATURE"] = str(temperature)
        os.environ["LLM_MAX_TOKENS"] = str(max_tokens)
        
        # Handle chat vs completion based on presence of chat history
        if chat_history or system:
            messages = []
            if system:
                messages.append({"role": "system", "content": system})
            if chat_history:
                for msg in chat_history:
                    messages.append({"role": msg["role"], "content": msg["content"]})
            messages.append({"role": "user", "content": prompt})
            
            # Save messages to a temporary file or pass as environment variable
            os.environ["LLM_MESSAGES"] = json.dumps(messages)
            cmd.extend(["--messages-env", "LLM_MESSAGES"])
        else:
            # For simple prompts, just add the prompt at the end
            cmd.append(prompt)

        # Run the command
        result = subprocess.run(cmd, 
                              capture_output=True, 
                              text=True, 
                              check=True)
        
        return result.stdout.strip()

    except subprocess.CalledProcessError as e:
        error_msg = f"llm CLI error: {e.stderr}"
        print(error_msg)
        return f"Error: {error_msg}"
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(error_msg)
        return f"Error: {error_msg}"