from transformers import pipeline

chat_model = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
)

async def ask_gpt(prompt: str) -> str:
    prompt = prompt.strip()
    if not prompt:
        return "Напиши что-нибудь :)"

    response = chat_model(
        prompt,
        max_new_tokens=300,
        temperature=0.7,
        do_sample=True,
    )

    text = response[0]["generated_text"].replace(prompt, "").strip()
    return text[:1000]
