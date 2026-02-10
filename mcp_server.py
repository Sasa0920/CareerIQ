from mcp.server.fastmcp import FastMCP
from src.job_api import fetch_linkdin_jobs, fetch_indeed_jobs

mcp = FastMCP("Job Recommender MCP")

@mcp.tool()
async def recommend_linkdin_jobs(listofkeys):
  return fetch_linkdin_jobs(listofkeys)

@mcp.tool()
async def recommend_indeed_jobs(listofkeys):
  return fetch_indeed_jobs(listofkeys)

if __name__ == "__main__":
    mcp.run(transport='stdio')