@echo off
echo 🎯 AI Quiz Generator from YouTube Videos
echo ========================================
echo.
echo Starting the application...
echo.
echo Make sure you have:
echo 1. Python installed
echo 2. Dependencies installed (pip install -r requirements.txt)
echo 3. .env file with your DEEPSEEK_API_KEY
echo.
echo The app will open in your default browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.
pause
streamlit run app.py
pause 