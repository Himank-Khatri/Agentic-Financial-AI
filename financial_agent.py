import os
import openai
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

## Web search agent
web_search_agent = Agent(
    name='Web Search Agent', 
    role='Search teh web for information',
    model=Groq(id='llama-3.1-70b-versatile'),
    tools=[DuckDuckGo()],
    instructions=['Always include sources'],
    show_tool_calls=True,
    markdown=True
)

## Financial agent
financial_agent = Agent(
    name='Financial Agent',
    role='Process financial agent',
    model=Groq(id='llama-3.1-70b-versatile'),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_info=True, technical_indicators=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    markdown=True
)

multi_ai_agent = Agent(
    team=[web_search_agent, financial_agent],
    instructions=['Always include sources', "Format your response using markdown and use tables to display data where possible."],
    show_tool_calls=True,
    markdown=True
)

web_search_agent.print_response("Summarize analyst recommendation and share the latest news for NIFTY50")


