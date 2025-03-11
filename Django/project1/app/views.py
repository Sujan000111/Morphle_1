from django.shortcuts import render
import os
import subprocess
from datetime import datetime
import pytz
from django.http import JsonResponse

def htop_view(request):
    # Get system username
    username = os.getlogin()

    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Execute the 'top' command
    try:
        result = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True)
        top_output = result.stdout.split("\n")[:10]  # Show first 10 lines
    except Exception as e:
        top_output = [str(e)]

    # Response JSON
    response_data = {
        "Name": "Sujan",  # Replace with your name
        "Username": "codespace",
        "Server Time": server_time,
        "TOP Command Output": htop
    }
    return JsonResponse(response_data)

# Create your views here.
