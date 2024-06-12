import cohere
import google.generativeai as genai
import settings


def generate_with_cohere(text_chunk, temperature, model_name):
    model_name = settings.DEFAULT_COHERE if model_name else None
    co = cohere.Client(settings.CO_API_KEY)
    response = co.chat(
        message=f"Generate a question and answer based on: {text_chunk}",
        model=model_name,
        temperature=temperature,
    )
    question, answer = response.text.split("Answer:", 1)
    return question.strip(), answer.strip()


def generate_with_gemini(text_chunk, temperature, model_name):
    model_name = settings.DEFAULT_COHERE if model_name else None
    genai.configure(api_key=settings.GOOGLE_API_KEY)
    generation_config = {"": temperature}
    gen_model = genai.GenerativeModel(model_name, generation_config=generation_config)
    response = gen_model.generate_content(
        f"Generate a question and answer based on: {text_chunk}"
    )
    question, answer = response.text.split("Answer:", 1)
    return question.strip(), answer.strip()
