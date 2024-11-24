# MGDNF Datasets

This repository contains the datasets utilized in the MGDNF paper, encompassing the following:

- Yak Individual Category Dataset

- Vehicle Identification Dataset
- Bird Species Dataset

Each dataset is organized into training and testing sets, structured as follows:

## Yak Individual Category Dataset

- Description: Comprises images of 21 distinct yak individuals, each representing a unique category.
- Image Count per Category: Ranges from 140 to 200 images.
- Total Images:
  - Training Set: 2,663 images
  - Test Set: 1,213 images
- Structure:
  - yak/
    - train/
      - individual_01/
      - individual_02/
      - ...
    - test/
      - individual_01/
      - individual_02/
      - ...

## Vehicle Identification Dataset

- Description: Contains images of 10 different vehicle types.
- Total Images:
  - Training Set: 2,200 images
  - Test Set: 1,000 images
- Structure:
  - vehicle_identification/
    - train/
      - type_01/
      - type_02/
      - ...
    - test/
      - type_01/
      - type_02/
      - ...

## Bird Species Dataset

- Description: Features images of 24 bird species.
- Total Images: 5,456
  - Training Set: 3,868 images
  - Test Set: 1,588 images
- Structure:
  - bird_species/
    - train/
      - species_01/
      - species_02/
      - ...
    - test/
      - species_01/
      - species_02/
      - ...

## Usage

1. Cloning the Repository:

   ```bash
   git clone https://github.com/Deep-AI-Application-DAIP/MGDNF-datasets.git
   ```

2. Accessing Datasets:

   Navigate to the respective dataset directories (yak/, vehicle_identification/, bird_species/) to access the training and testing images.

## Citation

If you utilize these datasets in your research, please cite the MGDNF paper accordingly.

## License

These datasets are provided for academic and research purposes. For other uses, please contact the repository maintainers.