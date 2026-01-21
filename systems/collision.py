class Collision:
    @staticmethod
    def player_ground(player, ground):
        if player.rect.colliderect(ground.rect):
            player.rect.bottom = ground.rect.top
            player.velocity.y = 0
            player.on_ground = True

    @staticmethod
    def player_enemy(player, enemy):
        return player.rect.colliderect(enemy.rect)
