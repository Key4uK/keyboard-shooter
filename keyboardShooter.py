from pynput import keyboard, mouse
import pygame
import signal
import sys

pygame.mixer.init()

# Load sounds
shot_sound = pygame.mixer.Sound("shot.wav")
reload_sound = pygame.mixer.Sound("reload.wav")
boom_sound = pygame.mixer.Sound("boom.wav")

left_click_sound = pygame.mixer.Sound("left.wav")
right_click_sound = pygame.mixer.Sound("right.wav")
middle_click_sound = pygame.mixer.Sound("middle.wav")

muted = False
shift_pressed = False

print("Shooter started!")
print("Press SHIFT + M to toggle mute")
print("ESC to quit")

# ---- Safe play function ----
def play_sound(sound):
    if not muted:
        sound.play()

# ---- Keyboard handlers ----
def on_key_press(key):
    global muted, shift_pressed

    try:
        # Detect shift press
        if key in (keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r):
            shift_pressed = True

        # Detect Shift + M
        elif hasattr(key, 'char') and key.char.lower() == 'm' and shift_pressed:
            muted = not muted
            if muted:
                print("🔇 Muted")
            else:
                print("🔊 Unmuted")

        elif key == keyboard.Key.space:
            play_sound(reload_sound)

        elif key == keyboard.Key.enter:
            play_sound(boom_sound)

        else:
            play_sound(shot_sound)

    except:
        play_sound(shot_sound)


def on_key_release(key):
    global shift_pressed
    if key in (keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r):
        shift_pressed = False


# ---- Mouse handler ----
def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.left:
            play_sound(left_click_sound)
        elif button == mouse.Button.right:
            play_sound(right_click_sound)
        elif button == mouse.Button.middle:
            play_sound(middle_click_sound)


# ---- Clean shutdown ----
def signal_handler(sig, frame):
    print("Shutting down...")
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

keyboard_listener = keyboard.Listener(
    on_press=on_key_press,
    on_release=on_key_release
)

mouse_listener = mouse.Listener(on_click=on_click)

keyboard_listener.start()
mouse_listener.start()

keyboard_listener.join()
mouse_listener.join()
