import pyautogui
import time

def main():
    print("Move your mouse around to see coordinates. Press Ctrl+C to exit.")
    try:
        while True:
            x, y = pyautogui.position()
            pixel = pyautogui.screenshot().getpixel((x, y))
            print(f"X: {x}, Y: {y}, Pixel Color: {pixel}", end="\r", flush=True)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nExiting.")

if __name__ == "__main__":
    main()
