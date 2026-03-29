# Skyline - Flight Booking & AI Chatbot

Dự án mô phỏng hệ thống tìm kiếm, đặt vé máy bay trực tuyến có tích hợp Trợ lý ảo AI, được đóng gói hoàn toàn bằng Docker.

## 🛠 Công nghệ sử dụng
* **Backend:** Python, Django
* **Frontend:** HTML, TailwindCSS
* **Database:** SQLite3
* **AI:** Google Gemini API
* **Deploy:** Docker

## Hướng dẫn chạy dự án (Chỉ cần cài Docker)

**
1. git clone https://github.com/MatthewLK13/Airplane-Booking-Django-Webapp.git
2. Create a .env file in the root directory based on the provided example and add your Gemini API key:
GEMINI_API_KEY=your_google_gemini_api_key_here
```bash

3. Khởi động server:
  Mở docker Desktop App
  Mở terminal ngay tại thư mục chưa src:
  chạy:
  docker build -t airline .
  docker run -p 8000:8000 airline
  Mở trình duyệt và truy cập: http://localhost:8000
