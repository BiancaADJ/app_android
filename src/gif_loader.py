from PyQt6.QtGui import QMovie

# Tela carregamento
def add_gif_to_label(label, gif_path):
    movie = QMovie(gif_path)
    label.setMovie(movie)
    movie.start()