# MinIO test with boto3
This script demonstrates how to connect to a MinIO server using the boto3 library in Python
and perform basic operations like listing buckets.

# MinIO Setup
- Install MinIO server:
  ```bash
    wget https://dl.min.io/server/minio/release/linux-amd64/archive/minio_20250613113347.0.0_amd64.deb -O minio.deb
    sudo dpkg -i minio.deb
  ```
- Create a directory for MinIO data:
  ```bash
  mkdir ~/minio
  ```
- Run MioIO server:
  ```bash
  minio server ~/minio --console-address ":9001"
  ```

# Requirements
- Python 3.x
- Install dependencies using pip:
  ```bash
  pip3 install -r requirements.txt
  ```

# Usage
1. Environment variable file settings:
    - Create env file
        ```bash
        sudo vi /etc/default/minio
        ```
    - Set the following user variables:
        ```bash
        MINIO_ROOT_USER=minioadmin
        MINIO_ROOT_PASSWORD=minioadmin
        ```
    - Set the following volumes variables:
        ```bash
        MINIO_VOLUMES="/home/technonia/minio"
        ```
2. Register the MinIO service:
    - Create a service file
        ```bash
        sudo vi /etc/systemd/system/minio.service
        ```

3. Run the following commands to start the MinIO service:
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable minio.service
    sudo systemctl start minio.service
    ```
4. Run the Python script:
    ```bash
    python3 main.py
    ```
5. Check the MinIO web interface:
    - Open your web browser and go to `http://localhost:9001`