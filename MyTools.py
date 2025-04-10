from crewai_tools import WebsiteSearchTool

# Example of limiting the search to the content of a specific website, 
# so now agents can only search within that website
md_tool = WebsiteSearchTool(website='https://medium.com/')