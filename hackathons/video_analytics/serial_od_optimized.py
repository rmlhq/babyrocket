import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import mlflow
from  mlflow.tracking import MlflowClient

import tensorflow as tf
import tensorflow_hub as hub
from tqdm import tqdm 
import time

from PIL import Image
from image_utils import download_and_resize_image,draw_boxes,save_to_file
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("--exp_name",type=str,help="Experiment Name",default="Default")
args                  = parser.parse_args()

exp_name = args.exp_name
size = 1
rank = 0

image_urls = [
  # Source: https://commons.wikimedia.org/wiki/File:The_Coleoptera_of_the_British_islands_(Plate_125)_(8592917784).jpg
  "https://upload.wikimedia.org/wikipedia/commons/1/1b/The_Coleoptera_of_the_British_islands_%28Plate_125%29_%288592917784%29.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Biblioteca_Maim%C3%B3nides%2C_Campus_Universitario_de_Rabanales_007.jpg/1024px-Biblioteca_Maim%C3%B3nides%2C_Campus_Universitario_de_Rabanales_007.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/0/09/The_smaller_British_birds_%288053836633%29.jpg",
  "https://upload.wikimedia.org/wikipedia/commons/0/09/The_smaller_British_birds_%288053836633%29.jpg",
  ]

# Increase the number of images to demonstrate parallel processing
image_urls = image_urls*25
total_images = len(image_urls)

# Get number of images processed per process
images_per_process = int(total_images/size)

# Get first and last images for the given process
start_image = rank*images_per_process

# tracking_uri = os.environ.get("TRACKING_URL")
# client = MlflowClient(tracking_uri=tracking_uri)
# mlflow.set_tracking_uri(tracking_uri)
# experiments = client.list_experiments()
# experiment_names = []
# for exp in experiments:
#     experiment_names.append(exp.name)
# experiment_name = exp_name
# if experiment_name not in experiment_names:
#     mlflow.create_experiment(experiment_name)
# mlflow.set_experiment(experiment_name)

mlflow_params  = {}
mlflow_metrics = {}
mlflow_params["rank"] = rank

# For last process get all the images
if rank == size-1:
  end_image   = total_images
else:
  end_image   = (rank+1)*images_per_process

print("Rank %d, Start %d, End %d"%(rank,start_image,end_image))


# Get the detector
module_handle = "https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1"
detector = hub.load(module_handle).signatures['default']

# object detection on images for this proces
total_runtime = 0
for _id,_url in enumerate(tqdm(image_urls[start_image:end_image],desc="Rank %d"%rank)):    
    path           = download_and_resize_image(_url, 640, 480)
    img            = tf.io.read_file(path)
    img            = tf.image.decode_jpeg(img, channels=3)
    converted_img  = tf.image.convert_image_dtype(img, tf.float32)[tf.newaxis, ...]

    start_time = time.time()
    result     = detector(converted_img)
    end_time   = time.time()

    result        = {key:value.numpy() for key,value in result.items()}
    objects       = list(set(result['detection_class_entities'].tolist()))
    total_runtime = total_runtime + (end_time - start_time)
    
    # print("Rank %d, image %s, runtime %0.2f"%(rank,path,end_time-start_time))
    mlflow_params["objects"]   = objects
    mlflow_metrics["runtime"]  = end_time - start_time
    
    image_with_boxes = draw_boxes(
      img.numpy(), result["detection_boxes"],
      result["detection_class_entities"], result["detection_scores"])
    filename = save_to_file(image_with_boxes)
    
    # try:
    #   with mlflow.start_run():
    #     mlflow.log_params(mlflow_params)
    #     mlflow.log_metrics(mlflow_metrics)
    #     mlflow.log_artifact(filename)
    # except:
    #   print("Retrying to enter data into the database")
#print("Rank %d, Average object detection time = %0.3f"%(rank,total_runtime/(end_image-start_image)))
