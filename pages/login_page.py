import pandas as pd
import bcrypt

USERS_FILE = "data/users.csv"

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def signup_user(name, email, password):
    try:
        users = pd.read_csv(USERS_FILE)
    except FileNotFoundError:
        users = pd.DataFrame(columns=["id","name","email","password_hash"])

    if email in users['email'].values:
        return False, "Email already registered"
    
    user_id = users['id'].max() + 1 if not users.empty else 1
    new_user = pd.DataFrame([[user_id, name, email, hash_password(password)]], 
                            columns=["id","name","email","password_hash"])
    users = pd.concat([users, new_user], ignore_index=True)
    users.to_csv(USERS_FILE, index=False)
    return True, "Signup successful"

def login_user(email, password):
    try:
        users = pd.read_csv(USERS_FILE)
    except FileNotFoundError:
        return False, "No users registered"

    user = users[users['email'] == email]
    if user.empty:
        return False, "User not found"
    if check_password(password, user.iloc[0]['password_hash']):
        return True, user.iloc[0]
    else:
        return False, "Incorrect password"
