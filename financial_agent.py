from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

## Web search agent
web_search_agent = Agent(
    name='Web Search Agent', 
    role='Search teh web for information',
    model=Groq(id='llama3-groq-70b-8192-tool-use-preview',),
    tools=[DuckDuckGo],
    instructions=['Always include sources'],
    show_tool_calls=True,
    markdown=True
)

## Financial agent
financial_agent = Agent(
    name='Financial Agent',
    role='Process financial agent',
    model=Groq(id='llama3-groq-70b-8192-tool-use-preview',),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_info=True, technical_indicators=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    markdown=True
)