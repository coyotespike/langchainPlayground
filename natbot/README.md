## Natbot Overview

Conceptually, this project is simple.

### Prompt Engineering.

It gives OpenAI a thorough prompt template which describes the commands it can issue, and how the HTML it will be given has been modified, and (importantly) what to do. This is in `constants.py`.

### Crawling
It builds a crawler which processes Google search results and can carry out simple navigation instructions. This is in `crawler.py`

### Combining the Two

- And then it loops
-- `browser_content from crawler.crawl()`
-- `get_gpt_command(browser_content)`
-- `run_cmd`, which gives back a new context for the first command, `crawler.crawl`

Maybe I will clean up this quick demo so everything is even tidier.

## Limitations:
- The crawler can only process Google search pages
- The agent never finishes searching. Ideally it would present a summary or something

## Improvements
- The crawler can ask GPT-3 to find the navigational elements on the page, like a search input.
- Use the crawler with LangChain to form an agent.
- Optionally, use SerpAPI or similar to parse results

## Credit
Clearly this is cloned from the great Nat Friedman, https://github.com/nat/natbot
