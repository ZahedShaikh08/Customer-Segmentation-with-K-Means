# Customer Segmentation App 🚀

[![Streamlit Version](https://img.shields.io/badge/Streamlit-1.0.0-blue.svg)](https://streamlit.io/) [![Python Version](https://img.shields.io/badge/python-3.8%2B-yellow.svg)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Interactive** K-Means customer segmentation demo built with [Streamlit](https://streamlit.io/).

---

## 📋 Table of Contents
1. [Features](#features)
2. [Demo](#demo)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Deployment](#deployment)
7. [Contributing](#contributing)
8. [License](#license)

---

## 🔥 Features
- **Upload** your CSV or use the default `Mall_Customers.csv` dataset
- **Select** numeric features dynamically via sidebar
- **Adjust** cluster count with a slider
- **Analyze** segmentation with a button click
- **Interactive** 2D scatter plot (zoom, pan, tooltip)
- **Download** the segmented results as CSV

---

## 🛠️ Installation

```bash
# Clone the repo
git clone https://github.com/ZahedShaikh08/Customer-Segmentation-with-K-Means
cd Customer-Segmentation-with-K-Means

# (Optional) Create virtual environment
python -m venv venv            # Windows PowerShell: .\venv\Scripts\Activate.ps1
source venv/bin/activate       # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

> Ensure you have `Mall_Customers.csv` in the root to use as default.

---

## 🚀 Usage

```bash
streamlit run app.py
```

1. **Upload** or use the default dataset.  
2. **Configure** features & cluster count in the sidebar.  
3. Click **Analyze Clustering** to run segmentation.  
4. Explore **Profiles**, **Centers**, and **Visualization**.  
5. Click **Download CSV** to save results.

---

## ⚙️ Configuration
<details>
<summary>Sidebar Options</summary>

- **Select features**: choose at least two numeric columns
- **Number of clusters (k)**: adjust between 2–10
- **Analyze Clustering**: button triggers the pipeline

</details>

---

## ☁️ Deployment

**Streamlit Community Cloud**  
1. Push code to GitHub.  
2. Go to [share.streamlit.io](https://share.streamlit.io/).  
3. Select your repo & `app.py`.  
4. Click **Deploy**.

**Heroku**  
```bash
# Create Procfile
# Procfile: web: streamlit run app.py --server.port $PORT
heroku create your-app-name
git push heroku main
heroku open
```

---

## 🤝 Contributing

Contributions welcome! Please open an issue or submit a pull request.

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
