import flet as ft

def main(page: ft.Page):
    page.title = "Login Page"
    page.window_width = 400
    page.window_height = 300
    
    # Predefined users
    users = {"user1": "user1", "user2": "user2", "user3": "user3", "admin": "admin"}
    
    def login(e):
        username = username_input.value
        password = password_input.value
        
        if username in users and users[username] == password:
            page.clean()
            page.add(ft.Text(f"Welcome, {username}!", size=34))
        else:
            error_text.value = "Invalid username or password."
            page.update()
    
    username_input = ft.TextField(label="Username")
    password_input = ft.TextField(label="Password", password=True)
    login_button = ft.ElevatedButton("Login", on_click=login)
    error_text = ft.Text(color="red")
    
    page.add(username_input, password_input, login_button, error_text)
    
ft.app(target=main)
