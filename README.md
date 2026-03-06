
# 🐘 Hadoop Pokec Social Network Analysis

<div align="center">

![Hadoop](https://img.shields.io/badge/Apache%20Hadoop-3.3.6-yellow?style=for-the-badge&logo=apache)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![AWS](https://img.shields.io/badge/AWS-EC2-orange?style=for-the-badge&logo=amazon-aws)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Distributed analysis of the Pokec social network dataset using Apache Hadoop MapReduce on a 3-node AWS EC2 cluster**

[Overview](#overview) • [Architecture](#architecture) • [Tasks](#tasks) • [Results](#results) • [Setup](#setup) • [Usage](#usage)

</div>

---

## Overview

This project analyzes the **Pokec social network dataset** — a complete snapshot of a Slovak social network with 1.6 million users and 30 million friend relationships. The analysis is implemented using the **MapReduce paradigm** on a fully distributed 3-node Hadoop cluster deployed on AWS EC2.

The project covers distributed data processing, unsupervised machine learning, supervised ML models, and data visualization — all built from scratch on real cloud infrastructure.

> 📌 **Dataset Source:** [Stanford SNAP — Pokec Social Network](https://snap.stanford.edu/data/soc-Pokec.html)

---

## Architecture

```
┌──────────────────────────────────────────────────────┐
│                  AWS EC2 — t3.small                  │
│                                                      │
│   ┌─────────────┐   ┌──────────┐   ┌──────────┐    │
│   │   MASTER    │   │  SLAVE1  │   │  SLAVE2  │    │
│   │             │   │          │   │          │    │
│   │  NameNode   │   │ DataNode │   │ DataNode │    │
│   │  Resource   │   │  Node    │   │  Node    │    │
│   │  Manager    │   │  Manager │   │  Manager │    │
│   │  Secondary  │   │          │   │          │    │
│   │  NameNode   │   │          │   │          │    │
│   └─────────────┘   └──────────┘   └──────────┘    │
│                                                      │
│   Private Network — SSH Passwordless Authentication  │
└──────────────────────────────────────────────────────┘
```

| Node | Role | Instance Type | RAM |
|------|------|--------------|-----|
| Master | NameNode + ResourceManager | t3.small | 2 GB |
| Slave1 | DataNode + NodeManager | t3.small | 2 GB |
| Slave2 | DataNode + NodeManager | t3.small | 2 GB |

---

## Tasks

### MapReduce Tasks (Hadoop Streaming — Python)

| Task | Description | Output |
|------|-------------|--------|
| **1a** | Most common hobbies — Word frequency count | Top hobbies ranked by count |
| **1b** | Eye color with highest average profile completion | Eye color → avg completion % |
| **1c** | Region with smallest number of users | Region → user count |
| **1d** | Age group distribution | 5 age brackets with user counts |
| **1e** | Least frequent eye color | Eye color → frequency |
| **2** | user_id range and spoken languages analysis | Min/Max ID, top 10 languages |
| **4** | Age-based profile completion segmentation | Age group → avg/min/max completion |
| **5** | User similarity using Cosine Similarity | Most similar user pairs per group |
| **6** | Missing vs present attribute comparison | Avg completion for filled vs empty fields |

### Python Analysis Tasks

| Task | Description | Method |
|------|-------------|--------|
| **3a** | User clustering by age, completion, color | KMeans (k=4) |
| **3b** | Region-based clustering | KMeans (k=3) |
| **7a** | Profile completion vs age | Scatter plot |
| **7b** | Hair color vs eye color distribution | Heatmap |
| **7c** | Languages spoken vs avg completion | Bar chart |
| **8a** | Predict profile completion | Linear Regression |
| **8b** | Predict profile completion | Random Forest Regressor |
| **8c** | Model comparison | RMSE + R2 comparison |

---

## Results

### Task 1a — Most Common Hobbies
```
sportovanie       47
cestovanie        31
hudba             28
kino              24
pocuvanie hudby   21
```

### Task 3 — KMeans Clustering

| Cluster | Count | Avg Age | Avg Completion % |
|---------|-------|---------|-----------------|
| 0 | 70 | 17.64 | 60.71 |
| 1 | 163 | 15.07 | 17.87 |
| 2 | 82 | 19.49 | 61.65 |
| 3 | 185 | 17.54 | 61.78 |

### Task 8 — ML Model Comparison

| Model | RMSE | R2 Score |
|-------|------|----------|
| Linear Regression | 14.78 | 0.5689 |
| **Random Forest** | **12.19** | **0.7068** |

✅ **Random Forest wins** — captures non-linear relationships better in social profile data

**Most important features:**
1. hair_color — 66.85%
2. favourite_color — 16.60%
3. eye_color — 7.02%
4. age — 4.87%
5. region — 3.54%
6. gender — 1.12%

### Task 7 — Visualizations

![Task 7 Plots](results/task7_plots.png)

![Model Comparison](results/task8_comparison.png)

---

## Project Structure

```
hadoop-pokec-analysis/
│
├── README.md
│
├── mapreduce/
│   ├── task1a_mapper.py       # Hobby word count mapper
│   ├── task1a_reducer.py      # Hobby word count reducer
│   ├── task1b_mapper.py       # Eye color completion mapper
│   ├── task1b_reducer.py      # Eye color completion reducer
│   ├── task1c_mapper.py       # Region count mapper
│   ├── task1c_reducer.py      # Region count reducer
│   ├── task1de_mapper.py      # Age groups + eye color mapper
│   ├── task1de_reducer.py     # Age groups + eye color reducer
│   ├── task2_mapper.py        # User ID + languages mapper
│   ├── task2_reducer.py       # User ID + languages reducer
│   ├── task4_mapper.py        # Age segmentation mapper
│   ├── task4_reducer.py       # Age segmentation reducer
│   ├── task5_mapper.py        # Cosine similarity mapper
│   ├── task5_reducer.py       # Cosine similarity reducer
│   ├── task6_mapper.py        # Missing attributes mapper
│   └── task6_reducer.py       # Missing attributes reducer
│
├── analysis/
│   └── tasks_3_7_8.py         # KMeans + Visualizations + ML models
│
├── config/
│   ├── core-site.xml          # HDFS core configuration
│   ├── hdfs-site.xml          # HDFS storage configuration
│   ├── yarn-site.xml          # YARN memory configuration
│   └── mapred-site.xml        # MapReduce configuration
│
└── results/
    ├── task7_plots.png         # 3 visualization plots
    └── task8_comparison.png    # Model comparison chart
```

---

## Setup

### Prerequisites

- 3 AWS EC2 t3.small instances (Ubuntu 22.04 LTS)
- Java 11 OpenJDK
- Apache Hadoop 3.3.6
- Python 3.12

### Step 1 — Install Java (All 3 Nodes)

```bash
sudo apt update -y
sudo apt install -y openjdk-11-jdk
java -version
```

### Step 2 — Create Hadoop User (All 3 Nodes)

```bash
sudo adduser hduser
sudo usermod -aG sudo hduser
echo "hduser ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/hduser
sudo su - hduser
```

### Step 3 — Configure /etc/hosts (All 3 Nodes)

```bash
sudo nano /etc/hosts
# Add:
<MASTER_PRIVATE_IP>   master
<SLAVE1_PRIVATE_IP>   slave1
<SLAVE2_PRIVATE_IP>   slave2
```

### Step 4 — Install Hadoop (All 3 Nodes)

```bash
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xzf hadoop-3.3.6.tar.gz
mv hadoop-3.3.6 hadoop
```

### Step 5 — Setup SSH (Master Only)

```bash
ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa
ssh-copy-id hduser@master
ssh-copy-id hduser@slave1
ssh-copy-id hduser@slave2
```

### Step 6 — Configure and Start Hadoop (Master Only)

```bash
# Format NameNode (only once)
hdfs namenode -format

# Start cluster
start-dfs.sh
start-yarn.sh

# Verify
yarn node -list
# Expected: Total Nodes:2
```

---

## Usage

### Set Streaming JAR

```bash
export SJAR=$(find ~/hadoop -name "hadoop-streaming*.jar" | grep -v sources)
echo $SJAR
```

### Upload Dataset to HDFS

```bash
hdfs dfs -mkdir -p /user/hduser/pokec
hdfs dfs -put pokec_mini.txt /user/hduser/pokec/
```

### Run Any MapReduce Task

```bash
hadoop jar $SJAR \
  -files mapreduce/task1a_mapper.py,mapreduce/task1a_reducer.py \
  -input /user/hduser/pokec/pokec_mini.txt \
  -output /user/hduser/pokec/out_task1a \
  -mapper "python3 task1a_mapper.py" \
  -reducer "python3 task1a_reducer.py"
```

### View Results

```bash
hdfs dfs -cat /user/hduser/pokec/out_task1a/part-* | sort -rn | head -10
```

### Run ML Analysis

```bash
pip3 install pandas matplotlib scikit-learn
python3 analysis/tasks_3_7_8.py
```

---

## Key Learnings

- **Hadoop configuration is strict** — one wrong path in an XML file brings down the entire cluster silently
- **YARN memory is non-negotiable** — t3.micro (1GB) cannot run distributed tasks, t3.small (2GB) works perfectly
- **Test locally first** — `head -5 file.txt | python3 mapper.py` saves hours of debugging
- **Hadoop Streaming flag** — use `-files` not `-file`, call scripts by name not full path

---

## Technologies

![Apache Hadoop](https://img.shields.io/badge/Apache%20Hadoop-3.3.6-yellow?logo=apache)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![AWS EC2](https://img.shields.io/badge/AWS-EC2%20t3.small-orange?logo=amazon-aws)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![matplotlib](https://img.shields.io/badge/matplotlib-3.7-blue)

---

## Author

**Syed Ghani**
- 🔗 LinkedIn: www.linkedin.com/in/syed-ghani-308321287
- 📧 Email: syedghani221@gmail.com

---

<div align="center">

⭐ If you found this useful, please give it a star!

*Cloud Computing Assignment — 2026*

</div>
