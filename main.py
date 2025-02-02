from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from ollama import chat

app = FastAPI()

class Validation(BaseModel):
    query: str

@app.post("/deepseek-r1")
async def getquestion(payload: Validation):
    system_prompt = (
        "You are an expert Python coder. You will receive a business use case from the user "
        "and generate Python code for it. Use FastAPI as the API framework. "
        "Mandatorily use try and except blocks for all functions. "
        "Follow this File structure:\n"
        "- app.py: Handles API requests and passes them to the controller.\n"
        "- controller.py: Validates input and forwards it to the service.\n"
        "- services.py: Implements business logic.\n"
        "- repository.py: Handles database operations.\n"
        "Your output structure should look like this app.py: #generatedcode, controller.py: #generatedcode, services.py: #generatedcode, repository.py: #generatedcode"
    )
    
    user_query = payload.query
    response = chat(
        model="deepseek-r1:1.5b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query},
        ]
    )

    # Extract only the code part from the response
    answer = response.message.content
    return {"answer": answer}

if __name__ == "__main__":
    uvicorn.run(app, port=8080)
