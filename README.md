
---

# 📸 Super‑Me Photo AI API

**Learn how to build a generative photo API using Python, FastAPI, Redis, and Replicate.** ([GitHub][1])

An AI‑powered backend that lets you **generate and serve custom photos** using text prompts and generative models. This project demonstrates how to train/run models on Replicate and build a REST API around them.

---

## 🧰 Tech Stack

* **Python 3.13**
* **FastAPI** – API framework
* **Upstash Redis & QStash** – for rate limiting, caching, scheduling ([Upstash](https://upstash.com/?utm_source=cfe))
* **Replicate** – generative AI model hosting ([Finetune model here](https://replicate.com/ostris/flux-dev-lora-trainer/train))
* **Decouple** – environment configuration
* **HTTP clients** (httpx/requests)
* **Streaming Responses** for serving images ([GitHub][1])

---

## 🚀 Features

* Generate photos from text prompts.
* Host and serve generated image files through API endpoints.
* Rate limiting and async support.
* Works with models that can be fine‑tuned for personalized images ([Replicate finetune link](https://replicate.com/ostris/flux-dev-lora-trainer/train))

---

## 📦 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/codingforentrepreneurs/super-me-photo-ai-api .
```

### 2. Create a Python environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
.\venv\Scripts\activate    # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

Create a `.env` file and add your API keys:

```env
REPLICATE_API_TOKEN=your_replicate_token
API_ACCESS_KEY=your_custom_api_key
REDIS_URL=your_redis_url
REPLICATE_MODEL=your_model_name
REPLICATE_MODEL_VERSION=your_model_version
```

### 5. Run the API

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