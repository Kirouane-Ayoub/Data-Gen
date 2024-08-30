# LLM Data Generator
```

██████   █████  ████████  █████         ██████  ███████ ███    ██ 
██   ██ ██   ██    ██    ██   ██       ██       ██      ████   ██ 
██   ██ ███████    ██    ███████ █████ ██   ███ █████   ██ ██  ██ 
██   ██ ██   ██    ██    ██   ██       ██    ██ ██      ██  ██ ██ 
██████  ██   ██    ██    ██   ██        ██████  ███████ ██   ████ 

                            LLM Data Generator
```
LLM Data Generator is a Python project designed to generate datasets for training language models (LLMs) using existing LLMs. The project supports multiple LLM providers and allows for flexible configuration of text splitting, model generation, and data saving formats.

## Features

- **Model Integration**: Supports various LLM providers like Cohere and Gemini.
- **Text Splitting**: Splits large text files into smaller chunks for processing.
- **Flexible Output**: Saves generated Q&A pairs in JSONL or CSV formats.
- **Environment Configuration**: Uses environment variables for API keys and other sensitive information.

## Requirements

- Python 3.8+
- Install dependencies from `requirements.txt`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Kirouane-Ayoub/Data-Gen.git
    cd Data-Gen
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your API keys:
    ```ini
    CO_API_KEY=your_cohere_api_key
    GOOGLE_API_KEY=your_gemini_api_key
    GROQ_API_KEY=....
    ```

## Usage

### Command-Line Interface

Run the main script from the command line, specifying the necessary arguments:

```sh
cd src 

python main.py input_file.txt output_file.jsonl --spliter regex --formula guanaco --file_format jsonl --model cohere --model_specific command-r-plus --chunk_size 1000 --overlap 200
```

### Arguments
- `input_file.txt`: Path to the input text file.
- `output_file.jsonl`: Path to save the output file.
- `--spliter`: Spliter function to use (regix or other).
- `--formula`: Formula format for Q&A pairs (guanaco, alpaca, etc.).
- `--file_format`: Output file format (jsonl or csv).
- `--model`: Model to use for generating Q&A pairs (cohere or gemini).
- `--model_specific`: Specific version or configuration for the model.
- `--chunk_size`: Number of tokens per chunk.
- `--overlap`: Number of tokens to overlap between chunks.
