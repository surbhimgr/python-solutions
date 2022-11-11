from detectron2.logger import setup_logger
setup_logger
from detectron2.data.datasets import register_coco_instances
from detectron2.engine import DefaultTrainer
import os
import pickle

config_file_path="detectron2/blob/main/configs/Misc/cascade_mask_rcnn_X_152_32x8d_FPN_IN5k_gn_dconv.yaml"
checkpoint_url="detectron2/blob/main/configs/Misc/cascade_mask_rcnn_X_152_32x8d_FPN_IN5k_gn_dconv.yaml"
output_dir = "/content/output/object_detection"
num_classes = 2

device = "cuda"

train_dataset_name = "MRCNN_train"
train_images_path = "/content/train"
train_json_annot_path = "/content/train.json"

test_dataset_name = "MRCNN_test"
test_images_path = "/content/test"
test_json_annot_path = "/content/test.json"

register_coco_instances(name = train_dataset_name, metadata={}, json_file = train_json_annot_path, image_root = train_images_path)
register_coco_instances(name = train_dataset_name, metadata={}, json_file = train_json_annot_path, image_root = train_images_path)



plot_samples(dataset_name = train_dataset_name, n=2)