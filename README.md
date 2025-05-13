# 💸 Currency Converter Web App (Flask + Render Deployment)

A simple currency converter web application built using **Python Flask**. This app converts between four currencies using fixed exchange rates. It is deployed on **Render**, a free cloud platform for hosting web apps.

---

## 📌 Features

- Converts currencies between:
  - USD (US Dollar)
  - EUR (Euro)
  - INR (Indian Rupee)
  - JPY (Japanese Yen)
- Simple, clean web interface (HTML + Flask templates)
- Stateless conversion using static rates
- Hosted on the cloud using Render

---

## 🧰 Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML (Jinja2 templating)
- **Cloud Hosting**: Render
- **Version Control**: Git & GitHub

---

## 🚀 Live Demo

👉 [Visit the App on Render](https://your-app-name.onrender.com) *(replace with your URL)*

---

## 🖥️ Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/currency-converter.git
cd currency-converter
2. Create a Virtual Environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the App
bash
Copy
Edit
python app.py
Visit: http://127.0.0.1:5000 in your browser

☁️ Deploying to Render (Cloud Hosting)
1. Push Your Code to GitHub
Make sure all files are committed and pushed to a GitHub repository.

2. Create Web Service on Render
Go to https://render.com

Click "New Web Service"

Connect your GitHub repository

Use the following settings:

Setting	Value
Environment	Python
Build Command	pip install -r requirements.txt
Start Command	python app.py
Port	Use os.environ.get("PORT", 5000) in app.py

Render will build and deploy your Flask app and give you a public URL.

🧪 Example Screenshot
(Add a screenshot if you have one)

📈 Pros and Cons
✅ Pros
✅ Very simple code structure — great for beginners

✅ Quick to deploy using free tier of Render

✅ No database or backend complexity

✅ Easy to customize or expand (e.g., more currencies)

❌ Cons
❌ Uses static currency rates (not real-time)

❌ No input validation or styling (basic UI)

❌ Not suitable for production without enhancements (e.g., HTTPS, WSGI server)

❌ No mobile responsiveness

📦 Future Improvements
✅ Use a live exchange rate API (like exchangerate-api.com or fixer.io)

✅ Add Bootstrap or TailwindCSS for styling

✅ Include more currencies

✅ Add input validation and error messages

✅ Deploy using a production WSGI server like Gunicorn
