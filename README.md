## How to run locally (with Docker Compose)

1. Save all your CSVs to `backend/data/`.
2. Build and start services:

docker-compose up --build

3. Access the chatbot UI at [http://localhost:3000](http://localhost:3000)

## Developer setup

- Frontend:  
cd frontend
npm install
npm start

(Runs on :3000; proxy settings might need adjusting if backend is elsewhere.)

- Backend:  
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


## Example Questions to Try

- What are the top 5 most sold products?
- What is the status of order id 12345?
- How many classic tshirts left in stock?

