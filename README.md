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
[test_results.md](test_results.md)


### ✅ Test 1 – Direct Answer (Không dùng tool)

Bạn: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu
TravelBuddy: Chào bạn! Mình là TravelBuddy, rất vui được đồng hành cùng bạn lên kế hoạch cho chuyến đi sắp tới 🌴✨
Để mình có thể tìm vé máy bay, gợi ý khách sạn phù hợp và tính toán chi phí chính xác nhất, bạn vui lòng chia sẻ thêm một vài thông tin nhé:    
- 👥 Chuyến đi có bao nhiêu người?
Nếu bạn chưa có ý tưởng cụ thể, mình có thể gợi ý nhanh một số điểm đến "hot" tại Việt Nam như: Đà Nẵng – Hội An, Đà Lạt, Nha Trang, Phú Quốc, Sapa hay Hà Nội – Ninh Bình. Bạn thích phong cách nào nhất? Cứ nhắn mình nhé, mình sẽ hỗ trợ tìm vé, tính ngân sách và đặt khách sạn ngay! 😊

  
---
### ✅ Test 2 – Single Tool Call (Search Flights)

Bạn: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng
Gọi tool: search_flights ({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
TravelBuddy: ✈️ Chuyến bay:
Dưới đây là các chuyến bay từ Hà Nội đi Đà Nẵng:
- VietJet Air: 890.000₫
- Bamboo Airways: 1.200.000₫
- Vietnam Airlines: 1.450.000₫
- Vietnam Airlines: 2.800.000₫
Bạn có muốn mình tìm thêm khách sạn tại Đà Nẵng hoặc tính toán chi phí cho chuyến đi không? Nếu có, hãy cho mình biết tổng ngân sách và các khoản chi tiêu dự kiến nhé!


---
### ✅ Test 3 – Multi-step Tool Usage (Flights + Hotels + Budget)

Bạn: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

🧠 Agent đang suy nghĩ...
🛠 Tool: search_flights | args: {'origin': 'Hà N
ội', 'destination': 'Phú Quốc'}

🧠 Agent đang suy nghĩ...
🛠 Tool: search_hotels | args: {'city': 'Phú Quố
c', 'max_price_per_night': 1500000}

🧠 Agent đang suy nghĩ...
⚠️ Model không gọi tool (bình thường với free model)
🤖 TravelBuddy: **✈️ Chuyến bay**  
- **VietJet Air** 16:00 → 18:15 | **1.100.000₫** (tốt nhất)  

**🏨 Khách sạn (Phú Quốc, 2 đêm, ≤ 1.500.000₫/đêm)**  
- **9Station Hostel** 2⭐ | 200.000₫/đêm | ⭐4.5  

**💰 Chi phí**
- Vé máy bay (khứ hồi): 1.100.000₫ × 2 = **2.200.000₫**
- Khách sạn: 200.000₫ × 2 đêm = **400.000₫**
- **Tổng dự kiến:** **2.600.000₫**

**📊 Còn lại**
- Ngân sách 5.000.000₫ – 2.600.000₫ = **2.400.000₫**

**💡 Gợi ý**
- Với ngân sách còn lại, bạn có thể nâng cấp khách sạn (ví dụ Sol by Meliá 1.500.000₫/đêm) hoặc dùng để chi tiêu ăn uống, tham quan.
- Nếu muốn vé rẻ hơn, có thể chọn chuyến VietJet 10:00 → 12:15 (1.350.000₫) và so sánh. 

---
### ✅ Test 4 – Missing Information (Clarification)

Bạn: Tôi muốn đặt khách sạn

🧠 Agent đang suy nghĩ...
⚠️ Model không gọi tool (bình thường với free model)
🤖 TravelBuddy: 🏨 **Khách sạn đề xuất:** 9Station Hostel (2⭐) – 200.000₫/đêm, ⭐4.5  

Bạn muốn xác nhận đặt phòng 2 đêm tại **9Station Hostel** cho chuyến đi Phú Quốc không? Nếu có yêu cầu khác (thay đổi khách sạn, ngày nhận/trả phòng, hoặc thêm dịch vụ), vui lòng cho tôi biết.


---
### ✅ Test 5 – Guardrail / Refusal (Ngoài phạm vi)

Bạn: Giải giúp tôi bài tập lập trình Python về linked list

🧠 Agent đang suy nghĩ...
⚠️ Model không gọi tool (bình thường với free model)
🤖 TravelBuddy: Xin lỗi, tôi chỉ hỗ trợ các câu hỏi liên quan đến du lịch. Nếu bạn cần tư vấn về chuyến bay, khách sạn hoặc ngân sách cho chuyến đi, mình rất sẵn lòng giúp đỡ!



## 👨‍💻 Thông Tin Tác Giả

**Sinh viên**: 2A202600218_Nguyễn Tiến Đạt  
**Khóa học**: AI in Action - Day 4  
**Thời gian**: 07 April 2026

