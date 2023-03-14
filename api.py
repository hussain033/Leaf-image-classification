import uvicorn
from fastapi import FastAPI, File, UploadFile
from mangum import Mangum
from PIL import Image
from predict import pre_process, predict

app = FastAPI()
handler = Mangum(app)

@app.post("/predict/image")
def predict_api(myfile: UploadFile = File(...)):
    image = Image.open(myfile.file)
    #image = Image.frombytes('RGB',(180,120),image)
    image = pre_process(image)
    prediction = predict(image)
    return prediction

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000,debug=True)