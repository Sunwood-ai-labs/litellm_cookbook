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

cathy = ConversableAgent(
    "cathy",
    system_message="あなたの名前はキャシーです。あなたはコメディアンのデュオの一員です。",
    llm_config=local_llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

joe = ConversableAgent(
    "joe",
    system_message="あなたの名前はジョーで、コメディアンのデュオの一員です。",
    llm_config=local_llm_config,
    human_input_mode="NEVER",  # Never ask for human input.
)

result = joe.initiate_chat(cathy, message="好きなアニメについて語り合って", max_turns=3)