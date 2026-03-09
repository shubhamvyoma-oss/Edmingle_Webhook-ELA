from flask import Flask, request, jsonify
from datetime import datetime
import json
import psycopg2

# Create a Flask application
app = Flask(__name__)

# Connect to PostgreSQL database using psycopg2
conn = psycopg2.connect(
    dbname="webhook_test",      # Name of the database
    user="postgres",            # Database username
    password="Svyoma",          # Database password
    host="localhost",           # Database host
    port="5432"                 # Default PostgreSQL port
)

# ---Webhook Endpoint---

# This endpoint will receive POST requests from Edmingle
@app.route("/edmingle/webhook", methods=["POST"])
def edmingle_webhook():
    received_at = datetime.now()  # Capture the exact time the webhook is received

    print(f"WEBHOOK RECEIVED at: {received_at}")  # Print log in terminal


    payload = request.get_json(force=True) # Parse incoming JSON payload from the request

    # Print formatted JSON for debugging/logging
    print("\nParsed JSON:")
    print(json.dumps(payload, indent=2, ensure_ascii=False))

    # Create a database cursor to execute SQL commands
    cursor = conn.cursor()

    # Insert webhook data into the database
    cursor.execute(
        """
        INSERT INTO webhook_events (source, received_at, raw_payload)
        VALUES (%s, %s, %s)
        """,
        (
            "edmingle",              # Source of webhook
            received_at,             # Timestamp when received
            json.dumps(payload)      # Store entire JSON payload as text
        )
    )

    conn.commit()  # Commit transaction so data is saved

    cursor.close()  # Close the cursor after query execution
 
    print("Stored in PostgreSQL")

    # Send a response back confirming webhook was received and stored
    return jsonify({
        "status": "stored",
        "timestamp": received_at.strftime("%Y-%m-%d %H:%M:%S")
    }), 200

# Run Flask Server
if __name__ == "__main__":
    app.run(port=5000, debug=True)