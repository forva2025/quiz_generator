# 🎯 AI Quiz Generator from YouTube Videos

A powerful web application that automatically generates educational quizzes, flashcards, and summaries from YouTube video transcripts using AI. Built with Streamlit and powered by the DeepSeek API.

## ✨ Features

- **🎬 YouTube Integration**: Extract transcripts from any YouTube video with captions
- **🧠 AI-Powered Generation**: Create intelligent quizzes using DeepSeek AI
- **📝 Multiple Output Formats**: Generate multiple-choice questions, flashcards, and summaries
- **📊 Export Options**: Download results as JSON or PDF reports
- **🎨 Modern UI**: Beautiful, responsive interface built with Streamlit and custom CSS
- **🌐 Multi-language Support**: Automatic language detection and translation
- **⚡ Fast Processing**: Efficient transcript extraction and AI generation

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- DeepSeek API key ([Get one here](https://platform.deepseek.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd quiz
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   DEEPSEEK_API_KEY=your_actual_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```
   
   Or use the provided batch file (Windows):
   ```bash
   run_app.bat
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501`

## 🧪 Testing Your Setup

Run the test script to verify your environment:

```bash
python test_setup.py
```

This will check:
- Python version compatibility
- Required package installation
- API key configuration
- API connectivity
- YouTube transcript API functionality

## 📖 How to Use

### Basic Usage

1. **Enter YouTube URL**: Paste any YouTube video URL in the input field
2. **Generate Quiz**: Click the "Generate Quiz" button
3. **Wait for Processing**: The app will extract the transcript and generate content
4. **Review Results**: View the generated summary, quiz questions, and flashcards
5. **Export**: Download your results as JSON or PDF

### Supported YouTube URL Formats

- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`

### Requirements for YouTube Videos

- Video must have captions/subtitles enabled
- Video must be publicly accessible
- Video must not be age-restricted or private

## 🏗️ Project Structure

```
quiz/
├── app.py                 # Main Streamlit application
├── config.py             # Configuration settings and constants
├── requirements.txt      # Python dependencies
├── run_app.bat          # Windows batch file for easy startup
├── test_setup.py        # Environment testing script
├── index.html           # Landing page HTML
└── README.md            # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DEEPSEEK_API_KEY` | Your DeepSeek API key | Yes |

### Customization

Edit `config.py` to modify:
- API settings (temperature, max tokens, timeout)
- UI colors and styling
- Default quiz settings
- Error and success messages

## 📚 API Integration

### DeepSeek API

The application uses the DeepSeek API for intelligent quiz generation:

- **Model**: `deepseek-chat`
- **Temperature**: 0.7 (balanced creativity and accuracy)
- **Max Tokens**: 2000
- **Timeout**: 30 seconds

### YouTube Transcript API

Uses `youtube-transcript-api` for reliable transcript extraction with:
- Automatic language detection
- Fallback to generated transcripts
- Translation support for non-English content

## 🎨 UI Components

### Main Interface
- **Header**: Clean, centered title with emoji
- **Sidebar**: Configuration and usage instructions
- **Input Section**: YouTube URL input with validation
- **Results Display**: Organized sections for summary, quiz, and flashcards

### Styling
- **Custom CSS**: Professional color scheme and typography
- **Responsive Design**: Works on desktop and mobile devices
- **Interactive Elements**: Hover effects and smooth transitions

## 📊 Export Features

### JSON Export
- Structured data format
- Easy integration with other applications
- Preserves all generated content

### PDF Export
- Professional report formatting
- Includes all quiz content
- Ready for printing or sharing

## 🛠️ Technical Details

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `streamlit` | ≥1.28.0 | Web application framework |
| `requests` | ≥2.31.0 | HTTP client for API calls |
| `youtube-transcript-api` | ≥0.6.1 | YouTube transcript extraction |
| `reportlab` | ≥4.0.0 | PDF generation |
| `python-dotenv` | ≥1.0.0 | Environment variable management |

### Architecture

- **Frontend**: Streamlit web interface
- **Backend**: Python with async processing
- **AI Integration**: REST API calls to DeepSeek
- **Data Processing**: Transcript cleaning and formatting
- **Export System**: Multi-format output generation

## 🔍 Troubleshooting

### Common Issues

1. **"API key not found"**
   - Ensure `.env` file exists in project root
   - Check that `DEEPSEEK_API_KEY` is set correctly

2. **"Failed to get transcript"**
   - Verify video has captions enabled
   - Check video accessibility (not private/restricted)

3. **"API request failed"**
   - Verify internet connection
   - Check API key validity
   - Ensure DeepSeek service is available

4. **"Failed to generate quiz"**
   - Check API key and quota
   - Verify transcript content quality
   - Try with a different video

### Performance Tips

- Use videos with clear, well-transcribed captions
- Avoid very long videos (>1 hour) for faster processing
- Ensure stable internet connection for API calls

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py --server.port 8501
```

### Production Deployment
- Deploy to Streamlit Cloud, Heroku, or similar platforms
- Set environment variables in deployment configuration
- Ensure proper API key security

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the web framework
- [DeepSeek](https://platform.deepseek.com/) for AI capabilities
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for transcript extraction
- [ReportLab](https://www.reportlab.com/) for PDF generation

## 📞 Support

For issues and questions:
1. Check the troubleshooting section above
2. Run `python test_setup.py` to diagnose problems
3. Review the configuration in `config.py`
4. Open an issue in the repository

---

**Happy Quiz Generating! 🎓✨** 