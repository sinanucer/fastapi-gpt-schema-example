# FastAPI GPT Schema Fix

This project fixes the OpenAPI `servers` issue for FastAPI deployed on Render.

## Features
- Custom OpenAPI schema with correct public URL.
- Book API with GET and POST methods.

## Deployment
1. Upload this project to GitHub.
2. Connect the repo to Render.
3. Use the start command:
   uvicorn main:app --host 0.0.0.0 --port 10000
4. Redeploy and check /openapi.json to ensure the correct `servers` URL is set.