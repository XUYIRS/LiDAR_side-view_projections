## **Chapter3 - Identifying tree species using deep learning and side-view projections**

---

### 📝 Introduction

This repository provides a complete pipeline for processing individual tree LiDAR point clouds and classifying tree species using deep learning. It combines side-view image generation and a tailored convolutional neural network (EfficientNet_S_V2) to identify tree species in urban environments. The workflow is designed for flexibility and reproducibility, and it supports both research and practical applications in urban forestry, remote sensing, and ecological monitoring.

### 🛰️ The Challenge: Optimizing Deep Learning Projections for Sparse LiDAR

The utility of side-view projections for tree species classification using lower-density airborne LiDAR (~20 pts/m²) remains underexplored. Several key limitations arise when translating this method from high-precision LiDAR to broader-scale, lower-density datasets:

1. **Uncertain projection requirements**: Prior studies often select the number of side views arbitrarily, with little regard for computational cost or accuracy trade-offs.
2. **Incomplete feature representation**: Side views alone may not capture all distinguishing traits of tree species, especially when the LiDAR lacks detail.
3. **Limited comparative evaluation**: It is unclear how side-view CNNs compare to traditional machine learning models across different sample sizes or in geographically diverse test areas.
4. **Scalability concerns**: Most methods are tailored to site-specific conditions or high-resolution data, challenging their broader applicability in national or urban tree inventories.

Together, these challenges constrain the scalability and efficiency of LiDAR-based species classification methods and limit their relevance for operational use.

------

### 🧪The Solution: A Refined and Scalable Side-View CNN Approach

This study proposes a refined deep learning pipeline tailored for lower-density airborne LiDAR data, specifically addressing the above challenges. The approach includes the following innovations:

- **Systematic evaluation of projection quantity**: By empirically testing multiple configurations, we identify 12 side-view projections as the optimal number for balancing accuracy and efficiency. This avoids arbitrary selection and ensures consistent model performance.
- **Integration of height and intensity information**: Beyond geometric structure, we incorporate LiDAR-derived height and intensity channels into the projection images. While height marginally improves classification (F1 gain: 0.14%), intensity substantially enhances accuracy, raising the F1-score by 3.96% *(p < 0.001)*.
- **Robust benchmarking against traditional methods**: We compare CNN-based models with random forests and other classical classifiers, revealing that deep learning consistently achieves higher accuracy and better spatial transferability, especially with larger training datasets.
- **Demonstrated generalizability**: Using English oak (*Quercus robur L.*) across multiple Dutch cities, we validate that our method performs well across diverse urban forest settings, overcoming data sparsity and structural similarity among species.

------

### 📁 Repository Structure

#### 0. Environment Setup

- **File**: `requirements.txt`

- **Purpose**: Lists all required Python packages and versions needed to run the scripts and notebooks. Enables users to replicate the environment quickly using tools like `pip` or `conda`.

- **Example usage**:

  ```bash
  pip install -r requirements.txt  
  ```

#### 1. LiDAR Metric Computation

- **Folder**: `LiDAR_metrics/`
- **Purpose**: Contains Python scripts and helper functions for computing a suite of LiDAR-derived structural metrics relevant to individual trees or forest patches.
- **Inputs**:
  - Normalized LiDAR point clouds (`*.las` or `*.laz`)
  - Bounding boxes representing the crowns of individual trees (`*.shp` or `*.geojson`)
- **Outputs**:
  - Metric tables in CSV format (e.g., height percentiles, canopy density, vertical distribution profiles)

#### 2. Example Data

- **Folder**: `example_data/`
- **Purpose**: Provides a small set of LiDAR point cloud data for testing and demonstration of workflows.
- **Contents**:
  - Individual tree point clouds in `.las` format
  - Bounding boxes of individual trees in `.geojson` format

#### 3. Tree Point Cloud Processing

- **Script**: `process_tree.py`
- **Purpose**: Process individual tree-level LiDAR point clouds to generate 2D side-view projections for deep learning applications.
- **Inputs**:
  - Tree point clouds (`*.las`)
- **Outputs**:
  - Side-view images (`*.png`) representing the vertical profile of each tree

#### 4. Model Training: Tree Species Classification

- **Notebook**: `Training.ipynb`
- **Purpose**: Train an EfficientNet_S_V2 convolutional neural network on side-view LiDAR projections to classify tree species.
- **Inputs**:
  - Side-view projection images (`*.png`)
  - Species labels (`*.csv`)
- **Outputs**:
  - Trained model checkpoints (`*.pl`)
  - Training logs and performance metrics (accuracy, loss)

#### 5. Model Prediction

- **Notebook**: `Prediction.ipynb`
- **Purpose**: Apply the trained EfficientNet_S_V2 model to new side-view projections for tree species identification.
- **Inputs**:
  - Side-view images (`*.png`)
  - Trained model weights
- **Outputs**:
  - Predicted species labels and confidence scores (`*.csv`)

#### 6. Workflow Tutorial

- **Notebook**: `Tutorial.ipynb`

- **Purpose**: Show how to generate side-view projections from raw LiDAR point cloud data.

- **Inputs**:

  - Tree point clouds (`*.las`)
  - Bounding boxes of individual trees  (`*.geojson`)

- **Outputs**:

  - Side-view images (`*.png`)

   



