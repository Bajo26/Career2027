def main():
    favorite_games = []
    number = 1
    
    while True:
        game = input("Enter your favorite game (or type 'done' to finish): ")
        if game in favorite_games:
            print("You have already entered this game. Please enter a different one.")
            continue
        if game.strip().lower() == 'done':
            break
        favorite_games.append(game)
    

    print("\nYour favorite games are:")
    
    for game in favorite_games:
        print(f"{number}. {game}")
        number += 1

    print("\nTotal Games:", len(favorite_games))
if __name__ == "__main__":
    main()