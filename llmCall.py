import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI
llm = OpenAI(temperature=0.9)
text = "What would be a good company name a company that makes colorful socks?"
print(llm(text))

# This model is very simple because it just calls the OpenAI API with optional parameters already set.
# https://github.com/hwchase17/langchain/blob/master/langchain/llms/openai.py
# model_name, temperature, max_tokens, top_p, frequency_penalty, best_of, etc.
# model_kwargs if they add more parameters, which is a good idea.
# Also openai_api_key to pass in directly.
