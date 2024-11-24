### Dataset Usage Instructions

The datasets provided in this repository are organized into subdirectories where each subdirectory corresponds to a specific class label. The provided `CustomDataset` class in the `scripts` folder allows for easy loading and preprocessing of these datasets for training and evaluation.

#### File Structure

Ensure your dataset directory follows this structure:

```
dataset/
    class_1/
        img1.jpg
        img2.jpg
        ...
    class_2/
        img1.jpg
        img2.jpg
        ...
    ...
```

#### Loading the Dataset

You can use the `CustomDataset` class located in the `scripts` folder to load the datasets. Below is an example of how to use the class:

```
pythonCopy codefrom scripts.custom_dataset import CustomDataset
from torchvision import transforms
from torch.utils.data import DataLoader

# Define dataset transformations (example)
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize images
    transforms.ToTensor(),         # Convert images to tensors
])

# Load the dataset
train_dataset = CustomDataset(root_dir='path_to_training_data', transform=transform)
test_dataset = CustomDataset(root_dir='path_to_test_data', transform=transform)

# Create DataLoader
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=CustomDataset.collate_fn)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False, collate_fn=CustomDataset.collate_fn)
```

#### Key Features of the `CustomDataset` Class

1. **Automatic Class Label Mapping**:
   The `CustomDataset` class automatically assigns a numerical label to each class based on the subdirectory names. This mapping is stored in the `class_to_idx` attribute.
2. **Flexible Transformations**:
   The `transform` parameter allows you to define preprocessing steps (e.g., resizing, normalization) using `torchvision.transforms`.
3. **Collation Function**:
   The `collate_fn` method ensures that images and labels are batched correctly when used with PyTorch's `DataLoader`.

#### Example Workflow

1. Organize your dataset according to the specified structure.
2. Modify the `root_dir` parameter in the `CustomDataset` initialization to point to your dataset's directory.
3. Use the `DataLoader` class to iterate through your dataset efficiently during training or evaluation.

#### Notes

- Ensure all images are in RGB format. The `CustomDataset` class automatically converts grayscale images to RGB.
- The provided `collate_fn` can handle batches effectively but can be customized further if needed.

For further details or troubleshooting, refer to the `custom_dataset.py` script in the `scripts` folder.

