# FastAPI GPT Schema Example

## Overview
This project demonstrates a simple FastAPI backend with a Book schema,
integrated easily with a Custom GPT for adding and retrieving books.

## How to Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the API:
   - Home: http://127.0.0.1:8000
   - Docs: http://127.0.0.1:8000/docs

## Deployment on Render

- Connect your GitHub repository to Render.
- Use the following start command:
  ```bash
  uvicorn main:app --host 0.0.0.0 --port 10000
  ```

## GPT Integration Schema

```json
{
  "type": "object",
  "properties": {
    "title": {"type": "string"},
    "author": {"type": "string"}
  },
  "required": ["title", "author"]
}
```