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

 **Tạo virtual environment (tùy chọn)**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

 **Cài đặt dependencies**
   ```bash
   pip install -r requirements.txt
   ```

 **Cấu hình biến môi trường**
   
   Tạo file `.env` trong thư mục gốc dự án:
   ```env
   OLLAMA_BASE_URL=https://kelkoo-her-murphy-rank.trycloudflare.com/v1
   MODEL_NAME=llama3.1:8b
   OLLAMA_API_KEY=your_api_key_here
   ```

### Chạy Agent

```bash
python agent.py
```


👉 Kết quả được lưu tại:

test_results.md
🧪 Demo Kết Quả

👉 Xem chi tiết tại: test_results.md

Preview:

✅ Test 1 – Direct Answer (Không dùng tool)

Input:

Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu

Console Output:

🤖 TravelBuddy:
Chào bạn! Mình là TravelBuddy, rất vui được đồng hành cùng bạn lên kế hoạch cho chuyến đi sắp tới 🌴✨

Để mình có thể tìm vé máy bay, gợi ý khách sạn phù hợp và tính toán chi phí chính xác nhất, bạn vui lòng chia sẻ thêm một vài thông tin nhé:
- 👥 Chuyến đi có bao nhiêu người?

Nếu bạn chưa có ý tưởng cụ thể, mình có thể gợi ý nhanh một số điểm đến "hot" tại Việt Nam như:
Đà Nẵng – Hội An, Đà Lạt, Nha Trang, Phú Quốc, Sapa hay Hà Nội – Ninh Bình.

Bạn thích phong cách nào nhất? 😊

✅ Test 2 – Single Tool Call (Search Flights)

Input:

Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

Console Output:

🧠 Agent đang suy nghĩ...
🛠 Tool: search_flights | args: {'origin': 'Hà Nội', 'destination': 'Đà Nẵng'}

🤖 TravelBuddy:
✈️ Chuyến bay:
- VietJet Air: 890.000₫
- Bamboo Airways: 1.200.000₫
- Vietnam Airlines: 1.450.000₫
- Vietnam Airlines: 2.800.000₫

Bạn có muốn mình tìm thêm khách sạn tại Đà Nẵng không?

✅ Test 3 – Multi-step Tool Usage (Flights + Hotels + Budget)

Input:

Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

Console Output:

🧠 Agent đang suy nghĩ...
🛠 Tool: search_flights | args: {'origin': 'Hà Nội', 'destination': 'Phú Quốc'}

🧠 Agent đang suy nghĩ...
🛠 Tool: search_hotels | args: {'city': 'Phú Quốc', 'max_price_per_night': 1500000}

⚠️ Model không gọi tool (bình thường với free model)

🤖 TravelBuddy:
✈️ Chuyến bay:
- VietJet Air 16:00 → 18:15 | 1.100.000₫

🏨 Khách sạn:
- 9Station Hostel – 200.000₫/đêm

💰 Chi phí:
- Vé máy bay: 2.200.000₫
- Khách sạn: 400.000₫
👉 Tổng: 2.600.000₫

📊 Còn lại:
5.000.000₫ – 2.600.000₫ = 2.400.000₫

💡 Gợi ý:
Bạn có thể nâng cấp khách sạn hoặc dùng phần còn lại cho ăn uống và tham quan.

✅ Test 4 – Missing Information (Clarification)

Input:

Tôi muốn đặt khách sạn

Console Output:

🧠 Agent đang suy nghĩ...
⚠️ Model không gọi tool (bình thường với free model)

🤖 TravelBuddy:
🏨 Khách sạn đề xuất:
- 9Station Hostel – 200.000₫/đêm

Bạn muốn xác nhận đặt phòng 2 đêm tại khách sạn này không?
Nếu có thay đổi về ngày hoặc khách sạn, hãy cho mình biết nhé!

✅ Test 5 – Guardrail / Refusal (Ngoài phạm vi)

Input:

Giải giúp tôi bài tập lập trình Python về linked list

Console Output:

🧠 Agent đang suy nghĩ...
⚠️ Model không gọi tool (bình thường với free model)

🤖 TravelBuddy:
Xin lỗi, tôi chỉ hỗ trợ các câu hỏi liên quan đến du lịch.
Nếu bạn cần tư vấn về chuyến bay, khách sạn hoặc ngân sách cho chuy
