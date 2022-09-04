from Hang_man_project import The_Full_Project_Hang_Man

if __name__ == '__main__':
    gameNumber = input('choose a game:\n'
                       '1. flappy_destroyer\n'
                       '2. flapy_bird\n'
                       '3.hang man\n'
                       '4.snake game\n'
                       '5.the_maze\n')
    if gameNumber == "1":
        from flappy_destroyer import The_game
    if gameNumber == "2":
        from flapy_bird import FlapyBird
    if gameNumber == "3":
        The_Full_Project_Hang_Man.main()
    if gameNumber == "4":
        from snake_game import Snake_Game
    if gameNumber == "5":
        from the_maze import maze
