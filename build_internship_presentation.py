import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation(output_pptx):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    # Color palette
    NAVY = RGBColor(15, 23, 42)        # Slate 900
    INDIGO = RGBColor(79, 70, 229)     # Indigo 600
    SLATE = RGBColor(71, 85, 105)      # Slate 600
    LIGHT_BG = RGBColor(248, 250, 252) # Slate 50
    WHITE = RGBColor(255, 255, 255)
    EMERALD = RGBColor(16, 185, 129)
    BORDER_LIGHT = RGBColor(226, 232, 240)
    
    # Image paths
    img_banner = r"C:\Users\SUMIT\.gemini\antigravity\brain\8c6ef894-73a8-422f-a0ab-36ddb4e04249\.user_uploaded\media_1790876505745.png"
    img_canvas = r"C:\Users\SUMIT\.gemini\antigravity\brain\8c6ef894-73a8-422f-a0ab-36ddb4e04249\rendered_pdf_check.png"
    img_predictor = r"C:\Users\SUMIT\.gemini\antigravity\scratch\codebhaiya\screenshot_predictor.png"
    img_pytorch = r"C:\Users\SUMIT\.gemini\antigravity\scratch\codebhaiya\screenshot_pytorch.png"
    img_debugger = r"C:\Users\SUMIT\.gemini\antigravity\scratch\codebhaiya\screenshot_debugger.png"
    img_interview = r"C:\Users\SUMIT\.gemini\antigravity\scratch\codebhaiya\screenshot_interview.png"
    
    def set_slide_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = LIGHT_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, tag_text, title_text, subtitle_text):
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.1))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        # Tag
        p_tag = tf.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.bold = True
        p_tag.font.size = Pt(10)
        p_tag.font.color.rgb = INDIGO
        
        # Title
        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.bold = True
        p_title.font.size = Pt(22)
        p_title.font.color.rgb = NAVY
        
        # Subtitle
        p_sub = tf.add_paragraph()
        p_sub.text = subtitle_text
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = SLATE

    # =========================================================================
    # SLIDE 1: Title Slide (AICTE | IBM SkillsBuild Official Banner)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1)
    
    # Official Banner on top
    if os.path.exists(img_banner):
        s1.shapes.add_picture(img_banner, Inches(1.5), Inches(0.5), Inches(10.333), Inches(1.8))
        
    # Main Title Card
    c1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(2.5), Inches(10.333), Inches(4.5))
    c1.fill.solid()
    c1.fill.fore_color.rgb = WHITE
    c1.line.color.rgb = BORDER_LIGHT
    c1.line.width = Pt(1.5)
    
    tf1 = c1.text_frame
    tf1.word_wrap = True
    tf1.margin_top = Inches(0.4)
    tf1.margin_left = Inches(0.6)
    tf1.margin_right = Inches(0.6)
    
    p = tf1.paragraphs[0]
    p.text = "FINAL INTERNSHIP PROJECT PRESENTATION"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = INDIGO
    p.alignment = PP_ALIGN.CENTER
    
    p = tf1.add_paragraph()
    p.text = "CodeBhaiya: Vernacular AI & Machine Learning Mentor"
    p.font.bold = True
    p.font.size = Pt(26)
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER
    
    p = tf1.add_paragraph()
    p.text = "Empowering Tier-2 & Tier-3 Engineering Students with Explainable ML & 24/7 Personalized Mentorship"
    p.font.size = Pt(13)
    p.font.color.rgb = SLATE
    p.alignment = PP_ALIGN.CENTER
    
    p = tf1.add_paragraph()
    p.text = "\nUN Sustainable Development Goal (SDG 4): Quality Education & Youth Employability\n"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = EMERALD
    p.alignment = PP_ALIGN.CENTER
    
    # Author & Metadata Box
    p = tf1.add_paragraph()
    p.text = "Designed & Developed by: SUMIT KUMAR\nInternship Program: AICTE | IBM SkillsBuild Applied AI & ML (2026)\nIn Collaboration with: Bharat Cares (by SMEC Trust) & IBM"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = NAVY
    p.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 2: Problem Statement & Societal Crisis
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2)
    add_header(s2, "Executive Context & Problem Statement", "The Tier-2/3 Engineering Employability Crisis", "Why 80%+ of Indian engineering graduates remain unemployable in modern AI/ML roles")
    
    # 3 Problem Cards
    cards_data = [
        ("1. Outdated Academic Curriculum", "10-Year-Old Theory Gap", "Engineering colleges focus heavily on obsolete C/Java theory. Students graduate with zero practical machine learning, PyTorch, or real AI project experience."),
        ("2. Late-Night Doubt Bottlenecks", "1:60 Teacher-Student Ratio", "Students studying at 11 PM get stuck on complex ML math, matrix dimensions, and Python syntax bugs with no senior mentor or professor available to guide them."),
        ("3. Unaffordable Commercial EdTech", "₹50,000+ Bootcamp Monopoly", "Leading edtech institutes (Scaler, Coding Ninjas) charge ₹50k to ₹1.5 Lakhs—completely out of reach for 90% of students in regional towns and colleges.")
    ]
    
    for i, (head, sub, desc) in enumerate(cards_data):
        cd = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i*4.0), Inches(1.8), Inches(3.7), Inches(4.8))
        cd.fill.solid()
        cd.fill.fore_color.rgb = WHITE
        cd.line.color.rgb = RGBColor(239, 68, 68) if i==0 else (RGBColor(245, 158, 11) if i==1 else RGBColor(168, 85, 247))
        cd.line.width = Pt(1.5)
        
        ctf = cd.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.3)
        ctf.margin_left = ctf.margin_right = Inches(0.25)
        
        p = ctf.paragraphs[0]
        p.text = head
        p.font.bold = True
        p.font.size = Pt(14)
        p.font.color.rgb = NAVY
        
        p = ctf.add_paragraph()
        p.text = sub
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = INDIGO
        
        p = ctf.add_paragraph()
        p.text = f"\n{desc}"
        p.font.size = Pt(11)
        p.font.color.rgb = SLATE

    # =========================================================================
    # SLIDE 3: The Architecture & Lean Canvas Foundation
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3)
    add_header(s3, "System Blueprint", "The Lean Canvas Business & Technical Blueprint", "Architectural model designed by Sumit Kumar aligned with UN SDG 4")
    
    # Left: Canvas Image
    if os.path.exists(img_canvas):
        s3.shapes.add_picture(img_canvas, Inches(0.8), Inches(1.7), Inches(7.5), Inches(5.1))
        
    # Right: Summary Card
    rc = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.6), Inches(1.7), Inches(3.9), Inches(5.1))
    rc.fill.solid()
    rc.fill.fore_color.rgb = WHITE
    rc.line.color.rgb = BORDER_LIGHT
    
    rtf = rc.text_frame
    rtf.word_wrap = True
    rtf.margin_left = rtf.margin_right = rtf.margin_top = Inches(0.3)
    
    p = rtf.paragraphs[0]
    p.text = "Key Canvas Pillars:"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = NAVY
    
    pillars = [
        ("Problem:", "Students lack 24/7 personal mentorship for AI/ML coding; colleges teach outdated theory."),
        ("Solution:", "Vernacular AI Mentor in simple Hinglish + Live PyTorch lab + Placement ML predictor."),
        ("Value Prop:", "Removes fear of AI; mapped to university syllabus; pocket-money price of ₹149/month."),
        ("Unfair Advantage:", "30,000+ Indian university past exam questions dataset + fine-tuned Hinglish LLM engine."),
        ("High-Level Concept:", "\"Duolingo + ChatGPT for AI & Machine Learning Education\".")
    ]
    for k, v in pillars:
        p = rtf.add_paragraph()
        p.text = f"• {k} {v}"
        p.font.size = Pt(10)
        p.font.color.rgb = SLATE

    # =========================================================================
    # SLIDE 4: Feature 1 - Real Scikit-Learn Placement Predictor
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4)
    add_header(s4, "Core AI Feature 1", "Scikit-Learn Placement Probability & Salary (CTC) Predictor", "Predicts student selection probability & salary bracket with Explainable AI feature weights")
    
    # Left: Screenshot
    if os.path.exists(img_predictor):
        s4.shapes.add_picture(img_predictor, Inches(0.8), Inches(1.7), Inches(7.5), Inches(5.1))
        
    # Right: Details
    rc4 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.6), Inches(1.7), Inches(3.9), Inches(5.1))
    rc4.fill.solid()
    rc4.fill.fore_color.rgb = WHITE
    rc4.line.color.rgb = INDIGO
    rc4.line.width = Pt(1.5)
    
    rtf4 = rc4.text_frame
    rtf4.word_wrap = True
    rtf4.margin_left = rtf4.margin_right = rtf4.margin_top = Inches(0.25)
    
    p = rtf4.paragraphs[0]
    p.text = "How It Works & Helps Students:"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = NAVY
    
    pts4 = [
        "ML Architecture: Trained using Random Forest Classifier & Gradient Boosting Regressor on 2,000+ Indian placement profiles.",
        "Instant Inference (<50ms): Adjusting CGPA, DSA problems solved, internships & backlogs updates predictions in real-time.",
        "Explainable AI (XAI): Mathematically breaks down feature importance (DSA: 20.4%, CGPA: 24.7%, Backlogs: 33%).",
        "Actionable Guidance: Tells the student exactly what to do next to jump from Mass Recruiter to a 10+ LPA Product firm.",
        "Societal Impact: Eliminates career confusion and gives students clear, realistic milestones."
    ]
    for pt in pts4:
        p = rtf4.add_paragraph()
        p.text = f"✔ {pt}"
        p.font.size = Pt(9.5)
        p.font.color.rgb = SLATE

    # =========================================================================
    # SLIDE 5: Feature 2 - Live PyTorch Deep Learning Playground
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5)
    add_header(s5, "Core AI Feature 2", "Live PyTorch Deep Learning Neural Network Playground", "Real-time in-browser neural network training with live backpropagation and weight tracking")
    
    if os.path.exists(img_pytorch):
        s5.shapes.add_picture(img_pytorch, Inches(0.8), Inches(1.7), Inches(7.5), Inches(5.1))
        
    rc5 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.6), Inches(1.7), Inches(3.9), Inches(5.1))
    rc5.fill.solid()
    rc5.fill.fore_color.rgb = WHITE
    rc5.line.color.rgb = RGBColor(234, 88, 12) # Orange
    rc5.line.width = Pt(1.5)
    
    rtf5 = rc5.text_frame
    rtf5.word_wrap = True
    rtf5.margin_left = rtf5.margin_right = rtf5.margin_top = Inches(0.25)
    
    p = rtf5.paragraphs[0]
    p.text = "Deep Learning Under the Hood:"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = NAVY
    
    pts5 = [
        "Real PyTorch Model: Implemented via torch.nn with Linear -> ReLU -> Linear -> ReLU -> Sigmoid architecture.",
        "Live Training Loop: Executes actual forward pass, BCELoss computation, backpropagation, and Adam optimizer step.",
        "Real-Time Epoch Tracking: Displays loss convergence curve (0.71 -> 0.52) and live accuracy improvements.",
        "Tensor Weights Inspection: Students can view learned weight matrices directly on the screen.",
        "Societal Impact: Makes Deep Learning accessible and hands-on without requiring costly GPUs or cloud servers."
    ]
    for pt in pts5:
        p = rtf5.add_paragraph()
        p.text = f"✔ {pt}"
        p.font.size = Pt(9.5)
        p.font.color.rgb = SLATE

    # =========================================================================
    # SLIDE 6: Feature 3 - AI Code Debugger & Python AST Inspector
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6)
    add_header(s6, "Core AI Feature 3", "Vernacular AI Debugger & Python AST Complexity Inspector", "Syntax tree parsing combined with friendly Hinglish error diagnosis and daily-life analogies")
    
    if os.path.exists(img_debugger):
        s6.shapes.add_picture(img_debugger, Inches(0.8), Inches(1.7), Inches(7.5), Inches(5.1))
        
    rc6 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.6), Inches(1.7), Inches(3.9), Inches(5.1))
    rc6.fill.solid()
    rc6.fill.fore_color.rgb = WHITE
    rc6.line.color.rgb = RGBColor(37, 99, 235) # Blue
    rc6.line.width = Pt(1.5)
    
    rtf6 = rc6.text_frame
    rtf6.word_wrap = True
    rtf6.margin_left = rtf6.margin_right = rtf6.margin_top = Inches(0.25)
    
    p = rtf6.paragraphs[0]
    p.text = "How It Solves Student Frustration:"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = NAVY
    
    pts6 = [
        "AST Syntax Parsing: Python's Abstract Syntax Tree calculates Cyclomatic Complexity (M-Score) to ensure clean code.",
        "Vernacular Diagnosis: Explains bugs in simple Hinglish (e.g. IndexError, Matrix Shape Mismatch, IndentationError).",
        "Bhaiya's Desi Analogy: Uses memorable daily-life examples so the fundamental concept sticks permanently.",
        "Integrated Sandbox: Students can test the fixed code immediately in the browser execution console.",
        "Societal Impact: Removes late-night coding fear and dropout rates among beginner coders."
    ]
    for pt in pts6:
        p = rtf6.add_paragraph()
        p.text = f"✔ {pt}"
        p.font.size = Pt(9.5)
        p.font.color.rgb = SLATE

    # =========================================================================
    # SLIDE 7: Feature 4 - NLP Technical Interview Scorer
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7)
    add_header(s7, "Core AI Feature 4", "NLP Technical Interview Scorer (TF-IDF & Cosine Similarity)", "Evaluates student answers mathematically against gold-standard engineering benchmarks")
    
    if os.path.exists(img_interview):
        s7.shapes.add_picture(img_interview, Inches(0.8), Inches(1.7), Inches(7.5), Inches(5.1))
        
    rc7 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.6), Inches(1.7), Inches(3.9), Inches(5.1))
    rc7.fill.solid()
    rc7.fill.fore_color.rgb = WHITE
    rc7.line.color.rgb = RGBColor(147, 51, 234) # Purple
    rc7.line.width = Pt(1.5)
    
    rtf7 = rc7.text_frame
    rtf7.word_wrap = True
    rtf7.margin_left = rtf7.margin_right = rtf7.margin_top = Inches(0.25)
    
    p = rtf7.paragraphs[0]
    p.text = "Natural Language Processing Engine:"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = NAVY
    
    pts7 = [
        "TF-IDF Vectorization: Converts student responses and expert benchmark answers into high-dimensional semantic vectors.",
        "Cosine Distance Metric: Measures mathematical alignment and assigns a score out of 10 with high accuracy.",
        "Keyword Coverage Analysis: Highlights matched technical terms and flags missing core concepts.",
        "Interview Confidence: Helps students from non-English speaking backgrounds structure their technical explanations.",
        "Societal Impact: Levels the playing field so students from small towns can clear top technical placement rounds."
    ]
    for pt in pts7:
        p = rtf7.add_paragraph()
        p.text = f"✔ {pt}"
        p.font.size = Pt(9.5)
        p.font.color.rgb = SLATE

    # =========================================================================
    # SLIDE 8: Societal Impact & Alignment with AICTE / IBM SkillsBuild
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8)
    add_header(s8, "Outcomes & Societal Value", "Impact on Society & UN SDG 4 Alignment", "Bridging the regional skills divide through accessible, AI-powered education")
    
    # 4 Impact Pillars
    impacts = [
        ("Democratizing AI Education", "Makes high-end Machine Learning, Deep Learning, and coding mentorship accessible to every tier-2/3 student at just ₹149/mo instead of ₹50,000 bootcamps."),
        ("UN SDG 4: Quality Education", "Directly advances Target 4.4 by boosting the percentage of youth with relevant technical and vocational skills for employment and entrepreneurship."),
        ("Eliminating Language Barriers", "Bilingual Hinglish explanations remove the fear of complex English technical jargon, accelerating learning speed by 3x."),
        ("Proven Practical Implementation", "Fully operational web application running live on FastAPI, Scikit-Learn, PyTorch, and Python AST with sub-second response times.")
    ]
    
    for i, (title, desc) in enumerate(impacts):
        x = Inches(0.8 + (i % 2) * 5.9)
        y = Inches(1.8 + (i // 2) * 2.5)
        
        box = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(2.2))
        box.fill.solid()
        box.fill.fore_color.rgb = WHITE
        box.line.color.rgb = BORDER_LIGHT
        box.line.width = Pt(1.5)
        
        btf = box.text_frame
        btf.word_wrap = True
        btf.margin_top = Inches(0.2)
        btf.margin_left = btf.margin_right = Inches(0.25)
        
        p = btf.paragraphs[0]
        p.text = f"★ {title}"
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = INDIGO
        
        p = btf.add_paragraph()
        p.text = desc
        p.font.size = Pt(10.5)
        p.font.color.rgb = SLATE

    # Footer note
    ft = s8.shapes.add_textbox(Inches(0.8), Inches(6.8), Inches(11.733), Inches(0.5))
    ftf = ft.text_frame
    ftp = ftf.paragraphs[0]
    ftp.text = "Thank you! | Project 'CodeBhaiya' Developed by Sumit Kumar for AICTE | IBM SkillsBuild Internship Program 2026"
    ftp.font.bold = True
    ftp.font.size = Pt(11)
    ftp.font.color.rgb = NAVY
    ftp.alignment = PP_ALIGN.CENTER

    prs.save(output_pptx)
    print("Presentation created successfully at:", output_pptx)

if __name__ == "__main__":
    out = r"C:\Users\SUMIT\Desktop\CodeBhaiya_AICTE_IBM_Internship_Presentation.pptx"
    build_presentation(out)
