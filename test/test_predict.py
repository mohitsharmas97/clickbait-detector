import os
import sys
import joblib
import warnings
warnings.filterwarnings("ignore")

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

sys.path.insert(0, parent_dir)

from backend.api.utils import predict_clickbait
from backend.api.main import translate_to_english  

# Model loading test
try:
    MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'backend', 'models', 'combined.joblib')
    model_components = joblib.load(os.path.abspath(MODEL_PATH))
    print("[SUCCESS] Model loaded successfully")
except FileNotFoundError:
    print(f"[ERROR] Model file not found: {MODEL_PATH}")
    sys.exit(1)

try:
    test_titles = [
        "Google Cloud Associate Cloud Engineer Course - Pass the Exam!",
        "Scientists discover new method for treating cancer",
        "You Won't Believe What Happened Next!"
    ]

    print("\n[TEST] English Clickbait Predictions:\n")
    for title in test_titles:
        result = predict_clickbait(title, model_components)
        print(f"Title: {title}")
        print(f" → Prediction: {result['prediction']} | Combined Probability: {result['combined_probability']:.3f}")

    print("[SUCCESS] English prediction tests passed\n")
except Exception as e:
    print(f"[ERROR] Error during English clickbait prediction tests: {e}")

# testing non english title transltion + prediction
try:
    non_english_titles = [
        "Este es un título increíble",      # spanish
        "Ceci est un titre incroyable",     # french
        "यह एक अविश्वसनीय शीर्षक है"       # hindi
    ]

    print("[TEST] Non-English Translation & Prediction:\n")
    for title in non_english_titles:
        translated = translate_to_english(title)
        print(f"Original: {title}")
        print(f"Translated: {translated}")
        result = predict_clickbait(translated, model_components)
        print(f" → Prediction: {result['prediction']} | Combined Probability: {result['combined_probability']:.3f}\n")

    print("[SUCCESS] Non-English translation + prediction tests passed\n")
except Exception as e:
    print(f"[ERROR] Error during non-English prediction tests: {e}")
