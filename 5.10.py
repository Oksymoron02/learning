current_users = ['admin', 'oksymoron', 'mehashin', 'franul', 'thinker']

new_users = ['oksy', 'oksykodon', 'OkSYmoron', 'thinker2']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Nick " + new_user + " jest już zajęty!")
    else:
        print(f"Nick " + new_user +  " jest dostępny.")