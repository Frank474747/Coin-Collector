import pygame

# Initialize Pygame's mixer
pygame.mixer.init()

# Load a sound effect
sound = pygame.mixer.Sound("sound_effect.wav")

# Play the sound
sound.play()

# Wait for the sound to finish (for demonstration)
pygame.time.delay(int(sound.get_length() * 1000))
