import csv
import json


def format_text(question: str, answer: str, formula: str, context=str):
    formula_options = {
        "alpaca": f"### Context:\n{context}\n\n### Question:\n{question}\n\n### Answer:\n{answer}\n",
        "guanaco": f"### Human: {question}\n### Assistant: {answer}\n",
        "llama2": f"[INST] {question} [/INST]\n{answer}\n[INST] {question} [/INST]\n{answer}\n",
        "chatml": f"<|im_start|> user \n{question}\n<|im_end|> \n\n<|im_start|> assistant \n{answer} <|im_end|>\n",
    }
    return formula_options.get(formula, "")


def save_to_file(
    qa_pairs, output_file: str, formula: str, file_format: str, context=None
):
    context_field = "Context" if context else None

    if file_format == "jsonl":
        with open(output_file, mode="w", encoding="utf-8") as file:
            for question, answer in qa_pairs:
                text = format_text(question, answer, formula, context)
                json_record = {"Question": question, "Answer": answer, "Text": text}
                if context_field:
                    json_record["Context"] = context

                file.write(json.dumps(json_record) + "\n")

    elif file_format == "csv":
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            headers = ["Context", "Question", "Answer", "Text"]
            if not context_field:
                headers.remove("Context")
            writer.writerow(headers)

            for question, answer in qa_pairs:
                text = format_text(question, answer, formula, context)
                row = [context, question, answer, text]
                if not context_field:
                    row.pop(0)
                writer.writerow(row)
