1) Profile API (HNG Stage 0 Task)

A simple REST API built with **Django REST Framework** that returns:
- User profile information (name, email, stack)
- Current UTC timestamp
- A random cat fact from an external public API

This project demonstrates how to build and expose a JSON API endpoint using Python and Django REST Framework.

---

2) Live API URL:
 **(Add your deployed link here once hosted, e.g. https://profileapi-production.up.railway.app/api/me/)**



3) GET /api/me/

Example response:
json
{
  "status": "success",
  "user": {
    "email": "example@gmail.com",
    "name": "Jude",
    "stack": ["PYTHON", "DJANGO"]
  },
  "timestamp": "2025-10-18T11:02:51.314811+00:00",
  "facts": "A cat..."
}



4) Features

- Returns JSON data with proper header: Content-Type: application/json

- Shows current UTC timestamp

- Fetches random cat facts from https://catfact.ninja/fact

- Uses Django REST Framework’s clean APIView class



5) Local Setup Instructions

- Clone the repository
git clone https://github.com/jais380/profile.git
cd profile

- Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate    # on Windows
# or
source venv/bin/activate  # on macOS/Linux

- Install dependencies: pip install -r requirements.txt

- Run migrations: python manage.py migrate

- Start the development server: python manage.py runserver


- Then open your browser and visit: http://127.0.0.1:8000/api/me/

You should see the JSON response containing your profile details and a cat fact



6) Install all dependencies using: pip install -r requirements.txt



7) Testing the Endpoint

You can test your endpoint in multiple ways:

- Using your browser

Visit: http://127.0.0.1:8000/api/me/

- Using curl: curl http://127.0.0.1:8000/api/me/

- Using Postman:

. Create a new GET request.

. Set URL to http://127.0.0.1:8000/api/me/.

. Click “Send” to view the JSON response.