import csv
import json


# Function to format the text based on the selected formula
def format_text(question: str, answer: str, formula: str, context=str):
    # Dictionary with different formatting options for each formula
    formula_options = {
        "alpaca": f"### Context:\n{context}\n\n### Question:\n{question}\n\n### Answer:\n{answer}\n",
        "guanaco": f"### Human: {question}\n### Assistant: {answer}\n",
        "llama2": f"[INST] {question} [/INST]\n{answer}\n[INST] {question} [/INST]\n{answer}\n",
        "chatml": f"<|im_start|> user \n{question}\n<|im_end|> \n\n<|im_start|> assistant \n{answer} <|im_end|>\n",
    }
    # Return the formatted text based on the selected formula
    return formula_options.get(formula, "")


# Function to save the formatted data to a file
def save_to_file(
    qa_pairs, output_file: str, formula: str, file_format: str, context=None
):
    # Determine if 'Context' field should be included
    context_field = "Context" if context else None

    # Save data in JSONL format
    if file_format == "jsonl":
        with open(output_file, mode="w", encoding="utf-8") as file:
            for question, answer in qa_pairs:
                # Format the text for the current question-answer pair
                text = format_text(question, answer, formula, context)
                # Create a JSON record with 'Question', 'Answer', 'Text', and optional 'Context' fields
                json_record = {"Question": question, "Answer": answer, "Text": text}
                if context_field:
                    json_record["Context"] = context

                # Write the JSON record to the file
                file.write(json.dumps(json_record) + "\n")

    # Save data in CSV format
    elif file_format == "csv":
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # Define the headers for the CSV file
            headers = ["Context", "Question", "Answer", "Text"]
            # Remove 'Context' header if it's not needed
            if not context_field:
                headers.remove("Context")
            # Write the headers to the CSV file
            writer.writerow(headers)

            # Iterate through each question-answer pair and write to the CSV file
            for question, answer in qa_pairs:
                # Format the text for the current question-answer pair
                text = format_text(question, answer, formula, context)
                # Create a row with 'Context', 'Question', 'Answer', and 'Text' fields
                row = [context, question, answer, text]
                # Remove 'Context' field if it's not needed
                if not context_field:
                    row.pop(0)
                # Write the row to the CSV file
                writer.writerow(row)
