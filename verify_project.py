import urllib.request
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def run_tests():
    print("==================================================")
    print("🔍 CODEBHAIYA FULL PROJECT VERIFICATION & AUDIT")
    print("==================================================")

    endpoints = [
        {
            "name": "1. Static Frontend UI (GET /)",
            "url": "http://127.0.0.1:8000/",
            "method": "GET",
            "payload": None
        },
        {
            "name": "2. Scikit-Learn Placement & Salary Predictor",
            "url": "http://127.0.0.1:8000/api/ml/predict-placement",
            "method": "POST",
            "payload": {
                "cgpa": 8.5,
                "dsa_solved": 250,
                "projects": 3,
                "internships": 2,
                "backlogs": 0
            }
        },
        {
            "name": "3. Live PyTorch Neural Net Training Loop",
            "url": "http://127.0.0.1:8000/api/ml/train-neural-net",
            "method": "POST",
            "payload": {
                "epochs": 15,
                "learning_rate": 0.05
            }
        },
        {
            "name": "4. Python AST Cyclomatic Complexity Parser",
            "url": "http://127.0.0.1:8000/api/ml/analyze-code-ast",
            "method": "POST",
            "payload": {
                "code": "def find_max(numbers):\n    m = numbers[0]\n    for n in numbers:\n        if n > m:\n            m = n\n    return m"
            }
        },
        {
            "name": "5. Scikit-Learn TF-IDF NLP Interview Evaluator",
            "url": "http://127.0.0.1:8000/api/ml/nlp-interview",
            "method": "POST",
            "payload": {
                "topic": "overfitting",
                "answer": "Overfitting happens when a model fits the training data too closely including noise. We prevent it with L1 L2 regularization, dropout, and cross validation."
            }
        },
        {
            "name": "6. Vernacular AI Hinglish Code Debugger",
            "url": "http://127.0.0.1:8000/api/debug",
            "method": "POST",
            "payload": {
                "code": "students = ['Aman', 'Priya', 'Rahul']\nfor i in range(len(students) + 1):\n    print(students[i])",
                "error_message": "IndexError: list index out of range",
                "language": "python"
            }
        },
        {
            "name": "7. Sandboxed Python Code Runner",
            "url": "http://127.0.0.1:8000/api/run",
            "method": "POST",
            "payload": {
                "code": "print('CodeBhaiya Sandbox: 2 + 2 = ' + str(2 + 2))",
                "language": "python"
            }
        }
    ]

    all_passed = True
    results = []

    for ep in endpoints:
        start_t = time.time()
        try:
            req = urllib.request.Request(ep["url"], method=ep["method"])
            if ep["payload"] is not None:
                req.add_header("Content-Type", "application/json")
                req.data = json.dumps(ep["payload"]).encode("utf-8")

            with urllib.request.urlopen(req, timeout=10) as resp:
                status = resp.status
                latency = round((time.time() - start_t) * 1000, 1)
                data = resp.read().decode("utf-8")
                
                # Validation checks
                if ep["method"] == "GET":
                    assert "CodeBhaiya" in data
                    detail = f"HTML Loaded ({len(data)} bytes)"
                else:
                    parsed = json.loads(data)
                    assert parsed.get("status") == "success" or "output" in parsed
                    detail = json.dumps(parsed)[:110] + "..."

                print(f"✅ PASSED: {ep['name']} | Status: {status} | Latency: {latency}ms")
                print(f"   Response Sample: {detail}\n")
                results.append((ep["name"], "PASSED", latency))
        except Exception as e:
            all_passed = False
            latency = round((time.time() - start_t) * 1000, 1)
            print(f"❌ FAILED: {ep['name']} | Latency: {latency}ms | Error: {str(e)}\n")
            results.append((ep["name"], "FAILED", latency))

    print("==================================================")
    if all_passed:
        print("🎉 ALL 7 CRITICAL COMPONENTS ARE FULLY FUNCTIONAL!")
    else:
        print("⚠️ SOME COMPONENTS FAILED VERIFICATION!")
    print("==================================================")

if __name__ == "__main__":
    run_tests()
