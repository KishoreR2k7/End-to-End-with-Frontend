import gradio as gr
import pandas as pd
import pickle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("model_columns.pkl", "rb") as f:
    model_columns = pickle.load(f)
def predict_life_expectancy(*args):
    input_data = pd.DataFrame([args], columns=model_columns)
    return model.predict(input_data)[0]
def login(username, password):
    if username == "kishore" and password == "123456":
        return gr.update(visible=True), gr.update(visible=False), ""
    else:
        return gr.update(visible=False), gr.update(visible=True), "❌ Invalid username or password"
css_style="""
.gradio-container {
    background: linear-gradient(135deg, #E3F2FD, #FFFFFF);
    color: #0D47A1;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding: 20px;
}

/* Login card */
.login-card {
    background: linear-gradient(135deg, #E1F5FE, #BBDEFB);
    padding: 30px;
    border-radius: 16px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.1);
    max-width: 400px;
    margin: auto;
}

/* Input boxes */
input[type="text"], input[type="password"], input[type="number"] {
    background: linear-gradient(90deg, #BBDEFB, #90CAF9);
    color: #0D47A1;
    border: 2px solid #64B5F6;
    border-radius: 12px;
    padding: 10px 15px;
    font-size: 1em;
    width: 100%;
    margin-bottom: 15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}

/* Output box */
.output-box input[type="number"] {
    background: linear-gradient(90deg, #E1F5FE, #B3E5FC);
    color: #0D47A1;
}

/* Buttons */
.gr-button {
    background: linear-gradient(90deg, #64B5F6, #42A5F5);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 25px;
    font-size: 1.1em;
    cursor: pointer;
    transition: all 0.3s ease;
    width: 100%;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}
.gr-button:hover {
    background: linear-gradient(90deg, #42A5F5, #1E88E5);
    transform: scale(1.05);
}

/* Titles */
h1 {
    color: #0D47A1;
    text-align: center;
    margin-bottom: 20px;
    font-size: 2.2em;
}

/* Card container for predictor */
.gr-column {
    background: linear-gradient(135deg, #FFFFFF, #E3F2FD);
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.1);
    gap: 12px;
}
"""
with gr.Blocks(css=css_style) as demo:
    with gr.Column(elem_classes=["login-card"], visible=True) as login_page:
        gr.HTML("<h1>🔒 Login</h1>")
        username = gr.Textbox(label="Username", placeholder="Enter your username")
        password = gr.Textbox(label="Password", type="password", placeholder="Enter your password")
        login_btn = gr.Button("Login")
        login_msg = gr.Label("")
    with gr.Column(visible=False) as predictor_page:
        gr.HTML("<h1>🌍 Life Expectancy Predictor</h1>")
        gr.Markdown("Predict life expectancy based on socio-economic and health features.")
        with gr.Column():
            inputs = [gr.Number(label=col) for col in model_columns]
            output = gr.Number(label="Predicted Life Expectancy", elem_classes=["output-box"])
            gr.Button("Predict").click(predict_life_expectancy, inputs, output)
    login_btn.click(
        login,
        inputs=[username, password],
        outputs=[predictor_page, login_page, login_msg]
    )
demo.launch()
