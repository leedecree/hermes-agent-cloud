# 🛰️ Hermes Agent Cloud (Free 24/7 Deployment)

یک نسخه سبک و کانتینری از **Hermes Agent** طراحی شده برای اجرا روی سرویس‌های ابری رایگان مانند **Render** و **Koyeb** متصل به تلگرام با Keep-Alive ضدخواب.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/leedecree/hermes-agent-cloud)

---

## ⚡ امکانات

- 🚀 **رایگان بدون نیاز به کارت بانکی:** بدون نیاز به کردیت کارت بین‌المللی
- 🤖 **متصل به تلگرام:** کنترل کامل ایجنت هرمس از طریق بات تلگرام شخصی
- 🛡️ **امنیت بالا:** قفل شده روی آی‌دی عددی شما (`TELEGRAM_ALLOWED_USERS`)
- 💓 **Keep-Alive وب‌سرور:** مجهز به اندپوینت `/healthz` برای بیدار ماندن دائمی روی Render
- 🧠 **پشتیبانی از مدل‌های رایگان و پرسرعت:** Google Gemini 2.5 Flash / Groq / OpenRouter

---

## 🛠️ راهنمای دیپلوی سریع روی Render (با ۱ کلیک)

1. روی دکمه آبی بالای صفحه (**Deploy to Render**) کلیک کنید یا وارد لینک زیر شوید:  
   👉 **[دیپلوی مستقیم در Render](https://render.com/deploy?repo=https://github.com/leedecree/hermes-agent-cloud)**
2. با اکانت گیت‌هاب وارد شوید (نیازی به کارت بانکی نیست).
3. مقادیر متغیرها را پر کنید:
   - `TELEGRAM_BOT_TOKEN`: توکن بات تلگرام (`8985367067:AAEd0O9vblcaPgOOCnIDQ0zKtUzLev_5yJI`)
   - `TELEGRAM_ALLOWED_USERS`: آیدی عددی شما (`6171669998`)
   - `GEMINI_API_KEY`: کلید رایگان جمینای از [Google AI Studio](https://aistudio.google.com/)
   - `MODEL_PROVIDER`: `gemini`
   - `MODEL_NAME`: `gemini-2.5-flash`
4. روی **Apply** کلیک کنید تا کانتینر ظرف ۳ دقیقه بالا بیاید.

---

## ⏰ روش ۲۴/۷ بیدار نگه داشتن (Keep-Alive)

پلن رایگان Render اگر ۱۵ دقیقه ترافیک وب دریافت نکند، سرویس را متوقف (sleep) می‌کند.
برای اینکه بات تلگرام شما همیشه بیدار و در دسترس باشد:
1. آدرس عمومی سرویس خود در رندر را کپی کنید (مثلاً `https://hermes-telegram-agent-xxxx.onrender.com/healthz`).
2. به سایت رایگان [cron-job.org](https://cron-job.org) یا [uptimerobot.com](https://uptimerobot.com) بروید.
3. یک مانیتور رایگان بسازید که هر **۱۰ دقیقه** یک درخواست `GET` به این آدرس بفرستد.
4. با این کار، سرویس شما **به صورت ۲۴ ساعته و دائمی فعال خواهد ماند!**

---

## 🌐 دیپلوی جایگزین روی Koyeb

در [koyeb.com](https://koyeb.com):
1. ثبت نام با گیت‌هاب.
2. انتخاب **Create Service** -> **GitHub**.
3. انتخاب ریپازیتوری `hermes-agent-cloud`.
4. انتخاب پلن **Free (Eco Nano)**.
5. اضافه کردن متغیرهای محیطی تلگرام و کلید مدل.
6. دیپلوی! (کویب حتی نیاز به پینگ دوره‌ای ندارد).
