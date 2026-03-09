# Edmingle_Webhook-ELA
This project receives webhook events from Edmingle and stores them in PostgreSQL.

## Features
- Receives Edmingle webhook events
- Stores raw JSON payload
- Supports events like:
  - User Created
  - Transaction Completed

## Tech Stack
Python  
Flask  
PostgreSQL  
Ngrok (for testing)

## Setup
1 Install dependencies
pip install -r requirements.txt

2 Create database
psql -U postgres -d webhook_test -f database/schema.sql

3 Run server
python app.py

Webhook endpoint:
http://localhost:5000/edmingle/webhook

## Testing with Ngrok
ngrok http 5000

## Edmingle webhook 
 - Paste the generated URL into the Edmingle webhook dashboard
 - Validate the URL
 - Select the relevant events
 - create the webhook 
