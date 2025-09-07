import gradio as gr
import pandas as pd
import pickle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)
def predict_life_expectancy(*args):
    input_data = pd.DataFrame([args], columns=model_columns)
    prediction = model.predict(input_data)[0]
    return prediction
css_style = """
.gradio-container {
    background: linear-gradient(135deg, #E3F2FD, #FFFFFF);
    color: #0D47A1;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 20px;
}
h1 {
    color: #0D47A1;
    text-align: center;
    margin-bottom: 10px;
    font-size: 2.4em;
    text-shadow: 1px 1px 3px #B0C4DE50;
}
.gr-markdown {
    color: #1565C0;
    text-align: center;
    margin-bottom: 25px;
    font-size: 1.2em;
}
input[type="number"] {
    background: linear-gradient(90deg, #BBDEFB, #90CAF9);
    color: #0D47A1;
    border: 2px solid #64B5F6;
    border-radius: 12px;
    padding: 10px 15px;
    font-size: 1em;
    width: 100%;
    box-sizing: border-box;
    margin-bottom: 15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}
.output-box input[type="number"] {
    background: linear-gradient(90deg, #E1F5FE, #B3E5FC);
    color: #0D47A1;
    border: 2px solid #64B5F6;
    border-radius: 12px;
    padding: 10px 15px;
    font-size: 1em;
    width: 100%;
    box-sizing: border-box;
    margin-bottom: 15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}
.gr-button {
    background: linear-gradient(90deg, #64B5F6, #42A5F5);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 25px;
    font-size: 1.1em;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-top: 10px;
    width: 100%;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}
.gr-button:hover {
    background: linear-gradient(90deg, #42A5F5, #1E88E5);
    transform: scale(1.05);
}
.gr-column {
    background: linear-gradient(135deg, #FFFFFF, #E3F2FD);
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.1);
    gap: 12px;
}
"""

with gr.Blocks(css=css_style) as demo:
    gr.HTML("<h1>🌍 Life Expectancy Predictor</h1>")
    gr.Markdown("Predict life expectancy based on socio-economic and health features.")

    with gr.Column():  # Card container
        inputs = [gr.Number(label=col) for col in model_columns]
        output = gr.Number(label="Predicted Life Expectancy", elem_classes=["output-box"])
        gr.Button("Predict").click(predict_life_expectancy, inputs, output)

demo.launch(auth=("kishore","123456"))
