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

```sh
python src/main.py --help

usage: main.py [-h] [--spliter {regex,word_based_splitter,character_based_splitter,paragraph_based_splitter,sentence_based_splitter}] [--formula {alpaca,guanaco,llama2,chatml}]
               [--file_format {jsonl,csv}] [--model {cohere,gemini,groq,ollama}] [--model_specific MODEL_SPECIFIC] [--chunk_size CHUNK_SIZE] [--overlap OVERLAP]
               input_file_path output_file

Generate Q&A pairs from text data using specified models.

positional arguments:
  input_file_path       Path to the input text file.
  output_file           Path to save the output file.

options:
  -h, --help            show this help message and exit
  --spliter {regex,word_based_splitter,character_based_splitter,paragraph_based_splitter,sentence_based_splitter}
                        Spliter function to use for splitting the text into chunks.
  --formula {alpaca,guanaco,llama2,chatml}
                        The formula format to use for formatting the Q&A pairs.
  --file_format {jsonl,csv}
                        Format of the output file.
  --model {cohere,gemini,groq,ollama}
                        Model to use for generating Q&A pairs.
  --model_specific MODEL_SPECIFIC
                        Specific version or configuration for the model.
  --chunk_size CHUNK_SIZE
                        Number of tokens per chunk.
  --overlap OVERLAP     Number of tokens to overlap between chunks.
```

### Usage Example:

```sh
cd src 
python main.py input_file.txt output_file.jsonl --spliter regex --formula alpaca --file_format jsonl --model ollama --model_specific llama3.1 --chunk_size 500 --overlap 100
```

