from dotenv import load_dotenv

load_dotenv()

# Import things that are needed generically
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

# Load the tool configs that are needed.
from langchain import LLMMathChain, SerpAPIWrapper

llm = OpenAI(temperature=0)
# search = SerpAPIWrapper() # to use this you need an API key
llm_math_chain = LLMMathChain(llm=llm, verbose=True)

tools = [
    # Tool(
    #     name = "Search",
    #     func=search.run,
    #     description="useful for when you need to answer questions about current events"
    # ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    )
]

# Construct the agent. We will use the default agent type here.
# See documentation for a full list of options.
llm = OpenAI(temperature=0)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
# agent.run("How old is Olivia Wilde's boyfriend? What is that number raised to the 0.23 power?")
agent.run("What is 1238 raised to the 0.23 power?")
