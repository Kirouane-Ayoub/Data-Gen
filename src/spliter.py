import re


def regix_spliter(text: str, chunk_size: int, overlap: int):
    # Use regular expressions to find sentence boundaries
    sentence_endings = re.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s")

    sentences = sentence_endings.split(text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= chunk_size:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    # Add overlap to chunks
    if overlap > 0:
        overlapping_chunks = []
        for i in range(len(chunks)):
            start = max(0, i * chunk_size - i * overlap)
            end = start + chunk_size
            overlapping_chunks.append(text[start:end].strip())
        return overlapping_chunks
    else:
        return chunks


def word_based_splitter(text: str, chunk_size: int, overlap: int):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        if len(" ".join(current_chunk + [word])) <= chunk_size:
            current_chunk.append(word)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    # Add overlap to chunks
    if overlap > 0:
        overlapping_chunks = []
        for i in range(len(chunks)):
            start = max(0, i * chunk_size - i * overlap)
            end = start + chunk_size
            overlapping_chunks.append(" ".join(words[start:end]).strip())
        return overlapping_chunks
    else:
        return chunks
