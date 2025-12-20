# Ethereum (ETH) Price Prediction Project / Dự Án Dự Đoán Giá ETH

## 🇬🇧 English Version

### Introduction
This project focuses on predicting the Ethereum (ETH) price (specifically the **SMA_20**) using a combination of Technical Indicators (derived from OHLCV data) and On-chain data.

**Project Scope:**
* **Data Period:** January 1, 2022 – December 8, 2025.
* **Feature Selection:** Variance Inflation Factor (VIF) technique is used to select the most relevant features and reduce multicollinearity.
* **Models Used:**
    * **Hybrid Model:** Classification combined with BiLSTM Regression.
    * **GRU Model:** Gated Recurrent Unit.
* **Key Comparisons:**
    1.  **Data Source Efficacy:** Comparing performance using *Technical Indicators Only* vs. *Technical Indicators + On-chain Data*.
    2.  **Model Performance:** Comparing the Hybrid Model (BiLSTM) vs. GRU Model.

### Prerequisites
* Python 3.x
* Jupyter Notebook
* Google Cloud Platform (GCP) Account with **BigQuery Admin** privileges.

### Workflow & Usage Instructions

#### Step 1: Get OHLCV Data
Run the notebook `get_ETH_binance.ipynb`.
* **Action:** Fetches ETH market data from Binance.
* **Output:** Generates the `ETH_dataset.csv` file.

#### Step 2: Google Cloud Environment Setup
To access On-chain data, you must set up your Google Cloud environment.
1.  Create a Google Cloud Project.
2.  Create a Service Account and download the **JSON Key file**.
3.  Grant **BigQuery Admin** permissions to the account.
4.  Create a `.env` file in the root directory containing:
    * `PROJECT_ID`: Your Google Cloud Project ID.
    * `GOOGLE_APPLICATION_CREDENTIALS`: Path to your downloaded JSON key file.

> **Note:** Refer to YouTube tutorials if you are unfamiliar with creating GCP Service Accounts and JSON keys.

#### Step 3: Get On-chain Data
Run the notebook `get_onchain.ipynb`.
* **Action:** Queries BigQuery using the credentials from Step 2.
* **Output:** Generates the `eth_onchain_features.csv` file.

#### Step 4: Merge Datasets
Run the Python script `merge_dataset.py`.
* **Action:** Merges the OHLCV data and On-chain data based on timestamps.
* **Output:** Generates the final `merged_dataset.csv`.

#### Step 5: Feature Selection
Run the notebook `features_selection_vif.ipynb`.
* **Action:** Analyzes the merged dataset to identify high-importance features using VIF.
* **Output:** Note down the listed **important technical indicators** and **important on-chain features**.

#### Step 6: Training & Prediction (Main)
Open the main notebook `ETH_chinh.ipynb`.
1.  **Update Configuration:**
    * Locate the variable `onchain_cols` and update it with the important **on-chain features** found in Step 5.
    * Locate the variable `base_features` and update it with the important **technical indicators** found in Step 5.
2.  **Run the Notebook:** Execute all cells.
3.  **Analyze Results:** The notebook will output the predictions and perform the comparisons between models (Hybrid vs. GRU) and data strategies (With vs. Without On-chain data).

---

## 🇻🇳 Vietnamese Version

### Giới thiệu
Đây là dự án dự đoán giá Ethereum (ETH) - cụ thể là chỉ báo **SMA_20** - dựa trên sự kết hợp giữa các chỉ báo kỹ thuật (được tạo từ dữ liệu OHLCV) và dữ liệu On-chain.

**Phạm vi dự án:**
* **Thời gian dữ liệu:** Từ 01/01/2022 đến 08/12/2025.
* **Lựa chọn đặc trưng:** Sử dụng kỹ thuật VIF (Variance Inflation Factor) để loại bỏ đa cộng tuyến và chọn lọc đặc trưng.
* **Mô hình sử dụng:**
    * **Mô hình Hybrid:** Kết hợp phân loại và hồi quy BiLSTM.
    * **Mô hình GRU:** Gated Recurrent Unit.
* **Mục tiêu so sánh:**
    1.  Hiệu quả giữa việc dùng *Chỉ dữ liệu kỹ thuật* so với *Dữ liệu kỹ thuật + On-chain*.
    2.  Hiệu suất giữa hai mô hình: Hybrid (BiLSTM) và GRU.

### Yêu cầu cài đặt
* Python 3.x
* Jupyter Notebook
* Tài khoản Google Cloud Platform (GCP) với quyền **BigQuery Admin**.

### Hướng dẫn sử dụng chi tiết

#### Bước 1: Thu thập dữ liệu OHLCV
Chạy file notebook `get_ETH_binance.ipynb`.
* **Hành động:** Tải dữ liệu giao dịch ETH từ Binance.
* **Kết quả:** Tạo ra file `ETH_dataset.csv`.

#### Bước 2: Cấu hình môi trường Google Cloud
Để lấy dữ liệu On-chain, bạn cần thiết lập môi trường Google Cloud.
1.  Tạo Google Cloud Project.
2.  Tạo Service Account và tải về file **JSON Key**.
3.  Cấp quyền **BigQuery Admin** cho tài khoản này.
4.  Tạo file `.env` chứa các thông tin sau:
    * `PROJECT_ID`: ID dự án Google Cloud của bạn.
    * `GOOGLE_APPLICATION_CREDENTIALS`: Đường dẫn tới file JSON key vừa tải.

> **Lưu ý:** Nếu chưa biết cách lấy file JSON và cấp quyền, bạn có thể xem hướng dẫn trên YouTube về "Google Cloud BigQuery Service Account".

#### Bước 3: Thu thập dữ liệu On-chain
Chạy file notebook `get_onchain.ipynb`.
* **Hành động:** Truy vấn dữ liệu từ BigQuery dựa trên cấu hình ở Bước 2.
* **Kết quả:** Tạo ra file `eth_onchain_features.csv`.

#### Bước 4: Gộp dữ liệu
Chạy file python `merge_dataset.py`.
* **Hành động:** Gộp file dữ liệu giá và dữ liệu on-chain thành một dataset duy nhất.
* **Kết quả:** Tạo ra file `merged_dataset.csv`.

#### Bước 5: Lựa chọn đặc trưng (Feature Selection)
Chạy file notebook `features_selection_vif.ipynb`.
* **Hành động:** Phân tích độ quan trọng của các đặc trưng.
* **Kết quả:** Bạn sẽ nhận được danh sách các **chỉ báo kỹ thuật quan trọng** và **đặc trưng on-chain quan trọng**. Hãy ghi nhớ hoặc copy danh sách này.

#### Bước 6: Huấn luyện và Dự đoán (File Chính)
Mở file notebook `ETH_chinh.ipynb`.
1.  **Cập nhật cấu hình:**
    * Tìm biến `onchain_cols`: Sửa lại danh sách này dựa trên các đặc trưng on-chain quan trọng tìm được ở Bước 5.
    * Tìm biến `base_features`: Sửa lại danh sách này dựa trên các chỉ báo kỹ thuật quan trọng tìm được ở Bước 5.
2.  **Chạy toàn bộ:** Thực thi tất cả các cell trong notebook.
3.  **Xem kết quả:** Hệ thống sẽ tiến hành huấn luyện, dự đoán và đưa ra các bảng so sánh hiệu suất giữa các mô hình và các chiến lược dữ liệu.
