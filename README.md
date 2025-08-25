# 💱 AI Currency Converter

**AI-powered currency converter built with LangChain and GPT-4o-mini.**  
It can handle natural language queries, fetch real-time exchange rates, and perform multi-step currency conversions with clear, user-friendly responses.

---

## ⚡ Features
- Convert currencies using natural language, e.g., “Convert 10 USD to INR”
- Fetch live exchange rates via **ExchangeRate API**
- Compute conversion factor and final conversion
- Built using **LangChain tools** and **OpenAI functions agent**

**🔮 Tech Stack**

LangChain – Orchestrates tools and LLM workflow
OpenAI GPT-4o-mini – LLM for query understanding
Python & Requests – API calls for real-time conversion


**▶️ Usage**
currency_conversion.py
**Example query processed by the agent:**
"What is the currency conversion from USD to INR for 10 USD"
**Example output:**
10 USD = 830 INR (Rate: 83)
