from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)

# this is just using Python's f-strings to format the prompt
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
    template_format="f-string"
)

# the below fails with TypeError: __init__() takes exactly 1 positional argument (3 given)
# chain = LLMChain(llm, prompt)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run("colorful socks"))
