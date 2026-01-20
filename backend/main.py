from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(title="FastAPI Backend", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "FastAPI Backend is running"}


@app.get("/greet")
async def greet_no_user():
    """
    Greet endpoint without a user name.
    
    Returns:
        A greeting message without a user name
    """
    return {"message": "Hello! Welcome to the FastAPI backend!"}


@app.get("/greet/{user}")
async def greet(user: str):
    """
    Greet endpoint that welcomes a user.
    
    Args:
        user: User name (path parameter)
    
    Returns:
        A greeting message with the user's name
    """
    return {"message": f"Hello! Welcome to the FastAPI backend, {user}!"}


@app.get("/fetch_weather_today")
async def fetch_weather_today():
    """
    Fetch today's weather (mock data).
    
    Returns:
        Mock weather data with current date in m/d/y format
    """
    now = datetime.now()
    # Format date as m/d/y (removing leading zeros)
    current_date = f"{now.month}/{now.day}/{now.year}"
    
    return {
        "location": "San Francisco, CA",
        "temperature": 72,
        "condition": "Sunny",
        "date": current_date
    }


@app.get("/health")
async def health():
    """
    Health check endpoint for Cloud Run.
    
    Returns:
        Health status of the application
    """
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
