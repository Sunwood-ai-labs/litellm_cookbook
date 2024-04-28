from litellm import completion
import pprint
response = completion(
    model="ollama/llama3", 
    messages=[{ "content": "respond in 20 words. who are you?","role": "user"}], 
    api_base="http://localhost:11434",
)
pprint.pprint(response['choices'][0])
#for chunk in response:
#    print(chunk['choices'][0]['delta'])