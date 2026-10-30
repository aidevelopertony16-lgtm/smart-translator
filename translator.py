import os
from google import genai
from google.colab import userdata

# 1. حل مشكلة الحروف العربية
os.environ["PYTHONIOENCODING"] = "utf-8"

# 2. جلب المفتاح بأمان (ملاحظة: هذا الكود مخصص لبيئة Google Colab)
api_key = userdata.get('GEMINI_API_KEY').strip().split()[0]
client = genai.Client(api_key=api_key)

print("🌟 مرحباً بك في المترجم الذكي! (اكتب 'خروج' للإنهاء)")

while True:
    text = input("\nاكتب الجملة بالعربية: ")
    
    if text == "خروج" or text == "exit":
        print("إلى اللقاء! 👋")
        break
        
    prompt = f"Translate this Arabic text to English. Provide only the translation: {text}"
    
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash", 
            contents=prompt,
        )
        print("الترجمة:", response.text)
    except Exception as e:
        print(f"عذراً، حدث خطأ: {e}")
