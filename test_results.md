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
❌ Test 5 – Guardrail / Refusal (Ngoài phạm vi)

Input:

Giải giúp tôi bài tập lập trình Python về linked list

Console Output:

🧠 Agent đang suy nghĩ...
⚠️ Model không gọi tool (bình thường với free model)

🤖 TravelBuddy:
Xin lỗi, tôi chỉ hỗ trợ các câu hỏi liên quan đến du lịch.
Nếu bạn cần tư vấn về chuyến bay, khách sạn hoặc ngân sách cho chuyến bay