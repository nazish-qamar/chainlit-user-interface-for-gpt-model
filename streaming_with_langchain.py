import chainlit as cl
from langchain import PromptTemplate, OpenAI, LLMChain

template = """Question: {question}

Answer: Let's think step by step"""

@cl.on_chat_start
def main():
    prompt = PromptTemplate(template=template, 
                            input_variables=["question"])
    llm_chain = LLMChain(
        prompt=prompt,
        llm=OpenAI(model="gpt-3.5-turbo-instruct", temperature=0, max_tokens=512),
        verbose=True,
    )

    cl.user_session.set("llm_chain", llm_chain)

@cl.on_message
async def main(message : cl.Message):
    llm_chain = cl.user_session.get("llm_chain")

    res = await llm_chain.acall(message.content, callbacks = [cl.AsyncLangchainCallbackHandler()])
    await cl.Message(content=str(res)).send()
