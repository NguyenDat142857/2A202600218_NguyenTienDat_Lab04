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

 **Cài đặt dependencies**
   ```bash
   pip install -r requirements.txt
   ```

 **Cấu hình biến môi trường**
   
   Tạo file `.env` trong thư mục gốc dự án:
   ```env
   llm = ChatOpenAI(
    model="openai/gpt-oss-120b:free",  # 🔥 MODEL MỚI
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.3,
)
   ```

### Chạy Agent

```bash
python agent.py
```


👉 Kết quả được lưu tại:
### 
test_results.md


### ✅ Test 1 – Direct Answer (Không dùng tool)

🔹 Input

Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu

🔹 Console Output

🤖 TravelBuddy:
Chào bạn! Mình là TravelBuddy, rất vui được đồng hành cùng bạn lên kế hoạch cho chuyến đi sắp tới 🌴✨

- 👥 Chuyến đi có bao nhiêu người?
- Gợi ý: Đà Nẵng, Đà Lạt, Phú Quốc, Sapa...
  
---
### ✅ Test 2 – Single Tool Call (Search Flights)

🔹 Input

Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

🔹 Console Output

🧠 Agent đang suy nghĩ...
🛠 Tool: search_flights | args: {'origin': 'Hà Nội', 'destination': 'Đà Nẵng'}

🤖 TravelBuddy:
✈️ Chuyến bay:
- VietJet Air: 890.000₫
- Bamboo Airways: 1.200.000₫
- Vietnam Airlines: 1.450.000₫

---
### ✅ Test 3 – Multi-step Tool Usage (Flights + Hotels + Budget)

🔹 Input

Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

🔹 Console Output

🧠 Agent đang suy nghĩ...
🛠 Tool: search_flights
🛠 Tool: search_hotels

🤖 TravelBuddy:
✈️ Vé: 2.200.000₫
🏨 Khách sạn: 400.000₫
💰 Tổng: 2.600.000₫
📊 Còn lại: 2.400.000₫

---
### ✅ Test 4 – Missing Information (Clarification)

🔹 Input

Tôi muốn đặt khách sạn

🔹 Console Output

🤖 TravelBuddy:
🏨 9Station Hostel – 200.000₫/đêm

Bạn muốn đặt 2 đêm không?

---
### ✅ Test 5 – Guardrail / Refusal (Ngoài phạm vi)

🔹 Input

Giải giúp tôi bài tập lập trình Python về linked list

🔹 Console Output

🤖 TravelBuddy:
Xin lỗi, tôi chỉ hỗ trợ các câu hỏi liên quan đến du lịch.


## 👨‍💻 Thông Tin Tác Giả

**Sinh viên**: 2A202600218_Nguyễn Tiến Đạt  
**Khóa học**: AI in Action - Day 4  
**Thời gian**: 07 April 2026

