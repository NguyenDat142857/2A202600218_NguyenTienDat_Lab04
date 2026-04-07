# 2A202600218_NguyenTienDat_Lab04
# ✈️ TravelBuddy - AI Travel Planning Assistant

🤖 Một trợ lý du lịch thông minh sử dụng AI để lập kế hoạch chuyến đi tối ưu theo ngân sách.

---

## 📌 Mô Tả Bài Toán

Trong thực tế, việc lên kế hoạch du lịch (chọn chuyến bay, khách sạn, tính toán chi phí) thường mất nhiều thời gian và công sức.  

👉 Bài toán đặt ra:
> Xây dựng một AI Agent có khả năng **tự động lập kế hoạch chuyến đi** dựa trên yêu cầu của người dùng.

Agent cần:
- Hiểu ngôn ngữ tự nhiên (tiếng Việt)
- Tự quyết định gọi tool phù hợp
- Kết hợp nhiều bước (multi-step reasoning)
- Tối ưu chi phí theo ngân sách

---

## 🧠 Giải Pháp

Dự án sử dụng:

- **LangGraph** → xây dựng workflow agent
- **LangChain** → quản lý LLM + tools
- **OpenRouter (Free Model)** → LLM suy luận
- **Tool-based reasoning** → Agent tự gọi function

---

## ⚙️ Kiến Trúc Hệ Thống


User Input
↓
Agent (LLM + Prompt)
↓
Tool Decision
↓
[search_flights] → [search_hotels] → [calculate_budget]
↓
Final Response


---



## 🎯 Tính Năng Chính

### ✈️ 1. Tìm chuyến bay
- Tìm theo tuyến bay
- Chọn phương án rẻ nhất
- Hiển thị giờ bay + hãng + giá

### 🏨 2. Tìm khách sạn
- Lọc theo ngân sách
- Ưu tiên rating cao
- Gợi ý khách sạn tốt nhất

### 💰 3. Tính toán ngân sách
- Tổng hợp chi phí
- So sánh với budget
- Đưa ra tư vấn tối ưu

### 🤖 4. Agent thông minh
- Hiểu tiếng Việt
- Tự động chain nhiều tools
- Không cần user chỉ định từng bước

---

## 📊 Dataset (Mock Data)

Dữ liệu mô phỏng trong `tools.py`:

- ✈️ 5 tuyến bay chính:
  - Hà Nội ↔ Đà Nẵng
  - Hà Nội ↔ Phú Quốc
  - Hà Nội ↔ TP.HCM
  - TP.HCM ↔ Đà Nẵng
  - TP.HCM ↔ Phú Quốc

- 🏨 Khách sạn:
  - 2⭐ → 5⭐
  - Giá: 200k → 3.5 triệu / đêm
  - Có rating & khu vực

---

## 🚀 Cách Cài Đặt

```bash
git clone <your-repo>
cd TravelBuddy

## Tạo môi trường (optional)
python -m venv venv
venv\Scripts\activate   # Windows
Cài dependencies
pip install -r requirements.txt
## 🔐 Cấu hình API

Tạo file .env:

OPENROUTER_API_KEY=your_api_key_here
## ▶️ Chạy chương trình
python agent.py
## 🧪 Demo & Test

Các test được thực hiện thủ công bằng cách chạy:

```bash
python agent.py
