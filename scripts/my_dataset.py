import os

from PIL import Image
import torch
from torch.utils.data import Dataset
import cv2
import numpy as np
class MyDataSet(Dataset):
    """自定义数据集"""

    def __init__(self, images_path: list, images_class: list, transform=None):
        self.images_path = images_path
        self.images_class = images_class
        self.transform = transform

    def __len__(self):
        return len(self.images_path)

    def __getitem__(self, item):
        img = Image.open(self.images_path[item]).convert('RGB')
        # RGB为彩色图片，L为灰度图片
        #raise ValueError("image: {} isn't RGB mode.".format(self.images_path[item]))
        
        label = self.images_class[item]

        if self.transform is not None:
            img = self.transform(img)

        return img, label

    @staticmethod
    def collate_fn(batch):
        # 官方实现的default_collate可以参考
        # https://github.com/pytorch/pytorch/blob/67b7e751e6b5931a9f45274653f4f653a4e6cdf6/torch/utils/data/_utils/collate.py
        images, labels = tuple(zip(*batch))

        images = torch.stack(images, dim=0)
        labels = torch.as_tensor(labels)
        return images, labels

class CustomDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        """
        root_dir: 数据集的目录，每个类别的图像存储在子目录中
        transform: torchvision.transforms 的转换操作
        """
        self.root_dir = root_dir
        self.transform = transform

        self.classes = os.listdir(root_dir)
        self.class_to_idx = {cls_name: i for i, cls_name in enumerate(self.classes)}

        self.imgs = []
        for cls in self.classes:
            cls_dir = os.path.join(root_dir, cls)
            self.imgs += [(os.path.join(cls_dir, fname), self.class_to_idx[cls]) for fname in os.listdir(cls_dir)]

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, idx):
        img_path, label = self.imgs[idx]
        image = Image.open(img_path).convert('RGB')

        if self.transform:
            image = self.transform(image)

        return image, label

    @staticmethod
    def collate_fn(batch):
        # https://github.com/pytorch/pytorch/blob/67b7e751e6b5931a9f45274653f4f653a4e6cdf6/torch/utils/data/_utils/collate.py
        images, labels = tuple(zip(*batch))

        images = torch.stack(images, dim=0)
        labels = torch.as_tensor(labels)
        return images, labels
