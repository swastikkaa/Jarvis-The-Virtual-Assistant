from openai import OpenAI 
client=OpenAI(
api_key="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"
)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistantnamed Sarah, skilled in general tasks like alexa and siri"},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message.content)
