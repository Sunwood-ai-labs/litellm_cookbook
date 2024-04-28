from litellm import completion
import pprint
response = completion(
    model="ollama/llama3", 
    messages=[{ "content": "20語で答えてください。あなたは誰ですか？","role": "user"}], 
    api_base="http://localhost:11434",
)
pprint.pprint(response['choices'][0])

print("--------------------")

response = completion(
    model="ollama/gemma", 
    messages=[{ "content": "20語で答えてください。あなたは誰ですか？","role": "user"}], 
    api_base="http://localhost:11434",
)
pprint.pprint(response['choices'][0])