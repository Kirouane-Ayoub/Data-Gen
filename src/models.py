import cohere
import google.generativeai as genai
import settings
from groq import Groq
from openai import OpenAI


def prompt(text_chunk):
    return f"Generate without using any markdowns only one Question and its corresponding Answer based on this text: {text_chunk}"


def generate_with_cohere(text_chunk, temperature, model_name):
    model_name = model_name or settings.DEFAULT_COHERE
    co = cohere.Client(settings.CO_API_KEY)
    response = co.chat(
        message=prompt(text_chunk),
        model=model_name,
        temperature=temperature,
    )
    question, answer = response.text.split("Answer:", 1)
    return question.strip(), answer.strip()


def generate_with_gemini(text_chunk, temperature, model_name):
    model_name = model_name or settings.DEFAULT_GEMINI
    genai.configure(api_key=settings.GOOGLE_API_KEY)
    generation_config = {"temperature": temperature}
    gen_model = genai.GenerativeModel(model_name, generation_config=generation_config)
    response = gen_model.generate_content(prompt(text_chunk))
    question, answer = response.text.split("Answer:", 1)
    return question.strip(), answer.strip()


def generarte_with_groq(text_chunk, temperature, model_name):
    model_name = model_name or settings.DEFAULT_GROQ
    client = Groq(api_key=settings.GROQ_API_KEY)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt(text_chunk),
            }
        ],
        model=model_name,
        temperature=temperature,
    )
    response = chat_completion.choices[0].message.content
    question, answer = response.split("Answer:", 1)
    return question.strip(), answer.strip()


def generarte_with_ollama(text_chunk, temperature, model_name):
    model_name = model_name or settings.DEFAULT_OLLAMA
    client = OpenAI(base_url="http://127.0.0.1:11434/v1", api_key="ollama")
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You are an advanced language model designed to follow instructions precisely.",
            },
            {
                "role": "user",
                "content": prompt(text_chunk),
            },
        ],
        temperature=temperature,
    )
    response = response.choices[0].message.content
    question, answer = response.split("\n", 1)
    return question.strip(), answer.strip()
