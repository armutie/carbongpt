from fastapi import FastAPI
from groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
app = FastAPI()
groq_client = Groq()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Hello, this is CarbonGPT!"}

@app.post("/query")
def process_query(request: QueryRequest):
    query_lower = request.query.lower()
    try:
        relevance_check = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a classifier. Respond only with 'yes' if the query is about carbon emissions, 'no' if it’s not."},
                {"role": "user", "content": query_lower}
            ],
            max_tokens=5
        )
        relevance = relevance_check.choices[0].message.content.strip().lower()
        if relevance == "yes":
            response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are CarbonGPT, an expert on carbon emissions. Answer only about carbon emissions."},
                    {"role": "user", "content": query_lower}
                ],
                max_tokens=200
            )
            answer = response.choices[0].message.content
            return {"status_code": 200, "response_content": answer}
        else:
            return {"status_code": 400, "response_content": f"Error: '{request.query}' is not related to carbon emissions."}
    except Exception as e:
        return {"status_code": 500, "response_content": f"Error processing query: {str(e)}"}