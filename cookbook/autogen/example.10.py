from autogen import UserProxyAgent, ConversableAgent
#
# pip install pyautogen
# https://microsoft.github.io/autogen/docs/installation/
#
local_llm_config={
    "config_list": [
        {
            "model": "gemma",
            "api_key": "sk-1234",
            "base_url": "http://localhost:4000"
        }
    ],
    "cache_seed": None # Turns off caching, useful for testing different models
}

# Create the agent that uses the LLM.
assistant = ConversableAgent("agent", llm_config=local_llm_config)

# Create the agent that represents the user in the conversation.
user_proxy = UserProxyAgent("user", code_execution_config=False)

# Let the assistant start the conversation.  It will end when the user types exit.
assistant.initiate_chat(user_proxy, message="How can I help you today?")