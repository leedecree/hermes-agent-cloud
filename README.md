# 🛰️ Hermes Agent Cloud (Free 24/7 Deployment)

یک نسخه سبک و کانتینری از **Hermes Agent** طراحی شده برای اجرا روی سرویس‌های ابری رایگان مانند **Render** و **Koyeb** متصل به تلگرام با Keep-Alive ضدخواب.

---

## ⚡ امکانات

- 🚀 **رایگان بدون نیاز به کارت بانکی:** بدون نیاز به کردیت کارت بین‌المللی
- 🤖 **متصل به تلگرام:** کنترل کامل ایجنت هرمس از طریق بات تلگرام شخصی
- 🛡️ **امنیت بالا:** قفل شده روی آی‌دی عددی شما (`TELEGRAM_ALLOWED_USERS`)
- 💓 **Keep-Alive وب‌سرور:** مجهز به اندپوینت `/healthz` برای بیدار ماندن دائمی روی Render
- 🧠 **پشتیبانی از مدل‌های رایگان و پرسرعت:** Google Gemini 2.5 Flash / Groq / OpenRouter

---

## 🛠️ راهنمای دیپلوی سریع روی Render (۵ دقیقه)

### مرحله ۱: ثبت نام در Render
1. به سایت [render.com](https://render.com) بروید.
2. با اکانت گیت‌هاب لاگین کنید (نیاز به کارت بانکی ندارد).

### مرحله ۲: ایجاد سرویس
1. روی دکمه **New +** کلیک کرده و گزینه **Web Service** را انتخاب کنید.
2. گزینه **Build and deploy from a Git repository** را انتخاب کرده و ریپازیتوری `hermes-agent-cloud` را انتخاب کنید.
3. مشخصات زیر را تنظیم کنید:
   - **Name:** `hermes-telegram-agent`
   - **Language:** `Docker`
   - **Instance Type:** `Free`
4. در بخش **Environment Variables**، مقادیر زیر را وارد کنید:
   - `TELEGRAM_BOT_TOKEN`: توکن بات تلگرام شما
   - `TELEGRAM_ALLOWED_USERS`: آیدی عددی تلگرام شما (`6171669998`)
   - `GEMINI_API_KEY`: کلید رایگان جمینای از [Google AI Studio](https://aistudio.google.com/)
   - `MODEL_PROVIDER`: `gemini`
   - `MODEL_NAME`: `gemini-2.5-flash`
5. دکمه **Create Web Service** را بزنید تا بیلد آغاز شود.

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
