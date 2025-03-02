
from dotenv import load_dotenv
load_dotenv()

import aisuite as ai
client = ai.Client()

import time

llms = [
    #"huggingface:meta-llama/Llama-3.1-8B-Instruct",
    "anthropic:claude-3-5-sonnet-20240620",
    "huggingface:meta-llama/Llama-3.2-1B-Instruct",
    #"huggingface:meta-llama/Llama-3.2-3B-Instruct"
]

def compare_llm(messages):
    execution_times = []
    responses = []
    for llm in llms:
        start_time = time.time()
        response = client.chat.completions.create(model=llm, messages = messages)
        end_time = time.time()
        execution_time = end_time - start_time
        responses.append(response.choices[0].message.content.strip())
        execution_times.append(execution_time)
        print(f"{llm} - {execution_time:.2f} seconds: {response.choices[0].message.content.strip()}")
    return responses, execution_times

sys_message ="""
Instruction: Answer the following questions based on the examples.

Examples:

Question: Who is the first president of the United States?
Answer: George Washington.
Question: Who wrote the play "Romeo and Juliet"?
Answer: William Shakespeare.
Question: What is the capital of France?
Answer: Paris.
"""

inputs = [
    "What is the chemical symbol for water?",
    "Who painted the Mona Lisa?",
    "What is the smallest country in the world?",
    "Who discovered penicillin?",
    "What is the tallest mountain in the world?"
]

messages = [
    {"role": "system", "content": sys_message},
    {"role": "user", "content": inputs}
]

responses, execution_times = compare_llm(messages)

import pandas as pd


def display(llms, execution_times, responses):
    data = {
        'Provider:Model Name': llms,
        'Execution Time': execution_times,
        'Model Response ': responses
    }

    df = pd.DataFrame(data)
    df.index = df.index + 1
    styled_df = df.style.set_table_styles(
        [{'selector': 'th', 'props': [('text-align', 'center')]},
         {'selector': 'td', 'props': [('text-align', 'center')]}]
    ).set_properties(**{'text-align': 'center'})

    return styled_df

display(llms, execution_times, responses)
