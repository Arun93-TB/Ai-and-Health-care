import os
import joblib

# Load trained model
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "disease_model.pkl")
model = joblib.load(model_path)


def predict_disease(fever, cough, headache, fatigue,
                    body_pain, vomiting, breathing):

    input_data = [[
        int(fever),
        int(cough),
        int(headache),
        int(fatigue),
        int(body_pain),
        int(vomiting),
        int(breathing)
    ]]

    disease = model.predict(input_data)[0]

    confidence = round(max(model.predict_proba(input_data)[0]) * 100, 2)

    return disease, confidence


# Test
if __name__ == "__main__":

    disease, confidence = predict_disease(
        1, 1, 1, 1, 1, 0, 0
    )

    print("Disease :", disease)
    print("Confidence :", confidence, "%")