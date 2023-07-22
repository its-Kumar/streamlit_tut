# Imports
import pickle

import pandas as pd
import streamlit as st

# Globals
classes = ["setosa", "versicolor", "virginica"]
images = {
    "setosa": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Irissetosa1.jpg",
    "versicolor": "https://www.researchgate.net/publication/277311207/figure/fig11/AS:614122739732486@1523429679166/Iris-Setosa-Iris-Versicolor-Iris-Virginica.png",
    "virginica": "https://ars.els-cdn.com/content/image/3-s2.0-B9780128147610000034-f03-01-9780128147610.jpg",
}


@st.cache_resource
def load_model(model_path: str):
    """## load model

    Args:
        model_path (str): path of model location

    Returns:
        _type_: model object
    """
    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)
            print("model loaded!!")
            return model
    except Exception:
        print("model not exists")
        return None


model = load_model("iris_model.pkl")

# Main
st.title("Simple Iris Flower Predictor 💐")
st.write("This app predicts the Iris Flower type")

if model:
    features = list(model.feature_names_in_)

    # Sidebar
    with st.sidebar:
        st.sidebar.header("User Input parameters")
        sepal_length = st.number_input(
            features[0], min_value=4.0, max_value=8.0)
        sepal_width = st.number_input(
            features[1], min_value=2.0, max_value=4.5)
        petal_leght = st.number_input(
            features[2], min_value=1.0, max_value=7.0)
        petal_width = st.number_input(
            features[3], min_value=0.0, max_value=2.5)
        petal_leght = st.number_input(
            features[2], min_value=1.0, max_value=7.0)
        petal_width = st.number_input(
            features[3], min_value=0.0, max_value=2.5)

    inputs = [sepal_length, sepal_width, petal_leght, petal_width]
    print("inputs: ", inputs)
    inputs = pd.DataFrame([inputs], columns=features)

    prediction = model.predict(inputs)
    prediction = classes[prediction[0]]
    pred_prob = model.predict_proba(inputs)
    print("prediction: ", prediction)
    print("probability", pred_prob)

    st.header("User Inputs")
    st.dataframe(inputs, hide_index=True, use_container_width=True)

    st.header("Prediction")
    st.markdown(f"Predicted Flower Name: **{prediction.title()}**")
    st.image(images[prediction], width=500)

    st.subheader("Prediction Probabilities")
    st.dataframe(
        data=pd.DataFrame(
            pred_prob, columns=classes, index=["probability"]
        ).style.highlight_max(color="green", axis=1),
        use_container_width=True,
    )
