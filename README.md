# FAQ Assistant Backend (Django REST Framework)




## Setup Instructions
1. Create virtual environment
2. Install dependencies
pip install -r requirements.txt
3. Run SQL script db_schema.sql
4. python manage.py runserver



## API Endpoints
POST /api/faqs/
GET /api/faqs/
GET /api/faqs/{id}/nPOST /api/ai/suggest-answer/




## Sample AI Request
{
"question": "How to reset password?"
}




## Sample AI Response
{
"draft_answer": "This is an AI-generated draft answer"
}