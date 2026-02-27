import os
import joblib
import re
from django.shortcuts import render
from django.conf import settings
from .utils import extract_text_from_pdf, extract_text_from_docx


# ==============================
# Load Model
# ==============================

MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    'classifier',
    'model',
    'resume_classifier_tuned.pkl'
)

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print("Model loading failed:", e)


# ==============================
# Label Mapping
# ==============================

LABEL_MAP = {
    0: "Peoplesoft",
    1: "React JS",
    2: "SQL Developer",
    3: "Workday"
}


# ==============================
# Resume Validation Function
# ==============================

def is_valid_resume(text):
    """
    Check whether uploaded document looks like a resume.
    """

    if not text or len(text.strip()) < 200:
        return False

    text_lower = text.lower()

    resume_keywords = [
        "education",
        "experience",
        "skills",
        "projects",
        "certification",
        "objective",
        "summary",
        "contact",
        "email",
        "phone"
    ]

    keyword_matches = sum(keyword in text_lower for keyword in resume_keywords)

    # Require at least 3 resume-related sections
    if keyword_matches >= 3:
        return True

    return False


# ==============================
# Main View
# ==============================

def upload_resume(request):
    prediction = None
    confidence = None
    error = None

    if request.method == "POST":

        uploaded_file = request.FILES.get("resume_file")

        if not uploaded_file:
            error = "No file uploaded."
        else:
            file_name = uploaded_file.name.lower()

            try:
                # -------- File Type Check --------
                if file_name.endswith(".pdf"):
                    text = extract_text_from_pdf(uploaded_file)

                elif file_name.endswith(".docx"):
                    text = extract_text_from_docx(uploaded_file)

                else:
                    error = "Only PDF and DOCX resume files are supported."
                    return render(request, "upload.html", {"error": error})

                # -------- Resume Content Validation --------
                if not is_valid_resume(text):
                    error = "Uploaded file does not appear to be a valid resume."

                elif model is None:
                    error = "Model not loaded properly."

                else:
                    # -------- Prediction --------
                    predicted_class = model.predict([text])[0]
                    prediction = LABEL_MAP.get(predicted_class, "Unknown")

                    # -------- Confidence --------
                    if hasattr(model, "predict_proba"):
                        probabilities = model.predict_proba([text])[0]
                        confidence = round(max(probabilities) * 100, 2)
                    else:
                        confidence = "N/A"

            except Exception as e:
                error = f"Error processing file: {str(e)}"

    return render(request, "upload.html", {
        "prediction": prediction,
        "confidence": confidence,
        "error": error
    })
def home(request):
    return render(request, 'home.html')