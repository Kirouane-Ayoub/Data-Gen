import argparse
import os
import random

from models import generate_with_cohere, generate_with_gemini
from save import save_to_file
from spliter import other_spliter, regix_spliter
from tqdm import tqdm

model_mapping = {"cohere": generate_with_cohere, "gemini": generate_with_gemini}
spliter_mapping = {"regix": regix_spliter, "other": other_spliter}


def data_generator(
    input_file_path: str,
    output_file: str,
    formula: str,
    file_format: str,
    model: str,
    model_specific: str,
    spliter: str,
    chunk_size: int,
    overlap: int,
):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_file)
    qa_pairs = []

    try:
        # Read the input file
        with open(input_file_path, encoding="utf-8") as file:
            content = file.read()

        spliter_function = spliter_mapping.get(spliter)
        if not spliter_function:
            print(f"Invalid spliter function: {spliter}")
            return

        chunks = spliter_function(text=content, chunk_size=chunk_size, overlap=overlap)

        # Create a tqdm progress bar
        with tqdm(total=len(chunks), desc="Processing Chunks") as pbar:
            for chunk in chunks:
                if chunk.strip():  # Skip empty chunks
                    temperature = random.uniform(
                        0, 1
                    )  # Generate a random temperature between 0 and 1
                    try:
                        generator_func = model_mapping[model]
                        question, answer = generator_func(
                            chunk, temperature, model_name=model_specific
                        )
                        qa_pairs.append((question, answer))
                    except KeyError:
                        print(f"Invalid model: {model}. Using default model instead.")
                pbar.update(1)  # Update the progress bar

        save_to_file(
            qa_pairs=qa_pairs,
            output_file=output_path,
            formula=formula,
            file_format=file_format,
        )
        print(f"QA dataset saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Q&A pairs from text data using specified models."
    )
    parser.add_argument(
        "input_file_path", type=str, help="Path to the input text file."
    )
    parser.add_argument("output_file", type=str, help="Path to save the output file.")
    parser.add_argument(
        "--spliter",
        type=str,
        default="regix",
        choices=["regix", "other"],
        help="Spliter function to use for splitting the text into chunks.",
    )
    parser.add_argument(
        "--formula",
        type=str,
        default="guanaco",
        help="The formula format to use for formatting the Q&A pairs.",
    )
    parser.add_argument(
        "--file_format",
        type=str,
        default="jsonl",
        choices=["jsonl", "csv"],
        help="Format of the output file.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="cohere",
        choices=["cohere", "gemini"],
        help="Model to use for generating Q&A pairs.",
    )
    parser.add_argument(
        "--model_specific",
        type=str,
        help="Specific version or configuration for the model.",
    )
    parser.add_argument(
        "--chunk_size", type=int, default=1000, help="Number of tokens per chunk."
    )
    parser.add_argument(
        "--overlap",
        type=int,
        default=200,
        help="Number of tokens to overlap between chunks.",
    )

    args = parser.parse_args()

    data_generator(
        args.input_file_path,
        args.output_file,
        args.formula,
        args.file_format,
        args.model,
        args.model_specific,
        args.spliter,
        args.chunk_size,
        args.overlap,
    )
