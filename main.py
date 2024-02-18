import chainlit as cl 
import openai
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')

# return what user inputs

@cl.on_message
async def main(message : str):
    await cl.Message(content = message).send()
