#!/usr/bin/env python3
"""
Test script for AI Quiz Generator from YouTube Videos
Run this script to verify your environment setup and API configuration
"""

import sys
import os
import requests
import json
from dotenv import load_dotenv

def test_environment():
    """Test basic environment setup"""
    print("🔍 Testing environment setup...")
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major >= 3 and python_version.minor >= 8:
        print(f"✅ Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    else:
        print(f"❌ Python version {python_version.major}.{python_version.minor}.{python_version.micro} is too old. Need 3.8+")
        return False
    
    # Check required packages
    required_packages = [
        ('streamlit', 'streamlit'),
        ('requests', 'requests'), 
        ('youtube_transcript_api', 'youtube_transcript_api'),
        ('reportlab', 'reportlab'),
        ('python-dotenv', 'dotenv')
    ]
    
    missing_packages = []
    for package_name, import_name in required_packages:
        try:
            __import__(import_name)
            print(f"✅ {package_name}")
        except ImportError:
            print(f"❌ {package_name} - not installed")
            missing_packages.append(package_name)
    
    if missing_packages:
        print(f"\n📦 Install missing packages with:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    print("✅ All required packages are installed")
    return True

def test_api_key():
    """Test DeepSeek API key configuration"""
    print("\n🔑 Testing API key configuration...")
    
    # Load environment variables
    load_dotenv()
    
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        print("❌ DEEPSEEK_API_KEY not found in environment variables")
        print("💡 Create a .env file with your API key:")
        print("   DEEPSEEK_API_KEY=your_actual_api_key_here")
        return False
    
    if api_key == "your_deepseek_api_key_here" or len(api_key) < 10:
        print("❌ API key appears to be invalid or placeholder")
        print("💡 Make sure you've replaced the placeholder with your actual API key")
        return False
    
    print(f"✅ API key found (length: {len(api_key)} characters)")
    return True

def test_api_connection():
    """Test DeepSeek API connection"""
    print("\n🌐 Testing API connection...")
    
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        print("❌ Cannot test API connection without API key")
        return False
    
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Simple test message
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": "Hello, this is a test message."}],
        "temperature": 0.7,
        "max_tokens": 50
    }
    
    try:
        print("🔄 Sending test request to DeepSeek API...")
        response = requests.post(url, headers=headers, json=data, timeout=15)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ API connection successful!")
            print(f"   Response time: {response.elapsed.total_seconds():.2f} seconds")
            return True
        elif response.status_code == 401:
            print("❌ API authentication failed - check your API key")
            return False
        elif response.status_code == 429:
            print("❌ API rate limit exceeded - try again later")
            return False
        else:
            print(f"❌ API request failed with status code: {response.status_code}")
            print(f"   Response: {response.text[:200]}...")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ API request timed out - check your internet connection")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - check your internet connection")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False

def test_youtube_transcript():
    """Test YouTube transcript API"""
    print("\n📺 Testing YouTube transcript API...")
    
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        
        # Test with a known video that has captions
        test_video_id = "dQw4w9WgXcQ"  # Rick Roll - has captions
        
        print("🔄 Testing transcript extraction...")
        # Use the API method that matches your installed version (1.2.2)
        transcript_list = YouTubeTranscriptApi().list(test_video_id).find_transcript(['en']).fetch()
        
        if transcript_list and len(transcript_list) > 0:
            # Check if we can access the text attribute
            if hasattr(transcript_list[0], 'text'):
                print("✅ YouTube transcript API working correctly")
                print(f"   Test video transcript length: {len(transcript_list)} segments")
                print(f"   Sample text: '{transcript_list[0].text[:50]}...'")
                return True
            else:
                print("❌ Transcript objects don't have expected structure")
                return False
        else:
            print("❌ No transcript data received")
            return False
            
    except Exception as e:
        print(f"❌ YouTube transcript API test failed: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("🎯 AI Quiz Generator - Environment Test")
    print("=" * 50)
    
    tests = [
        ("Environment Setup", test_environment),
        ("API Key Configuration", test_api_key),
        ("API Connection", test_api_connection),
        ("YouTube Transcript API", test_youtube_transcript)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {str(e)}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Your environment is ready.")
        print("🚀 You can now run the main app with: streamlit run app.py")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please fix the issues above.")
        print("💡 Check the README.md file for troubleshooting tips.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 