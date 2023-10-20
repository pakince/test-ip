from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware  # Import the CORSMiddleware

app = FastAPI()

# Define CORS settings
origins = ["*"]  # This allows access from all domains; "*" should be used with caution in a production environment.

# Add the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific HTTP methods if needed
    allow_headers=["*"],  # You can specify specific headers if needed
)
import socket

def get_azure_app_service_ip():
  """Returns the IP address of the Azure App Service instance."""
  hostname = socket.gethostname()
  app_service_ip = socket.gethostbyname(hostname)
  return hostname,app_service_ip

import os

def get_inbound_ip_address():
  """Gets the inbound IP address of the current machine.

  Returns:
    A string containing the inbound IP address, or `None` if the inbound IP address cannot be determined.
  """

  try:
    return os.environ['WEBSITE_EXTERNAL_IP']
  except KeyError:
    return None

@app.get("/getip")
async def get_ip(request: Request):
  # Get the IP address of the client that is making the request.
  client_ip = request.client.host

  # Get the IP address of the destination server.
  destination_ip = request.headers.get("X-Forwarded-For", client_ip)

  # Get the IP address of the Azure App Service instance.
  hostname,app_service_ip = get_azure_app_service_ip()

  inbound_ip = get_inbound_ip_address()
  # Return the client, destination, and Azure App Service IP addresses.
  return {"client_ip": client_ip, "destination_ip": destination_ip, "app_service_ip": app_service_ip,"hostname":hostname,"inbound_ip":inbound_ip}
