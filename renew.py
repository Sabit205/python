import requests
import os

def renew_server():
    xsrf_token_raw = os.getenv('XSRF_TOKEN')
    session_cookie = os.getenv('SESSION_COOKIE')

    if not xsrf_token_raw or not session_cookie:
        print("Error: XSRF_TOKEN or SESSION_COOKIE is not set.")
        return

    # Use the raw token as-is
    xsrf_token = xsrf_token_raw

    url = 'https://gpanel.eternalzero.cloud/api/client/freeservers/e96ce0bd-a984-4d67-976e-6effb8c863ce/renew'

    headers = {
        'Content-Type': 'application/json',
        'X-XSRF-TOKEN': xsrf_token,
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://gpanel.eternalzero.cloud/',
    }

    cookies = {
        'XSRF-TOKEN': xsrf_token_raw,  # raw token in cookie
        'pterodactyl_session': session_cookie
    }

    try:
        response = requests.post(url, headers=headers, cookies=cookies, json={})
        if response.status_code == 200:
            print('Server renewed successfully.')
            print(response.json())
        else:
            print(f'Error renewing server: {response.status_code}')
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f'Request failed: {e}')

renew_server()
