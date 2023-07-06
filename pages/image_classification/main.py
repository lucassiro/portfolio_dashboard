import cv2
from PIL import Image
import numpy as np
import streamlit as st
import streamlit.components.v1 as components

st.title("Computer vision")

# st.sidebar.title("Pages")
st.title("Image classification")
st.markdown("## Cats and Dogs")
'''
Você pode conferir toda a etapa de carregamento de dados, pré processamento
construção, treinamento e avaliação do modelo no link abaixo


components.html(
    """
    <a target="_blank" href="https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/model_monitoring/model_monitoring.ipynb">
      <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
    </a>
    """
)

st.markdown(
    """In this project, vamos construir
    um modelo bla bla bla"""
)

'''

https://github.com/GSNCodes/Image-Classification-Streamlit-TensorFlow/blob/main/app.py

file = st.file_uploader("Choose a image", accept_multiple_files=False)
img = cv2.imread(file)
# st.write(type(img))

    
    # test_image = Image.open(uploaded_file)
    # st.write(test_image)

# st.write("This is a simple image classification web app to identify cars")
# file = st.file_uploader("Please upload an image file", type=["jpg", "png"])


# def load_image(image_data):

#         image = load_img(image_data,target_size=(64,64))  

#         img = img_to_array(image)

#         img = np.array(image) 
#         img = img / 255.0
#         image = img.resize((64,64))

#         img = img.reshape(1,64,64,3)
#         label = model.predict_classes(img)
    
#         prediction = label[0][0]
        
#         return f"Prediction: {prediction}" 

# if file is None:
#     st.text("Please upload an image file")
# else:
#     import_and_predict(file, model)