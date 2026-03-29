import os
import google.generativeai as genai
from django.http import JsonResponse
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
def chat_with_gemini(request):
    if request.method == "POST":
        user_message = request.POST.get('message', '')
        
        try:
            available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            if not available_models:
                return JsonResponse({'error': 'Không tìm thấy model nào khả dụng cho Key này'}, status=404)
            
            selected_model = next((m for m in available_models if 'flash' in m), available_models[0])
            model = genai.GenerativeModel(
                model_name=selected_model,
                system_instruction="Bạn là trợ lý ảo chuyên nghiệp của hãng hàng không Skyline Airlines. "
                                   "Nhiệm vụ của bạn là hỗ trợ khách hàng giải đáp các thắc mắc về chuyến bay, "
                                   "thủ tục check-in, hành lý và các chương trình khuyến mãi. "
                                   "Hãy trả lời một cách lịch sự, thân thiện và luôn xưng hô là 'Skyline AI' hoặc 'Trợ lý Skyline'. "
                                   "Chỉ trả lời các nội dung liên quan đến hàng không và du lịch bằng tiếng Việt."
            )
            response = model.generate_content(user_message)
            
            return JsonResponse({'reply': response.text})
            
        except Exception as e:
            return JsonResponse({'error': f"Lỗi: {str(e)} | Model định dùng: {selected_model if 'selected_model' in locals() else 'N/A'}"}, status=500)