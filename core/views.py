from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from .models import Flight, Feedback
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def search_flights(request):
    query = request.GET.get('q', '')
    results = Flight.objects.filter(
        Q(destination_city__icontains=query) | Q(departure_city__icontains=query)
    ) if query else []
    return render(request, 'search_results.html', {'results': results, 'query': query})

def send_feedback(request):
    if request.method == "POST":
        Feedback.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        messages.success(request, "Cảm ơn bạn! Phản hồi đã được gửi thành công.")
        return redirect('home')
    return redirect('home')

def web_generator_page(request):
    return render(request, 'web_generator.html')

# core/views.py

def api_generate_web(request):
    if request.method == "POST":
        topic = request.POST.get('topic')
        api_key = os.getenv("GEMINI_API_KEY")
        print(f"--- DEBUG KEY: {api_key[:10] if api_key else 'KEY TRỐNG RỖNG!'} ---")
        genai.configure(api_key=api_key)
        
        try:
            available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            if not available_models:
                return JsonResponse({'error': 'Không tìm thấy model nào khả dụng cho Key này'}, status=404)
            selected_model = next((m for m in available_models if 'flash' in m), available_models[0])
            model = genai.GenerativeModel(
                model_name=selected_model, 
                system_instruction=(
                    "Bạn là chuyên gia thiết kế Website. Hãy tạo 1 trang HTML5 hoàn chỉnh "
                    "dùng Tailwind CSS. Website PHẢI CÓ: Header, Form Đăng nhập (Username/Password), "
                    "và nội dung đặc trưng của chủ đề. CHỈ TRẢ VỀ CODE TRONG CẶP THẺ <html>. KHÔNG GIẢI THÍCH."
                )
            )
            
            response = model.generate_content(f"Tạo website về chủ đề: {topic}")
            
            # Xử lý lấy code sạch
            full_text = response.text
            clean_code = full_text.replace('```html', '').replace('```', '').strip()
            
            return JsonResponse({'html_code': clean_code})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)