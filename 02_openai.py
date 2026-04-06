from openai import OpenAI

# pip install openai
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a person named karan who speaks hindi as well as english. He i from India and is a coder. You are analyze chat hitory and respond like Karan"},
        {"role": "user", "content": "what is coding"}
    ]
)

print (completion.choices[0].message)