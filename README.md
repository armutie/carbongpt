# CarbonGPT

CarbonGPT is an API-driven system that answers queries about carbon emissions using a fast language model. It verifies if a query pertains to carbon emissions and responds with relevant information or an error if off-topic.

## Functionality

- **Purpose**: Answers questions related to carbon emissions (e.g., "How much CO2 does a plane emit?").
- **Relevance Check**: Uses Groq's LLM to determine if a query is carbon-related.
- **Responses**:
  - If relevant: Returns a detailed answer.
  - If unrelated: Returns an error message.
- **Output**: JSON with `status_code` (200, 400, or 500) and `response_content`.

## Tech Stack

- **Backend Framework**: FastAPI
- **LLM Inference**: Groq Inference Engine (using `llama-3.3-70b-versatile`)
- **API Documentation**: Swagger/OpenAPI (built-in with FastAPI, see `/docs`)

## Setup Instructions

### Prerequisites
- Python 3.10+
- A Groq API key (sign up at [groq.com](https://groq.com))

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/carbongpt.git
   cd carbongpt
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn groq python-dotenv
   ```
   These may be installed already on your device. 
3. Create a .env file where you paste in your Groq API key