"""
Configuration file for AI Quiz Generator from YouTube Videos
Modify these settings to customize the application behavior
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
DEEPSEEK_MODEL = "deepseek-chat"  # Try alternative: "deepseek-chat" or "deepseek-coder"
DEEPSEEK_TEMPERATURE = 0.7
DEEPSEEK_MAX_TOKENS = 4000  # Increased for maximum quiz generation
API_TIMEOUT = 60  # Increased from 30 to 60 seconds for longer transcripts

# App Configuration
APP_TITLE = "🎯 AI Quiz Generator from YouTube Videos"
APP_ICON = "🎯"
PAGE_LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "collapsed"

# Quiz Generation Settings
DEFAULT_QUIZ_QUESTIONS = 5
DEFAULT_OPTIONS_PER_QUESTION = 4
DEFAULT_FLASHCARDS = 5

# UI Configuration
MAIN_HEADER_COLOR = "#1f77b4"
SECTION_HEADER_COLOR = "#2c3e50"
QUESTION_BOX_BORDER_COLOR = "#3498db"
FLASHCARD_BORDER_COLOR = "#b3d9ff"
CORRECT_ANSWER_BG_COLOR = "#d4edda"
CORRECT_ANSWER_TEXT_COLOR = "#155724"

# Export Configuration
DEFAULT_JSON_FILENAME = "quiz_data.json"
DEFAULT_PDF_FILENAME = "quiz_report.pdf"
PDF_PAGE_SIZE = "letter"

# Error Messages
ERROR_MESSAGES = {
    "no_api_key": "DeepSeek API key not found. Please set DEEPSEEK_API_KEY environment variable.",
    "invalid_url": "Invalid YouTube URL. Please check the format.",
    "transcript_failed": "Failed to get transcript. Make sure the video has captions/subtitles enabled.",
    "quiz_generation_failed": "Failed to generate quiz. Please check your API key and try again.",
    "pdf_creation_failed": "Failed to create PDF. Please try again.",
    "json_parse_failed": "Failed to parse JSON response from API."
}

# Success Messages
SUCCESS_MESSAGES = {
    "transcript_extracted": "Transcript extracted successfully!",
    "quiz_generated": "Quiz generated successfully!",
    "export_ready": "Export ready! Click the download buttons below."
}

# Loading Messages
LOADING_MESSAGES = {
    "processing": "🔄 Processing... This may take a few moments.",
    "extracting_transcript": "📝 Extracting transcript...",
    "generating_quiz": "🧠 Generating quiz with AI...",
    "creating_pdf": "📊 Creating PDF report..."
}

# Help Text
HELP_TEXT = {
    "youtube_url": "Paste any YouTube video URL here. The video must have captions/subtitles enabled.",
    "generate_button": "Click to start the quiz generation process. This will extract the transcript and generate quiz content.",
    "export_json": "Download your quiz data as a JSON file for further processing or integration.",
    "export_pdf": "Download a formatted PDF report with all quiz content."
} 