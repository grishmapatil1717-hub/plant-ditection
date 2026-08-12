"""
🌿 Plant Disease Predictor — Streamlit GUI
--------------------------------------------
Drop your trained model in the `load_model()` and `predict()` functions
below and this GUI will handle the rest.

Run with:
    streamlit run plant_disease_app.py
"""

import streamlit as st
from PIL import Image
import numpy as np
import time
import io
from fpdf import FPDF


def generate_pdf_report(image: Image.Image, label, confidence, top3, info, severity_result):
    """Builds a simple one-page PDF summarizing the prediction."""
    img_buffer = io.BytesIO()
    image.save(img_buffer, format="JPEG")
    img_buffer.seek(0)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Plant Disease Prediction Report", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 8, f"Generated: {time.strftime('%Y-%m-%d %H:%M')}", ln=True)
    pdf.ln(4)

    # Save image to a temp file since fpdf reads image paths, not buffers directly
    temp_img_path = "temp_report_image.jpg"
    image.save(temp_img_path, format="JPEG")
    pdf.image(temp_img_path, w=80)
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 8, f"Result: {label} ({confidence*100:.1f}% confidence)", ln=True)
    pdf.ln(2)

    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 7, "Top Predictions:", ln=True)
    pdf.set_font("Helvetica", "", 10)
    for cls, prob in top3:
        pdf.cell(0, 6, f"  {cls}: {prob*100:.1f}%", ln=True)
    pdf.ln(2)

    if info:
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(0, 7, "About this result:", ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 6, info["description"])
        pdf.ln(1)
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(0, 7, "Suggested action:", ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 6, info["remedy"])
        pdf.ln(1)

    if severity_result:
        severity_label, coverage = severity_result
        pdf.set_font("Helvetica", "B", 11)
        pdf.cell(0, 7, f"Estimated severity: {severity_label} (~{coverage*100:.0f}% lesion coverage)", ln=True)
        pdf.set_font("Helvetica", "I", 9)
        pdf.multi_cell(0, 5, "Rough estimate based on leaf discoloration, not a trained severity model.")

    return bytes(pdf.output(dest="S"))


# ------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------
st.set_page_config(
    page_title="🌱 Plant Disease Predictor",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------
# CUSTOM STYLING (cute, soft plant theme)
# ------------------------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f3fbf4 0%, #e8f5e9 100%);
    }
    h1 {
        color: #2e7d32;
        font-family: 'Trebuchet MS', sans-serif;
    }
    .result-card {
        background: white;
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 4px 14px rgba(0,0,0,0.08);
        border: 2px solid #a5d6a7;
        margin-top: 1rem;
    }
    .stButton>button {
        background-color: #66bb6a;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.6rem 1.4rem;
        font-weight: 600;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background-color: #4caf50;
        transform: scale(1.03);
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🌿 About")
    st.write(
        "Upload a photo of a plant leaf and this app will predict "
        "whether it's healthy or affected by disease."
    )
    st.markdown("---")
    st.markdown("### 📋 Tips for best results")
    st.write("- Use a clear, well-lit photo\n- Focus on a single leaf\n- Avoid blurry images")
    st.markdown("---")
    st.caption("Model: your model name here")

# ------------------------------------------------------------------
# HEADER
# ------------------------------------------------------------------
st.title("🌱 Plant Disease Predictor")
st.write("Upload a leaf image below and click **Predict** to check its health.")

# ------------------------------------------------------------------
# MODEL LOADING (cache so it only loads once)
# ------------------------------------------------------------------
import os

# --- CONFIG: set this to your Drive file's shareable link ID ---
# Get it from a Drive share link like:
#   https://drive.google.com/file/d/FILE_ID_HERE/view?usp=sharing
GDRIVE_FILE_ID = "1uPPXXC90noUpibecudBMiw9RPht9wpCP"
LOCAL_MODEL_PATH = "plant_model.keras"  # matches your Drive file's actual format


def download_model_from_drive(file_id: str, output_path: str):
    """Downloads the model from Google Drive if it isn't already local."""
    if os.path.exists(output_path):
        return  # already downloaded, skip
    import gdown
    url = f"https://drive.google.com/uc?id={file_id}"
    with st.spinner("Downloading model from Google Drive (first run only)..."):
        gdown.download(url, output_path, quiet=False)


@st.cache_resource
def load_model():
    """
    OPTION A (simplest): if you already manually downloaded the model file
    into this folder, just skip the Drive download and load directly:

        import tensorflow as tf
        return tf.keras.models.load_model(LOCAL_MODEL_PATH)

    OPTION B (auto-download from Drive, used below): make sure the Drive
    file's sharing is set to "Anyone with the link", paste its file ID
    into GDRIVE_FILE_ID above, then run `pip install gdown`.
    """
    download_model_from_drive(GDRIVE_FILE_ID, LOCAL_MODEL_PATH)

    import tensorflow as tf
    return tf.keras.models.load_model(LOCAL_MODEL_PATH)


CLASS_NAMES = ["Healthy", "Early_Blight", "Late_Blight"]
IMG_SIZE = (224, 224)

DISEASE_INFO = {
    "Healthy": {
        "description": "No signs of disease detected on this leaf.",
        "remedy": "Keep up good watering, sunlight, and airflow practices to maintain plant health.",
    },
    "Early_Blight": {
        "description": "A fungal disease causing brown spots with concentric rings, usually starting on older leaves.",
        "remedy": "Remove and dispose of affected leaves, avoid overhead watering, apply a copper-based fungicide, and rotate crops each season.",
    },
    "Late_Blight": {
        "description": "A fast-spreading, aggressive fungal disease causing dark, water-soaked lesions that can destroy a plant within days.",
        "remedy": "Remove and destroy infected plants immediately to stop spread, apply an appropriate fungicide, and improve air circulation around plants.",
    },
}


def estimate_severity(image: Image.Image, label: str):
    """
    Rough, non-ML severity estimate based on lesion color coverage.
    NOT a substitute for a trained severity model — this approximates
    how much of the leaf shows brown/dark discoloration, which loosely
    correlates with infection extent for blight-type diseases.
    Only meaningful when a disease was actually detected.
    """
    if label == "Healthy":
        return None  # no severity to estimate

    img_array = np.array(image.resize((224, 224)), dtype=np.float32) / 255.0
    r, g, b = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]

    # Leaf mask: greenish pixels (rough threshold, not perfect)
    leaf_mask = (g > r) & (g > b * 0.8)

    # Lesion mask: brown/dark spots (low green relative to red, or generally dark)
    lesion_mask = ((r > g) | (r + g + b < 0.6)) & leaf_mask

    leaf_pixels = np.sum(leaf_mask)
    lesion_pixels = np.sum(lesion_mask)

    if leaf_pixels == 0:
        return None

    coverage = lesion_pixels / leaf_pixels

    if coverage < 0.15:
        return "Mild", coverage
    elif coverage < 0.35:
        return "Moderate", coverage
    else:
        return "Severe", coverage

def predict(image: Image.Image, model):
    """Real inference matching the training preprocessing (RGB, 224x224, /255.0)."""
    image_resized = image.resize(IMG_SIZE)
    image_array = np.array(image_resized, dtype=np.float32) / 255.0
    image_input = np.expand_dims(image_array, axis=0)

    probabilities = model.predict(image_input, verbose=0)[0]

    ranked = sorted(zip(CLASS_NAMES, probabilities), key=lambda x: -x[1])
    top_label, top_prob = ranked[0]
    return top_label, float(top_prob), ranked


# ------------------------------------------------------------------
# MAIN UI
# ------------------------------------------------------------------
model = load_model()

uploaded_file = st.file_uploader(
    "Choose a leaf image", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("🔍 Predict"):
        with st.spinner("Analyzing leaf..."):
            label, confidence, top3 = predict(image, model)
        severity_result = estimate_severity(image, label)
        # Store everything needed to redraw results + build the PDF,
        # so it survives the rerun triggered by the download button.
        st.session_state["result"] = {
            "label": label,
            "confidence": confidence,
            "top3": top3,
            "severity_result": severity_result,
        }

    if "result" in st.session_state:
        r = st.session_state["result"]
        label, confidence, top3, severity_result = (
            r["label"], r["confidence"], r["top3"], r["severity_result"]
        )

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        if label.lower() == "healthy":
            st.success(f"✅ **{label}** ({confidence*100:.1f}% confidence)")
        else:
            st.error(f"⚠️ **{label}** ({confidence*100:.1f}% confidence)")

        st.markdown("**Top predictions:**")
        for cls, prob in top3:
            st.write(f"{cls}: {prob*100:.1f}%")
            st.progress(float(prob))

        info = DISEASE_INFO.get(label)
        if info:
            st.markdown("---")
            st.markdown(f"**About this result:** {info['description']}")
            st.markdown(f"**Suggested action:** {info['remedy']}")

        if severity_result:
            severity_label, coverage = severity_result
            st.markdown(f"**Estimated severity:** {severity_label} (~{coverage*100:.0f}% lesion coverage)")
            st.caption("⚠️ Rough estimate based on leaf discoloration, not a trained severity model. Use as a general guide only.")
        st.markdown('</div>', unsafe_allow_html=True)

        pdf_bytes = generate_pdf_report(image, label, confidence, top3, info, severity_result)
        st.download_button(
            "📄 Download PDF Report",
            data=pdf_bytes,
            file_name="plant_disease_report.pdf",
            mime="application/pdf",
        )
else:
    st.info("👆 Upload an image to get started.")
