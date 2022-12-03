from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

## So I added a third chain to the mix, which is one more than the documentation.
## I highly recommend this as an exercise.
## Just remember the outputs will flow from one chain to the next.
## Check input and output variables for each subchain.

llm = OpenAI(temperature=0.9)
# this is just using Python's f-strings to format the prompt
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
    template_format="f-string" # this just to demo what this last argument is, must leave at least a comma
)

# the below fails with TypeError: __init__() takes exactly 1 positional argument (3 given)
# chain = LLMChain(llm, prompt)

sponsor_chain = LLMChain(llm=llm, prompt=prompt, output_key="sponsor")


llm = OpenAI(temperature=.7)
template = """You are a playwright. Given the title of play and the era it is set in, it is your job to write a synopsis for that title.

Title: {title}
Era: {era}
Playwright: This is a synopsis for the above play:"""
prompt_template = PromptTemplate(input_variables=["title", 'era'], template=template)
synopsis_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="synopsis")

## This is an LLMChain to write a review of a play given a synopsis. ##
llm = OpenAI(temperature=.7)
template = """You are a play critic from the New York Times. Given the synopsis of play, it is your job to write a review for that play. You must also praise the corporate sponsor of the play.

Play Synopsis:
{synopsis}
Corporate Sponsor: {sponsor}
Review from a New York Times play critic of the above play:"""
prompt_template = PromptTemplate(input_variables=["synopsis", "sponsor"], template=template)
review_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="review")

# This is the overall chain where we run these three chains in sequence.
from langchain.chains import SequentialChain
overall_chain = SequentialChain(
    chains=[sponsor_chain, synopsis_chain, review_chain], # the order must matter
    input_variables=["era", "title", "product"],
    ## The output always includes the input variables, plus the output variables specified below.
    ## Therefore you can optionally include intermediate output variables in the output.
    output_variables=["review"],
    verbose=True)

review = overall_chain({"title":"Tragedy at sunset on the beach", "era": "Victorian England", "product": "toothpaste"})
print(review)


## You ready for one more? We can of course use a SequentialChain as a subchain in another SequentialChain.

template="""You are a college English teacher, and you also hate all corporate sponsors. You are given a review of a play, written by a New York Times play critic. Your job is to critique the review and its style, and explain positive and negative aspects of the style. Also describe why the reviewer's relationship with the corporate sponsor is problematic.

Play Review:
{review}
"""
last_chain=LLMChain(llm=OpenAI(temperature=.7), prompt=PromptTemplate(input_variables=["review"], template=template), output_key="critique")

critique = last_chain({"review": review})

print(critique)
