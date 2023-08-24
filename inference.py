from predict import pre_process, predict
def predict_api(img_path):
    image = Image.open(img_path)
    image = pre_process(image)
    prediction = predict(image)
    return prediction

if __name__ == "__main__":
    if(len(sys.argv) != 2):
      print("Usage: python3 inference.py /path/to/image")
    else:
      path = sys.argv[1]
      print("The leaf in the image is predicted as"+predict_app(path))
