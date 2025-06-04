import os
import openai
import chainlit as cl
from dotenv import load_dotenv
import time

# Load environment
load_dotenv()

client = openai.AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

@cl.on_message
async def handle_message(message: cl.Message):
    start_time = time.time()

    # Message that will be updated with stream
    streaming_message = cl.Message(content="")
    await streaming_message.send()

    full_content = ""
    model_used = None

    # 1. STREAMING the response
    stream_response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.content}
        ],
        stream=True
    )

    for chunk in stream_response:
        if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            full_content += token
            await streaming_message.stream_token(token)

        if not model_used and hasattr(chunk, "model"):
            model_used = chunk.model

    elapsed_time = time.time() - start_time

    # 2. SECOND CALL to get metadata (usage and model)
    metadata_response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message.content},
            {"role": "assistant", "content": full_content}
        ],
        stream=False  # now, to get usage
    )

    model_used = metadata_response.model or model_used
    usage = metadata_response.usage
    prompt_tokens = usage.prompt_tokens
    completion_tokens = usage.completion_tokens
    total_tokens = usage.total_tokens

    # 3. Show final metadata
    await cl.Message(
        author="ℹ️ Metadata",
        content=(
            f"### 📊 Response Info\n"
            f"- 🧠 **Model**: `{model_used}`\n"
            f"- ⏱ **Response time**: `{elapsed_time:.2f} seconds`\n"
            f"- 🔢 **Tokens**:\n"
            f"  - Prompt: `{prompt_tokens}`\n"
            f"  - Completion: `{completion_tokens}`\n"
            f"  - Total: `{total_tokens}`"
        )
    ).send()
