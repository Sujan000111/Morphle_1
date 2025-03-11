from django.shortcuts import render
import os
import subprocess
from datetime import datetime
import pytz
from django.http import JsonResponse

def htop_view(request):
    # Get system username
    username = os.getenv('USER', 'codespace_user')

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Run the htop command
    try:
        result = subprocess.run(["htop", "-b"], capture_output=True, text=True, timeout=2)
        top_output=subprocess.getoutput('top -b -n 1')
    except Exception as e:
        htop_output = [str(e)]

    return JsonResponse({
        "Name": "Your Full Name",  # Replace with your name
        "Username": username,
        "Server Time": server_time,
        "Top_output": top_output
    })