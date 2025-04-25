import requests
import os

def renew_server():
    # Get sensitive information from environment variables
    xsrf_token = os.getenv('XSRF_TOKE')  # Get XSRF token from environment variables
    session_cookie = os.getenv('SESSION_COOKIE')  # Get session cookie from environment variables

    if not xsrf_token or not session_cookie:
        print("Error: XSRF_TOKEN or SESSION_COOKIE is not set.")
        return

    url = 'https://panel.eternalhosting.cloud/api/client/freeservers/578954c7-576b-44a6-a7a6-453a6c1f92c4/renew'

    headers = {
        'Content-Type': 'application/json',
        'X-XSRF-TOKEN': xsrf_token,  # XSRF token from environment
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    cookies = {
        'pterodactyl_session': session_cookie  # Session cookie from environment
    }

    try:
        response = requests.post(url, headers=headers, cookies=cookies)

        if response.status_code == 200:
            print('Server renewed successfully.')
            print(response.json())  # Optional: print the server renewal response
        else:
            print(f'Error renewing server: {response.status_code}')
            print(response.text)  # Print the detailed error message
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')


# Call the function to renew the server
renew_server()
