
# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('upa.mp3')
pygame.mixer.music.play(loops=1, start=0.0)
pygame.event.wait()