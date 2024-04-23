# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:02:54 2024

@author: ocanh
"""

class Film:
    def __init__(self, judul, rilis, director):
        self.judul = judul
        self.rilis = rilis
        self.director = director

def main():
    films = []
    
    # Input data film favorit
    films.append(Film("Onepiece", 1999, "Oda"))
    films.append(Film("Naruto", 1999, "Masashi Kishimoto"))
    films.append(Film("Dilan 1990", 2018, "Pidi Baiq"))
    films.append(Film("Captain Tsubasa", 2018, "Tsuzuki Katsuaki"))
    films.append(Film("Kimetsu no Yaiba", 2019, "Haruo Sotozaki"))
    
    # Output
    print("Prak 5 (Hasanul Bashori - 064002300041)")
    print("----- ELKOM 2 --------")
    for i, film in enumerate(films, 1):
        print(f"Film favorit ke -{i}:")
        print(f"Judul: {film.judul}")
        print(f"Rilis: {film.rilis}")
        print(f"Director: {film.director}")
        print("=============================")

if __name__ == "__main__":
    main()
