

# ربات OCR تلگرام

این پروژه یک ربات تلگرامی است که تصاویر ارسالی کاربران را دریافت کرده و با استفاده از موتور **Tesseract OCR** متن موجود در آن را استخراج می‌کند و به کاربر برمی‌گرداند.



## 🧩 پیش‌نیازها

برای اجرای ربات OCR تلگرام، قبل از هر چیز باید موارد زیر را نصب یا آماده کنید:  
1. Python 3.8 یا نسخه‌های بالاتر  
2. Tesseract OCR (موتور تشخیص متن)  
3. توکن ربات تلگرام (از BotFather دریافت می‌شود)  
4. (اختیاری) نصب Git و VS Code برای توسعه و اجرا




## ساختار پروژه

```bash
ocr-telegram-bot/
├── bot.py
├── requirements.txt
├── README.md
└── LICENSE
```


## ⚙️ نصب و اجرای پروژه

برای اجرای ربات OCR تلگرام، مراحل زیر را دنبال کنید:

1. **نصب پایتون و تسرکت (Tesseract OCR):**  
   - از [python.org](https://www.python.org/downloads/) نسخه 3.8 یا بالاتر را نصب کنید.  
   - برنامه‌ی [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) را دانلود و نصب نمایید.  
     سپس مسیر نصب آن را یادداشت کنید (مثلاً:  
     `C:\Program Files\Tesseract-OCR\tesseract.exe`).

2. **نصب کتابخانه‌های مورد نیاز:**  
   در پوشه‌ی پروژه دستور زیر را اجرا کنید:
   ```bash
   pip install -r requirements.txt
