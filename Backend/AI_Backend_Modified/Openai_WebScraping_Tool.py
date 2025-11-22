from crewai_tools import ScrapeWebsiteTool
from agents import function_tool

#===============================
# Local scrape_tool test starts
#===============================

async def scrape_tool_test(search_url:str):
    tool =ScrapeWebsiteTool(website_url=search_url)
    text=tool.run()
    return text

#===============================
# Local scrape_tool test ends
#===============================
@function_tool
async def scrape_tool(search_url:str):
    tool =ScrapeWebsiteTool(website_url=search_url)
    text=tool.run()
    return text

if __name__=='__main__':
    import asyncio
    text=asyncio.run(scrape_tool_test(search_url='https://www.parentune.com'))
    print(text)
    
    


