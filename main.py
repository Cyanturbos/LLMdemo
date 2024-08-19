from openai import AsyncOpenAI
import chainlit as cl
#client = AsyncOpenAI()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Instrument the OpenAI client
cl.instrument_openai()

settings = {
    "model": "gpt-4o-mini",
    "temperature": 0,
    # ... more settings
}

@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful bot, you always reply in Spanish",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()

if __name__ == "__main__":
    cl.run()
