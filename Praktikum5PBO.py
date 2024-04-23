# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:17:49 2024

@author: ocanh
"""

class FilmFavorit:
    def __init__(self):
        self.daftar_film = []

    def masukkan_film(self):
        print("Masukkan 5 film favorit Anda:")
        for i in range(5):
            film = input(f"Film favorit ke-{i+1}: ")
            self.daftar_film.append(film)

    def tampilkan_daftar(self):
        print("\n-- Daftar Film Favorit --")
        for i, film in enumerate(self.daftar_film, start=1):
            print(f"{i}. {film}")


if __name__ == "__main__":
    film_favorit = FilmFavorit()
    film_favorit.masukkan_film()
    film_favorit.tampilkan_daftar()
