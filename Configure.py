try:
    import os
    AUTHOR: str = 'Chanchal Roy'
    MOBILE_NO: str = os.environ['my_phone_no']
    EMAIL_ID: str = os.environ['my_email_ID']
    APP_PASSWORD: str = os.environ['my_app_psw']
    WEATHER_API_KEY: str = os.environ['weather_api_key']
    NEWS_API_KEY: str = os.environ['news_api_key']

except:
    AUTHOR: str = '' # Enter Your Name.
    MOBILE_NO: str = '' # Enter Your Contact/Mobile Number.
    EMAIL_ID: str = '' # Enter Your Email ID.
    APP_PASSWORD: str = '' # Enter Your App Password.
    WEATHER_API_KEY: str = '' # Enter Your Weather API Key.
    NEWS_API_KEY: str = '' # Enter Your News API Key.