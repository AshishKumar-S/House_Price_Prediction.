from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import joblib
import uvicorn

app = FastAPI()

# Load trained model
obj = joblib.load("california1.joblib")
model = obj['model']


# ================= HOME PAGE =================
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>California House Price Predictor</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(to right, #4facfe, #00f2fe);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }

                .container {
                    background: white;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 15px 30px rgba(0,0,0,0.2);
                    width: 420px;
                }

                h2 {
                    text-align: center;
                    margin-bottom: 20px;
                }

                label {
                    font-weight: bold;
                }

                input {
                    width: 100%;
                    padding: 8px;
                    margin: 6px 0 15px 0;
                    border-radius: 6px;
                    border: 1px solid #ccc;
                }

                button {
                    width: 100%;
                    padding: 10px;
                    background: #4facfe;
                    color: white;
                    border: none;
                    border-radius: 6px;
                    font-size: 16px;
                    cursor: pointer;
                }

                button:hover {
                    background: #00c6ff;
                }
            </style>
        </head>

        <body>
            <div class="container">
                <h2>🏠 California House Price</h2>

                <form action="/predict" method="post">

                    <label>Median Income:</label>
                    <input type="number" step="any" name="MedInc" required>

                    <label>House Age:</label>
                    <input type="number" step="any" name="HouseAge" required>

                    <label>Average Rooms:</label>
                    <input type="number" step="any" name="AveRooms" required>

                    <label>Population:</label>
                    <input type="number" step="any" name="Population" required>

                    <label>Average Occupancy:</label>
                    <input type="number" step="any" name="AveOccup" required>

                    <label>Latitude:</label>
                    <input type="number" step="any" name="Latitude" required>

                    <button type="submit">Predict Price</button>

                </form>
            </div>
        </body>
    </html>
    """


# ================= PREDICTION =================
@app.post("/predict", response_class=HTMLResponse)
def predict(
    MedInc: float = Form(...),
    HouseAge: float = Form(...),
    AveRooms: float = Form(...),
    Population: float = Form(...),
    AveOccup: float = Form(...),
    Latitude: float = Form(...)
):

    input_data = [[
        MedInc,
        HouseAge,
        AveRooms,
        Population,
        AveOccup,
        Latitude
    ]]

    prediction = model.predict(input_data)[0]

    return f"""
    <html>
        <head>
            <title>Prediction Result</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(to right, #43e97b, #38f9d7);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}

                .result-box {{
                    background: white;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 15px 30px rgba(0,0,0,0.2);
                    text-align: center;
                }}

                .price {{
                    font-size: 26px;
                    font-weight: bold;
                    margin: 20px 0;
                }}

                a {{
                    text-decoration: none;
                    background: #43e97b;
                    color: white;
                    padding: 10px 18px;
                    border-radius: 6px;
                }}

                a:hover {{
                    background: #2ecc71;
                }}
            </style>
        </head>

        <body>
            <div class="result-box">
                <h2>Prediction Result</h2>
                <div class="price">
                    Predicted Price: ${round(prediction * 100000, 2)}
                </div>
                <a href="/">Predict Again</a>
            </div>
        </body>
    </html>
    """


# ================= RUN SERVER =================
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)