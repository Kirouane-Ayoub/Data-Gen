import re


def regex_splitter(text: str, chunk_size: int, overlap: int):
    """
    Splits the input text into chunks of the specified size with optional overlap.

    :param text: The input text to be split.
    :param chunk_size: The size of each chunk.
    :param overlap: The amount of overlap between consecutive chunks.
    :return: A list of text chunks.
    """
    # Regular expression to match sentence endings (period, question mark, etc.)
    sentence_endings = re.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s")

    # Split the text into sentences based on sentence endings
    sentences = sentence_endings.split(text)

    # Initialize variables for chunking
    chunks = []
    current_chunk = ""

    # Iterate through each sentence and create chunks
    for sentence in sentences:
        # If adding the current sentence to the current chunk doesn't exceed the chunk size, add it
        if len(current_chunk) + len(sentence) + 1 <= chunk_size:
            current_chunk += " " + sentence
        # Otherwise, add the current chunk to the list and reset it
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence

    # Add the last chunk if it exists
    if current_chunk:
        chunks.append(current_chunk.strip())

    # If overlap is specified, create overlapping chunks
    if overlap > 0:
        overlapping_chunks = []
        for i in range(len(chunks)):
            # Calculate the start and end indices for the current overlapping chunk
            start = max(0, i * chunk_size - i * overlap)
            end = start + chunk_size
            # Add the overlapping chunk to the list
            overlapping_chunks.append(text[start:end].strip())
        return overlapping_chunks
    else:
        return chunks


def word_based_splitter(text: str, chunk_size: int, overlap: int):
    """
    Splits the input text into chunks of the specified size with optional overlap based on word boundaries.

    :param text: The input text to be split.
    :param chunk_size: The size of each chunk (in characters).
    :param overlap: The amount of overlap between consecutive chunks (in characters).
    :return: A list of text chunks.
    """
    # Split the text into words
    words = text.split()

    # Initialize variables for chunking
    chunks = []
    current_chunk = []

    # Iterate through each word and create chunks
    for word in words:
        # Check if adding the current word to the current chunk exceeds the chunk size
        if len(" ".join(current_chunk + [word])) <= chunk_size:
            # If it doesn't exceed, add the word to the current chunk
            current_chunk.append(word)
        else:
            # If it exceeds, add the current chunk to the list of chunks and reset it
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]

    # Add the last chunk if it exists
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    # If overlap is specified, create overlapping chunks
    if overlap > 0:
        overlapping_chunks = []
        for i in range(len(chunks)):
            # Calculate the start and end indices for the current overlapping chunk
            start = max(0, i * chunk_size - i * overlap)
            end = start + chunk_size
            # Add the overlapping chunk to the list
            overlapping_chunks.append(" ".join(words[start:end]).strip())
        return overlapping_chunks
    else:
        # If no overlap is specified, return the non-overlapping chunks
        return chunks


def character_based_splitter(text: str, chunk_size: int, overlap: int) -> list:
    """
    Splits the input text into chunks of the specified size with optional overlap based on character count.

    :param text: The input text to be split.
    :param chunk_size: The size of each chunk (in characters).
    :param overlap: The amount of overlap between consecutive chunks (in characters).
    :return: A list of text chunks.
    """
    # Initialize an empty list to store the chunks
    chunks = []

    # Iterate over the text with a step size of (chunk_size - overlap)
    for i in range(0, len(text), chunk_size - overlap):
        # Extract the current chunk from the text
        chunk = text[i : i + chunk_size]
        # Remove leading and trailing whitespace from the chunk
        chunk = chunk.strip()
        # Append the chunk to the list of chunks
        chunks.append(chunk)

    # Return the list of chunks
    return chunks


def paragraph_based_splitter(text: str, chunk_size: int, overlap: int) -> list:
    """
    Splits the input text into chunks of the specified size with optional overlap based on paragraph boundaries.

    :param text: The input text to be split.
    :param chunk_size: The size of each chunk (in characters).
    :param overlap: The amount of overlap between consecutive chunks (in characters).
    :return: A list of text chunks.
    """
    # Split the text into paragraphs based on newline characters
    paragraphs = text.split("\n")

    # Initialize variables for chunking
    chunks = []
    current_chunk = ""

    # Iterate through each paragraph and create chunks
    for paragraph in paragraphs:
        # Check if adding the current paragraph to the current chunk exceeds the chunk size
        if len(current_chunk) + len(paragraph) + 1 <= chunk_size:
            # If it doesn't exceed, add the paragraph to the current chunk with a newline separator
            current_chunk += "\n" + paragraph
        else:
            # If it exceeds, add the current chunk to the list of chunks and reset it
            chunks.append(current_chunk.strip())
            current_chunk = paragraph

    # Add the last chunk if it exists
    if current_chunk:
        chunks.append(current_chunk.strip())

    # If overlap is specified, create overlapping chunks
    if overlap > 0:
        overlapping_chunks = []
        for i in range(len(chunks)):
            # Calculate the start and end indices for the current overlapping chunk
            start = max(0, i * chunk_size - i * overlap)
            end = start + chunk_size
            # Add the overlapping chunk to the list
            overlapping_chunks.append(text[start:end].strip())
        # Return the list of overlapping chunks
        return overlapping_chunks
    else:
        # If no overlap is specified, return the non-overlapping chunks
        return chunks


def sentence_based_splitter(text: str, chunk_size: int, overlap: int) -> list:
    """
    Splits the input text into chunks of the specified size with optional overlap based on sentence boundaries.

    :param text: The input text to be split.
    :param chunk_size: The size of each chunk (in characters).
    :param overlap: The amount of overlap between consecutive chunks (in characters).
    :return: A list of text chunks.
    """
    # Import necessary libraries and download the required NLTK resources
    import nltk

    nltk.download("punkt")
    from nltk.tokenize import sent_tokenize

    # Tokenize the input text into sentences
    sentences = sent_tokenize(text)

    # Initialize variables for chunking
    chunks = []
    current_chunk = ""

    # Iterate through each sentence and create chunks
    for sentence in sentences:
        # Check if adding the current sentence to the current chunk exceeds the chunk size
        if len(current_chunk) + len(sentence) + 1 <= chunk_size:
            # If it doesn't exceed, add the sentence to the current chunk with a space separator
            current_chunk += " " + sentence
        else:
            # If it exceeds, add the current chunk to the list of chunks and reset it
            chunks.append(current_chunk.strip())
            current_chunk = sentence

    # Add the last chunk if it exists
    if current_chunk:
        chunks.append(current_chunk.strip())

    # If overlap is specified, create overlapping chunks
    if overlap > 0:
        overlapping_chunks = []
        for i in range(len(chunks)):
            # Calculate the start and end indices for the current overlapping chunk
            start = max(0, i * chunk_size - i * overlap)
            end = start + chunk_size
            # Add the overlapping chunk to the list
            overlapping_chunks.append(text[start:end].strip())
        # Return the list of overlapping chunks
        return overlapping_chunks
    else:
        # If no overlap is specified, return the non-overlapping chunks
        return chunks
