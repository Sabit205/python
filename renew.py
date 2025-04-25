import requests
import os

def renew_server():
    # Get sensitive information from environment variables
    xsrf_token = os.getenv('XSRF_TOKEN')  # Corrected variable name
    session_cookie = os.getenv('SESSION_COOKIE')

    if not xsrf_token or not session_cookie:
        print("Error: XSRF_TOKEN or SESSION_COOKIE is not set.")
        return

    url = 'https://panel.eternalzero.cloud/api/client/freeservers/e96ce0bd-a984-4d67-976e-6effb8c863ce/renew'

    headers = {
        'Content-Type': 'application/json',
        'X-XSRF-TOKEN': xsrf_token,
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    cookies = {
        'XSRF-TOKEN': xsrf_token,  # Also needed in cookies
        'pterodactyl_session': session_cookie
    }

    try:
        response = requests.post(url, headers=headers, cookies=cookies, json={})

        if response.status_code == 200:
            print('Server renewed successfully.')
            print(response.json())  # Optional: show response data
        else:
            print(f'Error renewing server: {response.status_code}')
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')


# Call the function to renew the server
renew_server()
