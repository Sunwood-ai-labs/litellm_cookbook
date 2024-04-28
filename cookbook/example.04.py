import openai # openai v1.0.0+
import pprint
client = openai.OpenAI(api_key="sk-1234",base_url="http://localhost:4000") # set proxy to base_url
# request sent to model set on litellm proxy, `litellm --model`
pprint.pprint(client.models.list())


response = client.chat.completions.create(model="gemma", messages = [
    {
        "role": "user",
        "content": "これはテストリクエストです、短い詩を書いてください"
    }
])

print(response)