from litellm import completion
import pprint

response = completion(
    model="ollama/gemma", 
    messages=[{ "content": "あなたの今日の架空の予定を教えて","role": "user"}], 
    api_base="http://localhost:11434",
)
pprint.pprint(response['choices'][0])