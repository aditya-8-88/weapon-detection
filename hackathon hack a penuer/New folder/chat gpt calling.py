import openai

details = "You have to educate bank employees on effective security protocols and how to respond during a robbery.Focus on providing realistic simulations, crisis management techniques, and guidelines for minimizing risks to personnel and customers bullet point wise."
openai.api_key = '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'
msg = "help"

response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[
        {"role": "system", "content": details},
        {"role": "assistant", "content": details },
        {"role": "user", "content": msg},
    ]
)
text = response["choices"][0]["message"]["content"]
with open("text.txt","w") as wf:
          wf.write(text)