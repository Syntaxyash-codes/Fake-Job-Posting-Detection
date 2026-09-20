import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fake_job_model.pkl")
model_features = joblib.load("model_features.pkl")

st.set_page_config(
    page_title="FraudLens | Fake Job Detector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp {
    background: #0b0f19;
}

.block-container {
    max-width: 1350px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #263244;
}

.hero {
    padding: 35px 40px;
    border-radius: 22px;
    background: linear-gradient(135deg, #151d2f, #0f172a);
    border: 1px solid #263244;
    margin-bottom: 25px;
}

.hero-badge {
    display: inline-block;
    padding: 6px 13px;
    border-radius: 20px;
    background: #172554;
    color: #60a5fa;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 15px;
}

.hero-title {
    font-size: 43px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 8px;
}

.hero-subtitle {
    color: #94a3b8;
    font-size: 17px;
    max-width: 800px;
}

.section-card {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 20px;
}

.section-heading {
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 5px;
}

.section-description {
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 20px;
}

.metric-card {
    background: #111827;
    border: 1px solid #263244;
    border-radius: 15px;
    padding: 18px;
    text-align: center;
}

.metric-number {
    font-size: 25px;
    font-weight: 750;
}

.metric-label {
    color: #94a3b8;
    font-size: 13px;
}

.result-real {
    background: linear-gradient(135deg, #052e1b, #064e3b);
    border: 1px solid #10b981;
    border-radius: 20px;
    padding: 30px;
    text-align: center;
}

.result-fake {
    background: linear-gradient(135deg, #3b0a0a, #581c1c);
    border: 1px solid #ef4444;
    border-radius: 20px;
    padding: 30px;
    text-align: center;
}

.result-title {
    font-size: 34px;
    font-weight: 800;
}

.result-subtitle {
    color: #d1d5db;
    margin-top: 8px;
}

.confidence {
    font-size: 18px;
    font-weight: 650;
    margin-top: 18px;
}

.footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    padding-top: 20px;
}
</style>
""", unsafe_allow_html=True)


with st.sidebar:

    st.markdown("## 🛡️ FraudLens")

    st.caption("AI-powered job posting analysis")

    st.divider()

    st.markdown("### Model")
    st.info("Decision Tree Classifier")

    st.markdown("### Detection")
    st.write("Real Job")
    st.write("Potentially Fraudulent")

    st.divider()

    st.markdown("### How it works")

    st.write("01  Job information")
    st.write("02  Feature extraction")
    st.write("03  ML prediction")
    st.write("04  Risk classification")

    st.divider()

    st.caption("Machine Learning Project")


st.markdown("""
<div class="hero">
    <div class="hero-badge">MACHINE LEARNING • FRAUD DETECTION</div>
    <div class="hero-title">🛡️ FraudLens</div>
    <div class="hero-subtitle">
        An intelligent job posting analyzer that uses machine learning
        to identify potentially fraudulent employment opportunities.
    </div>
</div>
""", unsafe_allow_html=True)


m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">17,880</div>
        <div class="metric-label">Job Records</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">208</div>
        <div class="metric-label">Model Features</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">Decision Tree</div>
        <div class="metric-label">ML Algorithm</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">97.2%</div>
        <div class="metric-label">Test Accuracy</div>
    </div>
    """, unsafe_allow_html=True)


st.write("")

st.markdown("""
<div class="section-card">
<div class="section-heading">📋 Job Posting Analysis</div>
<div class="section-description">
Enter the details of a job posting. The trained model will analyze
its characteristics and generate a classification.
</div>
</div>
""", unsafe_allow_html=True)


left, right = st.columns(2, gap="large")


with left:

    st.markdown("#### Job Content")

    title = st.text_input(
        "Job Title",
        placeholder="e.g. Software Engineer"
    )

    company_profile = st.text_area(
        "Company Profile",
        placeholder="Enter company information...",
        height=120
    )

    description = st.text_area(
        "Job Description",
        placeholder="Enter the complete job description...",
        height=180
    )

    requirements = st.text_area(
        "Requirements",
        placeholder="Enter required skills and qualifications...",
        height=130
    )

    benefits = st.text_area(
        "Benefits",
        placeholder="Enter salary, benefits, perks, etc...",
        height=100
    )


with right:

    st.markdown("#### Job Attributes")

    employment_type = st.selectbox(
        "Employment Type",
        [
            "Unknown",
            "Full-time",
            "Part-time",
            "Contract",
            "Temporary",
            "Other"
        ]
    )

    required_experience = st.selectbox(
        "Required Experience",
        [
            "Unknown",
            "Internship",
            "Entry level",
            "Associate",
            "Mid-Senior level",
            "Director",
            "Executive",
            "Not Applicable"
        ]
    )

    required_education = st.selectbox(
        "Required Education",
        [
            "Unknown",
            "High School or equivalent",
            "Bachelor's Degree",
            "Master's Degree",
            "Doctorate",
            "Other"
        ]
    )

    industry = st.text_input(
        "Industry",
        placeholder="e.g. Information Technology"
    )

    function = st.text_input(
        "Job Function",
        placeholder="e.g. Engineering"
    )

    st.markdown("#### Posting Signals")

    c1, c2, c3 = st.columns(3)

    with c1:
        telecommuting = st.selectbox(
            "Remote",
            [0, 1],
            format_func=lambda x: "Yes" if x else "No"
        )

    with c2:
        has_company_logo = st.selectbox(
            "Logo",
            [0, 1],
            format_func=lambda x: "Yes" if x else "No"
        )

    with c3:
        has_questions = st.selectbox(
            "Questions",
            [0, 1],
            format_func=lambda x: "Yes" if x else "No"
        )


st.write("")

predict = st.button(
    "🔎 Analyze Job Posting",
    type="primary",
    use_container_width=True
)


if predict:

    if not title and not description:

        st.warning(
            "Please enter at least a Job Title or Job Description."
        )

        st.stop()


    new_data = pd.DataFrame([{
        "title_length": len(title),
        "description_length": len(description),
        "requirements_length": len(requirements),
        "company_profile_length": len(company_profile),
        "benefits_length": len(benefits),
        "has_email": int("@" in description),
        "has_url": int(
            "http" in description.lower()
            or "www." in description.lower()
        ),
        "telecommuting": telecommuting,
        "has_company_logo": has_company_logo,
        "has_questions": has_questions,
        "employment_type": employment_type,
        "required_experience": required_experience,
        "required_education": required_education,
        "industry": industry,
        "function": function
    }])


    categorical_features = [
        "employment_type",
        "required_experience",
        "required_education",
        "industry",
        "function"
    ]


    new_data[categorical_features] = (
        new_data[categorical_features].fillna("Unknown")
    )


    new_data = pd.get_dummies(
        new_data,
        columns=categorical_features,
        dtype=int
    )


    new_data = new_data.reindex(
        columns=model_features,
        fill_value=0
    )


    prediction = model.predict(new_data)[0]


    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(new_data)[0]

        confidence = max(probabilities) * 100

    else:

        confidence = None


    st.divider()

    st.markdown("### Analysis Result")


    if prediction == 0:

        st.markdown(
            f"""
            <div class="result-real">
                <div class="result-title">✓ REAL JOB</div>
                <div class="result-subtitle">
                    The model classified this posting as a real job.
                </div>
                <div class="confidence">
                    Model Confidence: {confidence:.2f}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="result-fake">
                <div class="result-title">⚠ POTENTIALLY FRAUDULENT</div>
                <div class="result-subtitle">
                    The model identified characteristics associated
                    with fraudulent job postings.
                </div>
                <div class="confidence">
                    Model Confidence: {confidence:.2f}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.write("")

    st.markdown("### Extracted Signals")

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.metric(
            "Title Length",
            len(title)
        )

    with s2:
        st.metric(
            "Description Length",
            len(description)
        )

    with s3:
        st.metric(
            "Requirements",
            len(requirements)
        )

    with s4:
        st.metric(
            "Benefits",
            len(benefits)
        )


    st.info(
        "The prediction is generated from the trained Decision Tree "
        "model using the same feature-processing pipeline used during training."
    )


st.markdown("""
<div class="footer">
FraudLens • Fake Job Posting Detection • Machine Learning
</div>
""", unsafe_allow_html=True)