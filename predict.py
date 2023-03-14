import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image

def pre_process(image: Image.Image):
    # load the image and convert into
    # numpy array
    img = image.resize((180,120))
    # asarray() class is used to convert
    # PIL images into NumPy arrays
    numpydata = np.asarray(img)
    image = np.expand_dims(numpydata, axis=0)
    #image = image//255.0
    return image
    
def predict(image: Image.Image):
    #save_option = tf.saved_model.LoadOptions(experimental_io_device='/job:localhost', )
    model = tf.keras.models.load_model('leaf_classify.h5',custom_objects={'KerasLayer':hub.KerasLayer})#, options=save_option)
    pre = model.predict(image,batch_size = None)
    result = np.argmax(pre)
    classes = ['Alstonia Scholaris','Arjun','Bael','Basil','Chinar','Gauva','Jamun','Jatropa','Lemon','Mango','Pomegranate',
'Pongamia Pinnata']
    return classes[result]