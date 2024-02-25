import chainlit as cl 
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


# pass the user message to chat.completion api, and display the chat_completion response
@cl.on_message
async def main(message : cl.Message):
    chat_completion = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a nerdy assistant."},
            {"role": "user", "content": message.content}
        ]
    )
    await cl.Message(content = chat_completion.choices[0].message.content).send()
