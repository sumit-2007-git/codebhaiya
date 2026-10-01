---
title: CodeBhaiya - Vernacular AI & ML Mentor
emoji: 🚀
colorFrom: indigo
colorTo: blue
sdk: docker
app_port: 7860
pinned: false
license: mit
---

# CodeBhaiya - Vernacular AI & Machine Learning Mentor 🚀
> **Empowering Tier-2 & Tier-3 Engineering Students with Explainable ML & 24/7 Personalized Mentorship**  
> *Developed by Sumit Kumar for the AICTE | IBM SkillsBuild Applied AI & ML Internship Program 2026*  
> *In Collaboration with Bharat Cares (by SMEC Trust) & IBM*  
> *Aligned with UN Sustainable Development Goal 4 (Quality Education)*

---

### 🌐 Live Production Demo
- **Live Web Application:** [https://codebhaiya.onrender.com](https://codebhaiya.onrender.com)
- **Status:** 🟢 Operational (FastAPI + PyTorch + Scikit-Learn Engines)

---

## 🌟 Overview & Key Features

1. **Scikit-Learn Placement Probability & CTC Predictor:**
   - Multi-output ML pipeline using **Random Forest Classifier** and **Gradient Boosting Regressor**.
   - Explainable AI (XAI) feature importance breakdown (DSA, CGPA, Backlogs, Internships).
2. **Live PyTorch Neural Network Playground:**
   - Real `torch.nn` training loop running directly in the backend.
   - Interactive Epoch Loss convergence graph (e.g., 0.71 -> 0.27) and tensor weight inspection.
3. **Vernacular AI Code Debugger & Python AST Tree Analyzer:**
   - Evaluates code complexity (Cyclomatic Complexity M-Score) using Python's native `ast` library.
   - Explains syntax & runtime bugs in friendly, stress-free Hinglish with daily-life analogies.
   - Live sandboxed execution environment.
4. **NLP Technical Interview Scorer:**
   - Evaluates interview responses using **TF-IDF Vectorization** and **Cosine Similarity** against FAANG benchmarks.
   - Highlights matched technical keywords and flags missing core concepts.

---

## 💻 Local Setup & Running

```bash
# 1. Clone or navigate to the repository
cd codebhaiya

# 2. (Optional) Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the live server
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```
Open **`http://127.0.0.1:8000`** in your browser!

---

## 🚀 How To Deploy (Step-by-Step)

### Option 1: Deploy on Render.com (Recommended - Free Web Service)
1. Push this project to your GitHub account:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of CodeBhaiya AI platform"
   git branch -M main
   git remote add origin https://github.com/<YOUR_USERNAME>/codebhaiya.git
   git push -u origin main
   ```
2. Go to [https://dashboard.render.com](https://dashboard.render.com) and click **"New +" -> "Web Service"**.
3. Connect your GitHub repository `codebhaiya`.
4. Configure the settings:
   - **Name:** `codebhaiya-ai-mentor`
   - **Environment:** `Python 3`
   - **Region:** Singapore or Frankfurt
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Plan:** `Free`
5. Click **"Deploy Web Service"**.
6. Within 2-3 minutes, your live URL will be active:  
   `https://codebhaiya-ai-mentor.onrender.com`

---

### Option 2: Deploy on Hugging Face Spaces (100% Free • 16 GB RAM • Built for AI/ML)
Hugging Face Spaces provides **16 GB RAM** and **2 vCPU** for free, making it ideal for PyTorch and Scikit-Learn:
1. Go to [https://huggingface.co/spaces](https://huggingface.co/spaces) and click **"Create new Space"**.
2. Set:
   - **Space name:** `codebhaiya-ai-mentor`
   - **License:** `MIT`
   - **Space SDK:** `Docker` (Blank)
   - **Space hardware:** `CPU Basic (2 vCPU, 16GB RAM) - Free`
3. Push your repository to Hugging Face:
   ```bash
   git remote add space https://huggingface.co/spaces/<YOUR_HF_USERNAME>/codebhaiya-ai-mentor
   git push --force space main
   ```
4. Hugging Face will automatically detect the `Dockerfile` and launch your live application with a public URL!

---

### Option 3: Deploy on Railway.app
1. Go to [https://railway.app](https://railway.app) and sign in with GitHub.
2. Click **"New Project" -> "Deploy from GitHub repo"**.
3. Select `codebhaiya`.
4. Railway will automatically detect the `Procfile` and deploy it instantly.
5. In project settings, click **"Generate Domain"** to get your public URL.

---

### Option 4: Deploy with Docker on Any Cloud VPS (AWS EC2 / DigitalOcean)
```bash
# Build the Docker image
docker build -t codebhaiya:latest .

# Run the container
docker run -d -p 8000:8000 --name codebhaiya-app codebhaiya:latest
```
Access via `http://<YOUR_SERVER_IP>:8000`.

---

## 📂 Project Architecture

```
codebhaiya/
├── app.py                 # FastAPI backend & REST endpoints
├── ml_models.py           # Scikit-Learn, PyTorch, AST & TF-IDF models
├── static/
│   ├── index.html         # Responsive Tailwind & Lucide UI
│   └── Lean_Canvas_Final_Fixed.pdf # Verified Lean Canvas
├── Dockerfile             # Production container definition
├── render.yaml            # Render Blueprint configuration
├── Procfile               # Heroku / Railway / Render process file
├── runtime.txt            # Python version specification
├── requirements.txt       # Production dependencies (Lightweight CPU torch)
├── verify_project.py      # Automated 7-point health check suite
└── README.md              # Project documentation
```

---

## 📜 Credits & Acknowledgments
- **Lead Developer:** Sumit Kumar
- **Internship Program:** AICTE | IBM SkillsBuild Applied AI & ML Internship Program 2026
- **Partner Organizations:** Bharat Cares (by SMEC Trust) & IBM
