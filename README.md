# CarbonGPT

CarbonGPT is an API-driven system that answers queries about carbon emissions using a fast language model. It verifies if a query pertains to carbon emissions and responds with relevant information or an error if off-topic.

## Functionality

- Purpose: Answers questions related to carbon emissions (e.g., "How much CO2 does a plane emit?").
- Relevance Check: Uses Groq's LLM to determine if a query is carbon-related.
- Responses:
  - If relevant: Returns a detailed answer.
  - If unrelated: Returns an error message.
- Output: JSON with `status_code` (200, 400, or 500) and `response_content`.

## Tech Stack

- Backend Framework: FastAPI
- LLM Inference: Groq Inference Engine (using `llama-3.3-70b-versatile`)
- API Documentation: Swagger/OpenAPI (built-in with FastAPI, see `/docs`)

## Setup Instructions

### Prerequisites

- Python 3.10+
- A Groq API key (sign up at [groq.com](https://groq.com))

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/armutie/carbongpt.git
   cd carbongpt
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn groq python-dotenv
   ```
3. Create a `.env` file in the project root and paste your Groq API key there:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   ```

### Running the API

1. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
2. Access it at `http://127.0.0.1:8000`:
   - Root: `http://127.0.0.1:8000/` (returns a welcome message).
   - API Docs: `http://127.0.0.1:8000/docs` (interactive Swagger UI).

### Configuration

- API Key: Set via `.env` file (see above).
- Model: Uses `llama-3.3-70b-versatile` (editable in `main.py`).
- Max Tokens: Responses capped at 200 tokens (adjustable in `main.py`).

## API Details

### Endpoint: `/query`

- Method: POST
- Request Body: URL parameter with a `query` field (string).
- Example Request:
   {"query": "How much CO2 does a car emit?"}

- Responses:
  - Success (200):
    ```json
    {
      "status_code": 200,
      "response_content": "A typical car emits about 4.6 metric tons of CO2 per year."
    }
    ```
  - Unrelated Query (400):
    ```json
    {
      "status_code": 400,
      "response_content": "Error: 'What’s the best pizza?' is not related to carbon emissions."
    }
    ```
  - Error (500):
    ```json
    {
      "status_code": 500,
      "response_content": "Error processing query: Invalid API key"
    }
    ```

### Testing

- Use Swagger at `/docs` to try it interactively.
