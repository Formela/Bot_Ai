from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def get_class(image, model, labels):
  np.set_printoptions(suppress=True)
  model = load_model(model, compile=False)
  class_names = open(labels, "r").readlines()

  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

  image = Image.open(image).convert("RGB")

  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  image_array = np.asarray(image)

  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

  data[0] = normalized_image_array

  # Przewiduje model
  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]


  Pies = class_name[2:].strip()
  if Pies == 'Boxer':
    msg = ('Boxer to rasa psów o średniej wielkości, znana z energii, przyjaznego usposobienia i charakterystycznego wyglądu z mocnymi mięśniami i krótkim futrem. Są bardzo towarzyscy i mają silny instynkt ochrony, co czyni je dobrymi psami stróżującymi. Potrzebują regularnego wysiłku fizycznego i interakcji z ludźmi, aby były szczęśliwe.')
    
  elif Pies == 'Owczarek':
    msg = ('Oto Informacje o Owczarku niemiecki: Niemiecki owczarek jest rasą psów dobrze znanych z inteligencji i lojalności.To średniej wielkości pies o silnej budowie, z charakterystycznymi uszami stojącymi. Są aktywni fizycznie i potrzebują dużo aktywności, aby być szczęśliwymi. Często są używane jako psy policyjne, stróżujące lub towarzyszące.')
  

  return (msg)