'''
Archivo principal del juego Games
'''
from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import json

def main():
    ''' Funcion principal del juego'''
    if archivo_torneo != "":
        with open(archivo_torneo, "r") as f:
            torneo = json.load(f)
    else:
        players_mexico = ['Chicharito', 'Piojo', 'Chucky', 'Tecatito', 'Gullit', 'Ochoa', 'Guardado', 'Herrera', 'Layun', 'Moreno', 'Araujo']
        players_espania = ['Casillas', 'Ramos', 'Pique', 'Iniesta', 'Xavi', 'Torres', 'Villa', 'Silva', 'Busquets', 'Alba', 'Alonso']
        lisa_mexico = [Athlete(x) for x in players_mexico]
        lisa_espania = [Athlete(x) for x in players_espania]
        soccer = Sport("Soccer", 11, "FIFA")
        mexico = Team("Mexico", soccer, lisa_mexico)
        espania = Team("Espania", soccer, lisa_espania)
        juego = Game(mexico, espania)
        torneo = [juego.to_json()]
        with open(archivo_torneo, "w", encoding='utf8') as f:
            json.dump(torneo, f, ensure_ascii=False, indent=4)
        print(f"Se esscribio el archivo {archivo_torneo} con un torneo de {len(torneo)} juego(s)")
    # Jugar todos los juegos del torneo
    for juego in torneo:
        A = Team(juego['A']['name'], Sport(juego['A']['sport']['name'], juego['A']['sport']['players'], juego['A']['sport']['league']), [Athlete(x['name']) for x in juego['A']['players']])
        B = Team(juego['B']['name'], Sport(juego['B']['sport']['name'], juego['B']['sport']['players'], juego['B']['sport']['league']), [Athlete(x['name']) for x in juego['B']['players']])
        game = Game(A, B)
        game.play()
        print(game)
        print("----------------")

if __name__ == "__main__":
    archivo_torneo = ""
    main(archivo_torneo)