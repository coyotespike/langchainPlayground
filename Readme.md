## Overview

From a zoomed-out view, an LLM is like a bash tool: it takes in text, and outputs text. (yes I know bash takes in streams while an LLM takes in a string literal but ignore that for now)

This enables prompt chaining, where the output from one LLM iteration serves as input to the next.

The [ LangChain project ](https://github.com/hwchase17/langchain) uses Python OOP to make it easy to prompt chain LLMs.

This repo is just me running through the LangChain project using the excellent docs, and making notes on how it works.

## The Future

Because LangChain presciently abstracts over LLMs and the tools they use, you could imagine hooking up an LLM as the brain driving an unlimited number of sub-LLMs. Some LLMs take text and output images. To complete the loop you need another LLM to take the output images and return text.

Similarly, we can also direct the LLM to output text suitable to be run as commands, and use the command output as a prompt chain. LangChain makes this easy too.

Text-image-text, text-code-text, text-music-text, and of course text-action-text as long as the action outputs text (for example a google search outputs HTML).

Data cleaning can be a problem, but maybe we can use a LLM to clean the data. For instance, I have had success asking GPT to find the search input given an HTML dump. This would make creating a crawler easier.

At some point we may even need to think along Kafka lines. The LLMs are like Kafka topics, and the prompt chain is like a Kafka stream. Kafka was invented because multiple data sources required a common data format to simplify API communication at scale (internally).

## Usage

Be sure to put install OpenAI

pip install langchain
pip install openai

Or get errythang with pip install langchain[all]

pip install python-dotenv # this is for loading the API key from a .env file
pip install google-search-results  # this is for the SerpApi search engine for the math example

Also be sure to set your OpenAI API key as an environment variable, by renaming the .env.example file to .env and filling in your key.
