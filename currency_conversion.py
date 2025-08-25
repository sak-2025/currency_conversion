import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate


load_dotenv()


# gloabl Declaration

base_currency: str = "USD"
target_currency: str = "INR"
amount: int = 100



#step 1 : tool creation
@tool
def get_conversion_factor_full(base_currency :str , target_currency: str , amount :int) ->str:
    '''This function will fetch the base currency and convert it into target currency'''
    url=f'https://v6.exchangerate-api.com/v6/accc8b555d22f428f12c53ab/pair/{base_currency}/{target_currency}'    
    response = requests.get(url)
    print("Status Code:", response.status_code)
    data=response.json()
    if response.status_code== 200:
        try:
            rate =data.get('conversion_rate')
            if rate:
                converted_amount = round(rate * amount ,2)
                return f'{amount} {base_currency} = {converted_amount} {target_currency} / (Rate : {rate})'
               # return f'{amount} {base_currency} = {converted_amount} {target_currency} (Rate: {rate})'

            else:
                print('Conversion rate not found')
        except Exception  as e:
            return f' Error JSON {e}'
        
    return f' Api call failed with status code {response.status_code}'


@tool
def get_conversion_factor(base_currency :str , target_currency: str) ->float:
    '''This function will fetch the base currency and convert it into target currency'''
    url=f'https://v6.exchangerate-api.com/v6/accc8b555d22f428f12c53ab/pair/{base_currency}/{target_currency}'    
    response = requests.get(url)
    print("Status Code:", response.status_code)
    data=response.json()
    if response.status_code== 200:
            rate =data.get('conversion_rate')  
    return rate



@tool
def currency_conv(base_currency_value :int , converion_factor : float)-> float:
    ''' Multiply the value of base currency with the conversion factor'''
    return base_currency_value * converion_factor

## printing

result = get_conversion_factor.invoke({'base_currency':'USD','target_currency':'INR'})
print (result)

#print(currency_conv.invoke({'base_currency_value':10,'converion_factor':50}))



def create_currency_agent() ->AgentExecutor :

   llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
   tools = [get_conversion_factor,currency_conv]

   prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful currency conversion assistant."),
        ("user", "{input}"),
        ("ai", "{agent_scratchpad}")
    ])
   
   agent = create_openai_functions_agent(llm,
                                         tools,
                                         prompt)
   return AgentExecutor(agent=agent,tools=tools , verbose =True)


def main():

    agent_executor =create_currency_agent()
    query = " What is the currency conversion from USD to INR for 10 USD"
    result = agent_executor.invoke({"input":query}) 



if __name__ == "__main__":
    main()