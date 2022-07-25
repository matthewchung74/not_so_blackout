try:
    from PIL import Image
    import io
    from enum import Enum
    from io import BytesIO, StringIO
    from typing import Union
    import pandas as pd
    import streamlit as st
    from not_so_blackout import test_image
except Exception as e:
    print(e)
 
STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""
 
 
class FileUpload(object):
 
    def __init__(self):
        self.fileTypes = ["csv", "png", "jpg", "jpeg"]
 
    def run(self):
        """
        Upload File on Streamlit Code
        :return:
        """
        st.info(__doc__)
        st.markdown(STYLE, unsafe_allow_html=True)
        file = st.file_uploader("Upload file", type=self.fileTypes)
        show_file1 = st.empty()
        show_file2 = st.empty()
        if not file:
            show_file1.info("Please upload a file of type: " + ", ".join(["csv", "png", "jpg"]))
            return
        content = file.getvalue()
        if isinstance(file, BytesIO):
            image = Image.open(io.BytesIO(content))
            print(type(image))
            image = image.resize((256, 256)).convert('RGB')
            image = test_image(image)
            show_file1.image(content)
            show_file2.image(image)

        file.close()
  
 
if __name__ ==  "__main__":
    header = st.container()
    with header:
        st.title("Less Black Blackout")
        st.text("SRGAN for removing PHI")

    helper = FileUpload()
    helper.run()
