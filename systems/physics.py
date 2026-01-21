from settings import GRAVITY

class Physics:
    @staticmethod
    def apply_gravity(entity, dt):
        entity.velocity.y += GRAVITY * dt
