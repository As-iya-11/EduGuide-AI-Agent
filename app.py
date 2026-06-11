import gradio as gr

def eduguide(question):
    question_lower = question.lower()
    
    if "python" in question_lower:
        return """## 🐍 Learning Python

**Start here:**
1. Install Python from python.org
2. Learn variables, loops, functions
3. Practice daily!

**Free Resources:**
- freeCodeCamp Python (YouTube)
- Python.org official tutorial
- W3Schools Python"""

    elif "machine learning" in question_lower or "ml" in question_lower:
        return """## 🤖 Learning Machine Learning

**Start here:**
1. Learn Python first
2. Learn NumPy and Pandas
3. Start with Scikit-learn

**Free Resources:**
- Kaggle Learn (Free)
- Andrew Ng Coursera Course
- Google ML Crash Course"""

    elif "ai" in question_lower or "artificial intelligence" in question_lower:
        return """## 🧠 Learning AI

**Start here:**
1. Python + Math basics
2. Machine Learning fundamentals
3. Deep Learning with TensorFlow

**Free Resources:**
- Microsoft AI Skills Navigator
- Fast.ai (Free)
- DeepLearning.AI"""

    elif "data science" in question_lower:
        return """## 📊 Learning Data Science

**Start here:**
1. Python + Statistics
2. Pandas + Matplotlib
3. SQL basics

**Free Resources:**
- Kaggle (Free)
- DataCamp free tier
- Towards Data Science blog"""

    elif "java" in question_lower:
        return """## ☕ Learning Java

**Start here:**
1. Install JDK from oracle.com
2. Learn OOP concepts
3. Practice on HackerRank

**Free Resources:**
- MOOC.fi Java Programming
- Codecademy Java
- W3Schools Java"""

    else:
        return f"""## 📚 EduGuide Response for: {question}

**Your Learning Path:**
1. Search YouTube for beginner tutorials
2. Find free courses on Coursera/edX
3. Practice with hands-on projects
4. Join communities on Reddit/Discord

**Free Resources:**
- YouTube tutorials
- Coursera (audit free)
- GitHub projects
- Stack Overflow

Keep learning! You've got this! 🌟"""

demo = gr.Interface(
    fn=eduguide,
    inputs=gr.Textbox(
        placeholder="Ask me anything! e.g. How to learn Python?",
        label="Your Learning Question",
        lines=3
    ),
    outputs=gr.Markdown(label="EduGuide Response"),
    title="🎓 EduGuide AI Agent",
    description="### Your Personal AI-Powered Learning Assistant!\nAsk any question and get instant guidance with curated free resources.",
    examples=[
        ["How do I learn Python?"],
        ["How to get started with Machine Learning?"],
        ["What is Artificial Intelligence?"],
        ["How to learn Data Science?"],
        ["How to learn Java?"]
    ],
    theme="soft"
)

demo.launch()
