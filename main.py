#this will call the battlefield class

from battlefield_class import Battlefield


if __name__ == '__main__':
    
    game = Battlefield()
    
    game.run_game()
    game.display_welcome()
    game.battle()
    while dino_1.dino_health > 0 and dino_2.dino_health > 0 and dino_3.dino_health > 0 or robot_1.robot_health > 0 and robot_2.robot_health > 0 and robot_3.robot_health > 0:
        for i in game.dino_herd:
            game.dino_turn([i])
            game.show_dino_opponent_options([i])
            game.robo_turn([i])
            game.show_robo_opponent_options([i])
    if dino_1.dino_health <= 0 and dino_2.dino_health <= 0 and dino_3.dino_health <= 0:
        winner = "Robots!"
        game.display_winners() + winner

    else:
        winner = "Dinosaurs!"
        game.display_winners() + winner