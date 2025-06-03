import os
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam, ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam

class CHAT:
    _client_async: AsyncOpenAI | None = None

    @staticmethod
    def _get_instance(
        base_url: str | None = None, api_key: str | None = None
    ) -> AsyncOpenAI:
        if CHAT._client_async is None:
            base_url = base_url or os.environ.get("BASE_URL")
            if base_url is None:
                raise AssertionError("Enter a valid Base URL")

            api_key = api_key or os.environ.get("API_KEY")
            if base_url is None:
                raise AssertionError("Enter a valid API Key")
            
            CHAT._client_async = AsyncOpenAI(base_url=base_url, api_key=api_key)
        return CHAT._client_async
    
    @staticmethod
    async def chat(
        prompt: str,
        system_prompt: str | None = None,
        history: list[dict] = [],
        model: str = "gpt-4o",
        base_url: str | None = None,
        api_key: str | None = None,
        **kwargs,
    ) -> str:
        client_async = CHAT._get_instance(base_url=base_url, api_key=api_key)
        model = os.environ.get("LLM_MODEL") | "gpt-4o-mini"

        messages: list[ChatCompletionMessageParam] = []
        if system_prompt:
            messages.append(
                ChatCompletionSystemMessageParam(role="system", content=system_prompt)
            )

        if history:
            messages.extend(history)
        messages.append(ChatCompletionUserMessageParam(role="user", content=prompt))

        response: ChatCompletion = await client_async.chat.completions.create(
            model=model, messages=messages, max_tokens=8192, **kwargs
        )

        content = response.choices[0].message.content
        if content is None:
            raise ValueError("None response returned")
        return content
    