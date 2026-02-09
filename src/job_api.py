from dotenv import load_dotenv
from apify_client import ApifyClient
import os

load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_KEY"))

#Fetch linkdin jobs based on search query and location
def fetch_linkdin_jobs(search_query,location="sri lanka",rows=60):
  run_input ={
    "search_term": search_query,
    "location":location,
    "rows": rows,
    "proxy":{
      "useApifyProxy":True,
      "apifyProxyGroups":["RESIDENTIAL"]
    }
  }
  run = apify_client.actor("qLWmLIaUhhLldluI9").call(run_input=run_input)
  jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
  return jobs

#Fetch indeed jobs based on search query and location
def fetch_indeed_jobs(search_query, location="sri lanka", rows=60):
  run_input = {
      "search_term": search_query,   
      "location": location,          
      "max_jobs": rows,              
      "sort": "relevance",
      "date_posted": "all"
    }

  run = apify_client.actor("MXLpngmVpE8WTESQr").call(run_input=run_input)
  jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
  return jobs

  

