import subprocess

def add_user(username):
    try:
        subprocess.run(['net', 'user', username, '/add'], check=True)
        print("Пользователь", username, "добавлен.")
        return True
    except:
        print("Ошибка при добавлении пользователя", username)
        return False

def remove_user(username):
    try:
        subprocess.run(['net', 'user', username, '/delete'], check=True)
        print("Пользователь", username, "удален.")
        return True
    except:
        print("Ошибка при удалении пользователя", username)
        return False

def list_users():
    try:
        result = subprocess.run(['net', 'user'], capture_output=True, text=True, encoding='cp866')
        users = []
        lines = result.stdout.splitlines()
        for line in lines:
            line = line.strip()
            if line and not line.startswith('-') and not line.startswith('Учетные'):
                parts = line.split()
                for part in parts:
                    if part and not part.startswith('$') and len(part) > 1:
                        users.append(part)
        return users
    except:
        return []

print("Существующие пользователи:", list_users()[:10])

add_user('test_user')
remove_user('test_user')