# GGDrive2Kaggle
GGDrive2Kaggle is a lightweight and efficient utility designed to automate the process of uploading datasets from Google Drive to Kaggle.

> Automate your data uploads. From Drive to Kaggle, effortlessly. 🚀

**GGDrive2Kaggle** is a lightweight and efficient utility designed to automate the process of uploading datasets from **Google Drive** to **Kaggle**.

Whether you're preparing data for a competition, publishing a research dataset, or managing a private dataset pipeline, this tool helps you skip the manual steps and push data directly from your Drive to your Kaggle account.

---

## 🔧 Features

- 📁 Pull files directly from Google Drive (via file ID or public link).
- 🧠 Automatically create or update Kaggle datasets.
- ⚡ Fast and easy to use — no manual uploads required.
- 🛠️ Ideal for competitions, research, or automated pipelines.

---

## 📦 Requirements

- Python 3.7+
- Kaggle API credentials (`kaggle.json`)
- Google Drive file ID or shareable link

Install dependencies:
```bash
pip install -r requirements.txt
```

## 🔐 Setup

  1. Get Kaggle API credentials
     
      - Go to Kaggle Account Settings
      
      - Click "Create New API Token"
      
      - A file named kaggle.json will be downloaded
      
      - Place it in the root folder of the project or in ~/.kaggle/kaggle.json

  3. Authenticate Google Drive (if needed)
      - If using PyDrive or other libraries that require OAuth, follow their auth flow. If accessing public files via direct ID, this may not be necessary.


## 🚀 Usage

  - Upload a file from Google Drive to Kaggle:
  ```bash
  python ggdrive2kaggle.py \
  --gdrive-id <GOOGLE_DRIVE_FILE_ID> \
  --dataset <USERNAME/DATASET_SLUG> \
  --title "My Dataset Title" \
  --description "A brief description of the dataset." \
  --folder "my-dataset-folder"
  ```

## 📁 Example
  ```bash
  python ggdrive2kaggle.py \
  --gdrive-id 1a2b3c4d5e6f7g8h9i \
  --dataset yourusername/awesome-dataset \
  --title "Awesome Dataset" \
  --description "This dataset contains awesome stuff." \
  --folder "./data"
  ```

## 📌 Notes
  - Kaggle API has a rate limit — avoid uploading too frequently.
  - If dataset already exists, make sure you're the owner, or the update will fail.
  - For large files, make sure Kaggle supports the upload size.

## 📄 License
This project is licensed under the MIT License.

## 🤝 Contributing
Pull requests are welcome! If you’d like to add features or improve the tool, feel free to fork and submit a PR.

## 🙌 Acknowledgments
  - Kaggle API
  - Google Drive API
