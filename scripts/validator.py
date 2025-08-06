import subprocess

# running an LLM with text prompt as input and the model which is mistral in this case
def query_ollama(prompt, model="mistral"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    # returns the LLM output
    return result.stdout.decode()

# Checking if invoice field matches the relevant contract clauses
def validate_field(field_name, field_value, context_chunk):
    prompt = f"""
    Based on the following contract clause:

    \"\"\"{context_chunk}\"\"\"

    Does the following contract text match the invoice {field_name}: "{field_value}"?
    Provide a Yes or No, followed by a detailed explanation that references all relevant clauses in the context, including any related terms, conditions, or exceptions that might influence the match.
    """
    # It returns the LLM/s yes/no decision and it's explanation
    return query_ollama(prompt)
