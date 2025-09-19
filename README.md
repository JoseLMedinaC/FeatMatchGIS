# Semi-Dense Feature Matching

Precise GIS layers are essential for smart-city services and autonomous navigation. However, pedestrian-level assets such as sidewalks and vegetation buffers remain poorly mapped in most urban databases. AI-generated imagery offers a way to complement these datasets, but only if its synthesised views can be accurately aligned. To address this challenge, we introduce a feature-to-feature knowledge distillation (KD) framework that produces an ultra-lightweight neural network (student) capable of extracting semi-dense features from images. These features yield semantically rich keypoint correspondences that support translation, rotation, and scale restoration. The framework distils geometric expertise from a high-capacity teacher into a compact student, built on a Mamba model. Our evaluation focuses on aligning GIS features, covering roads, sidewalks, buildings, and vegetation. The KD-Mamba matcher boosts alignment accuracy and reaches an 86% post-correction similarity rate. The proposed method outperforms classical feature-based baselines, SIFT and ORB, by a wide margin (around 12%). Compared with state-of-the-art deep homography estimators, it achieves similar precision while cutting computational cost by 40%. These gains stem from the model’s ability to capture long-range geometric dependencies with O(N ) complexity. By tightening the spatial registration of AI-generated imagery, our approach enables the reliable fusion of street-level, aerial, and satellite data into coherent pedestrian GIS layers. This paves the way for high-fidelity maps that support next-generation urban applications.
---

## **Contents**

### **Scripts**

1. **`script.py`**:
2. **`final.sh`**:
---

## **Requirements**

### **Dependencies**

- **Python Libraries**:
  - `numpy`
  - `opencv-python`
---
## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
## Further Reading

If you wish to deepen your understanding of **Street-to-GIS generative AI** and **GIS alignment**, consider the following works:

- Zadegan, A. A., Medina, J., & Hadachi, A. (2025). *Street2GIS: Multimodal Generative Framework for Pedestrian Infrastructure Mapping*. In **2025 Joint Urban Remote Sensing Event (JURSE)** (pp. 1–5). IEEE.  
  [BibTeX reference](#bibtex-street2gis)

- Medina, J., Zadegan, A. A., & Hadachi, A. (2025). *Semi-Dense Feature Matching via Mamba-Based Knowledge Distillation*. Accepted at **ICMLA 2025**.  
  [Conference website](https://www.icmla-conference.org/icmla25/)  

---

### References

#### Street2GIS
@inproceedings{zadegan2025street2gis,
  title={Street2GIS: Multimodal Generative Framework for Pedestrian Infrastructure Mapping},
  author={Zadegan, Alireza Akhavi and Medina, Jos{\'e} and Hadachi, Amnir},
  booktitle={2025 Joint Urban Remote Sensing Event (JURSE)},
  pages={1--5},
  year={2025},
  organization={IEEE}
}
@inproceedings{medina2025semidense,
  title={Semi-Dense Feature Matching via Mamba-Based Knowledge Distillation},
  author={Medina, Jos{\'e} and Zadegan, Alireza Akhavi and Hadachi, Amnir},
  booktitle={2025 IEEE International Conference on Machine Learning and Applications (ICMLA)},
  year={2025},
  organization={IEEE}
}


---

## **Acknowledgments**

The authors acknowledge the support of the European Union and Estonian Research Council via project TEM-TA101 and the collaboration project LLTAT21278 with Bolt Technologies.

