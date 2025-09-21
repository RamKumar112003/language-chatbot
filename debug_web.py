#!/usr/bin/env python3
"""
Debug script for web application
"""

from web_app import app

def test_about_route():
    """Test the about route"""
    print("Testing about route...")
    
    with app.test_client() as client:
        response = client.get('/about')
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ About page works")
        else:
            print(f"❌ About page failed: {response.status_code}")
            print("Response:", response.data.decode()[:500])

if __name__ == '__main__':
    test_about_route()
