## Video Analytics

### Pre-requisites

1. Python >=3.7
2. tensorflow==2.3.1
3. tensorflow-hub==0.9.0
4. matplotlib==3.1.3
5. youtube-dl==2020.9.20
6. Access to BabyRocket (optional)

### Getting Started

#### On your local machine
1. Clone two git repositories.
    - `git clone https://github.com/rmlhq/babyrocket`
    - `git clone https://github.com/streamlit/demo-self-driving`
2. Start Jupyter lab and go through the tutorials in the next section
3. Extract objects and meta data from video and build applications using tensorflow, tensorflow-hub, and streamlit 

#### On BabyRocket
1. Email us [here](mailto:info@rocketml.net) to get access to BabyRocket.
2. Login to BabyRocket
3. Go to projects page and create a project
4. From project details page open Jupyterlab
5. Open a terminal and clone [hackathon tutorials](https://github.com/rmlhq/babyrocket) and [streamlit self-driving demo](https://github.com/streamlit/demo-self-driving) git repositories
6. Install all required python libraries 
   ` sudo /opt/conda/bin/pip install --upgrade tensorflow tensorflow-hub youtube-dl matplotlib`
7. (Optional) Scale up the master node to B8ms with 8 cores and 32GB memory


### Tutorials

1. [OpenCV Image and Video Processing](opencv_image_video_processing.ipynb)
2. [Object Detection using Tensorflowhub](object_detection.ipynb)
3. Object detection using REST APIs
4. Distributed object detection 
5. [UI application using Streamlit](https://github.com/streamlit/demo-self-driving)

### How to deploy a streamlit app on BabyRocket and share with others?

Step 1: Start a streamlit app. Below is an example to start the self-driving demo app
```streamlit run https://raw.githubusercontent.com/streamlit/demo-self-driving/master/app.py
   
   You can now view your Streamlit app in your browser.

   Network URL: http://10.0.2.35:8501
   External URL: http://13.77.163.202:8501
```

Step 2: On BabyRocket, go to projects detail and click on **App** button or add a tab in the project and select **App**. Enter the port number, "/8501/" in the form and click on **Add to App Tab**

Step 3: Hover on the **App** tab and click on "Copy URL" icon. Share the URL with the world!