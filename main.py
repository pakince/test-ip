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

@app.get("/getip")
async def get_ip(request: Request):
    # Get the IP address of the client that is making the request.
    client_ip = request.client.host

    # Get the IP address of the destination server.
    destination_ip = request.headers.get("X-Forwarded-For", client_ip)

    # Return the client and destination IP addresses.
    return {"client_ip": client_ip, "destination_ip": destination_ip}
