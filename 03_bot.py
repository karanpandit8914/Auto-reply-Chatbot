import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(
    api_key="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"
)

def is_last_message_from_sender(chat_log, sender_name = "Mom"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True
    return False

# Small delay so you can switch to the target window
time.sleep(3)

# Step 1: Click on the chrome icon
pyautogui.click(925, 745)

time.sleep(1)  # wait for UI response

while True:
    # Step 2: Drag to select text
    pyautogui.moveTo(484, 191)
    pyautogui.dragTo(1275, 640, duration=0.5)

    time.sleep(2)

    # Step 3: Copy selected text (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')

    time.sleep(2)

    pyautogui.click(889, 400)

    # Step 4: Get text from clipboard
    chat_history = pyperclip.paste()

    # Store in variable
    print("Copied Text:\n", chat_history)


    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a person named karan who speaks hindi as well as english. You are from India and you are coder. You are analyze chat hitory and respond like Karan. Output should be the next chat response (text message only)"},
                {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message
        pyperclip.copy(response)


        # Step 5: Click on chat input box (IMPORTANT)
        pyautogui.click(846, 680)
        time.sleep(0.5)

        # Optional: ensure cursor is active
        pyautogui.click(846, 680)

        # Step 6: Paste into chat box
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.3)

        # Step 7: Send message
        pyautogui.press('enter')