from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Define a simple data source (e.g., from a database or API)
def get_user_data():
    return {
        "user_name": "Alice",
        "items": [
            {"name": "Laptop", "price": 999.99},
            {"name": "Mouse", "price": 25.50},
            {"name": "Keyboard", "price": 75.00}
        ]
    }

@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    user_data = get_user_data()
    # Pass the data in a dictionary to the 'context' argument
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context=user_data
    )