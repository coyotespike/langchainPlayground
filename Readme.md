## Overview

From a zoomed-out view, an LLM is like a bash tool: it takes in text, and outputs text. (yes I know bash takes in streams while an LLM takes in a string literal but ignore that for now)

This enables prompt chaining, where the output from one LLM iteration serves as input to the next.

The LangChain project uses Python OOP to make it easy to prompt chain LLMs.

Similarly, we can also direct the LLM to output text suitable to be run as commands, and use the command output as a prompt chain. LangChain makes this easy too.

This repo is just me running through the LangChain project using the excellent docs, and making notes on how it works.

## Usage

Be sure to put install OpenAI

pip install langchain
pip install openai

Or get errythang with pip install langchain[all]

pip install python-dotenv # this is for loading the API key from a .env file

Also be sure to set your OpenAI API key as an environment variable, by renaming the .env.example file to .env and filling in your key.
