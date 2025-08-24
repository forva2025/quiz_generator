#!/usr/bin/env python3
"""
Simple API Key Test Script
Run this to quickly test if your DeepSeek API key is working
"""

import os
import requests
from dotenv import load_dotenv

def test_api_key():
    """Test the DeepSeek API key"""
    print("🔑 Testing DeepSeek API Key...")
    print("=" * 50)
    
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.getenv('DEEPSEEK_API_KEY')
    
    if not api_key:
        print("❌ No API key found!")
        print("💡 Create a .env file with: DEEPSEEK_API_KEY=your_key_here")
        return False
    
    # Check if it's a placeholder
    if api_key in ["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "your_actual_deepseek_api_key_here", "your_deepseek_api_key_here"]:
        print("❌ Placeholder API key detected!")
        print("💡 Replace the placeholder with your real DeepSeek API key")
        print("🔗 Get your key from: https://platform.deepseek.com/")
        return False
    
    print(f"✅ API key found (length: {len(api_key)} characters)")
    
    # Test API call
    print("\n🌐 Testing API connection...")
    
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": "Hello, this is a test message."}],
        "temperature": 0.7,
        "max_tokens": 50
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            print("✅ API connection successful!")
            result = response.json()
            content = result['choices'][0]['message']['content']
            print(f"📝 Response: {content}")
            return True
        elif response.status_code == 401:
            print("❌ Authentication failed!")
            print("💡 Check if your API key is correct and active")
            return False
        elif response.status_code == 429:
            print("⏰ Rate limit exceeded!")
            print("💡 Try again later")
            return False
        else:
            print(f"❌ API request failed (Status: {response.status_code})")
            print(f"📝 Response: {response.text[:200]}...")
            return False
            
    except requests.exceptions.Timeout:
        print("⏰ Request timed out!")
        print("💡 Check your internet connection")
        return False
    except requests.exceptions.ConnectionError:
        print("🌐 Connection error!")
        print("💡 Check your internet connection")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_api_key()
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 Your API key is working correctly!")
        print("🚀 You can now run the main app: streamlit run app.py")
    else:
        print("⚠️  API key test failed. Please fix the issues above.")
        print("📖 Check the README.md for troubleshooting tips.")
    
    print("=" * 50) 