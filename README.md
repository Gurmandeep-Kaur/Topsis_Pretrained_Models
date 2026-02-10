# Topsis

This repository contains the complete implementation of TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) using my own Python package. The goal is to compare multiple text conversational models using different performance criteria and identify the most suitable model based on overall ranking.

---

## Selected Models, Criteria, and Weights

The following Hugging Face conversational models were considered:
- DialoGPT-small
- DialoGPT-medium
- DialoGPT-large
- BlenderBot-small
- BlenderBot-400M

The criteria used were:
- Quality (Response quality score)
- Latency (Inference time in seconds)
- Model Size (Size of the model in MB)
- Memory (Runtime memory usage in MB)

Quality is treated as a benefit criterion, while latency, model size, and memory are cost criteria. The values considered in the sample data are approximate and derived from Hugging Face documentation and known model characteristics. Exact benchmarking was not performed due to hardware constraints.

The weights used were "4,2,1,1" giving the highest importance to response quality, followed by latency, with model size and memory having lower priority.

---

## Observations

DialoGPT-medium achieved the highest TOPSIS score due to its balanced performance across all criteria. Although BlenderBot-400M has the highest quality, its large size, high latency, and memory usage significantly reduced its overall score. 

---

## Python Package

The complete package can be accessed at https://pypi.org/project/Topsis-Gurmandeep-102303764/
It shall first be installed using the command: 
`pip install Topsis-Gurmandeep-102303764`

Then run the package from the command line: 
`python -m topsis_gurmandeep_102303764.topsis sample_data.csv "4,2,1,1" "+,-,-,-" output.csv`

---

## Author

Gurmandeep Kaur

---

