
---

````markdown
# 📸 RepliFace: AI Photo Generator

**Learn how to build a generative photo API using Python, FastAPI, Redis, and Replicate.**

An AI-powered backend that lets you **generate and serve custom photos** using text prompts and generative models.  
This project demonstrates how to train/run models on Replicate and build a REST API around them.

---

## 🧰 Tech Stack

- **Python 3.13**
- **FastAPI** – API framework
- **Upstash Redis & QStash** – for rate limiting, caching, scheduling  
  ([Upstash](https://upstash.com/?utm_source=cfe))
- **Replicate** – generative AI model hosting  
  ([Finetune model here](https://replicate.com/ostris/flux-dev-lora-trainer/train))
- **Decouple** – environment configuration
- **HTTP clients** (`httpx` / `requests`)
- **Streaming Responses** – for serving images

---

## 🚀 Features

- Generate photos from text prompts.
- Host and serve generated image files through API endpoints.
- Rate limiting and async support.
- Works with models that can be fine-tuned for personalized images.

---

## 📦 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Madhusanka-slc/photo_generator.git .
````

---

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate it:

```bash
# macOS / Linux
source venv/bin/activate

# Windows
.\venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Prepare Your Images & Run Pipeline

#### 🔹 Place Your Images Inside:

```
data/inputs/
```

#### 🔹 Run the Pipeline:

```bash
python scripts/run_pipeline.py
```

This will:

* Create dataset zip
* Validate images
* Optimize images
* Generate final zip in `data/outputs/`

---

#### 🔹 Use the Zipped Images

Use the generated dataset zip file inside `data/outputs/`
to train your model in **Replicate**.

---

### 5️⃣ Configure Environment Variables

Create a `.env` file and add your credentials:

```env
REPLICATE_API_TOKEN=your_replicate_token
API_ACCESS_KEY=your_custom_api_key
REDIS_URL=your_redis_url
REPLICATE_MODEL=your_model_name
REPLICATE_MODEL_VERSION=your_model_version
```

---

### 6️⃣ Run the API

```bash
uvicorn main:app --reload
```

Your API will be available at:

```
http://127.0.0.1:8000
```

---

## 📝 Example Endpoints

| Method | Route                                 | Description                   |
| ------ | ------------------------------------- | ----------------------------- |
| POST   | `/generate`                           | Generate images from a prompt |
| GET    | `/predictions`                        | List predictions              |
| GET    | `/predictions/{id}`                   | Get prediction details        |
| GET    | `/predictions/{id}/files/{index}.jpg` | Retrieve output image         |

---

```

