from openai import AsyncOpenAI
import chainlit as cl
#client = AsyncOpenAI()
client = AsyncOpenAI(
    openai_api_key=None,        # OpenAI API 密钥（默认从环境变量读取）
    temperature=1,              # 生成文本的随机性，默认是 1
    model_name="gpt-4o-mini", # 使用的模型名称，默认是 "gpt-3.5-turbo"
    max_tokens=256,             # 最大 token 长度，默认是 256
    top_p=1,                    # 对生成结果的筛选程度，默认是 1
    frequency_penalty=0,        # 控制重复用词的程度，默认是 0
    presence_penalty=0,         # 控制话题新颖性的程度，默认是 0
    request_timeout=60,         # 请求超时时间，默认是 60 秒
    logit_bias=None,            # 控制特定词语的生成概率，默认是 None
    n=1                         # 生成的文本数量，默认是 1
)


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
