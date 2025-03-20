import time
import random
from collections import defaultdict

class ThrottlingRateLimiter:
    def __init__(self, min_interval: float = 10.0):
        self.min_interval = min_interval
        self.last_messages = defaultdict(lambda: ['', 0.0])

    def can_send_message(self, user_id: str) -> bool:
        return self.time_until_next_allowed(user_id) <= 0

    def record_message(self, user_id: str) -> bool:
        if not self.can_send_message(user_id): return False
        current_time = time.time()
        self.last_messages[user_id][1] = current_time
        self.last_messages[user_id][0] = 'message' # the message was sent
        return True

    def time_until_next_allowed(self, user_id: str) -> float:
        current_time = time.time()
        last_message_time = self.last_messages[user_id][1]
        return self.min_interval - (current_time - last_message_time)

def test_throttling_limiter():
    limiter = ThrottlingRateLimiter(min_interval=10.0)

    print("\n=== Симуляція потоку повідомлень (Throttling) ===")
    for message_id in range(1, 11):
        user_id = message_id % 5 + 1

        result = limiter.record_message(str(user_id))
        wait_time = limiter.time_until_next_allowed(str(user_id))

        print(f"Повідомлення {message_id:2d} | Користувач {user_id} | "
              f"{'✓' if result else f'× (очікування {wait_time:.1f}с)'}")

        # Випадкова затримка між повідомленнями
        time.sleep(random.uniform(0.1, 1.0))

    print("\nОчікуємо 10 секунд...")
    time.sleep(10)

    print("\n=== Нова серія повідомлень після очікування ===")
    for message_id in range(11, 21):
        user_id = message_id % 5 + 1
        result = limiter.record_message(str(user_id))
        wait_time = limiter.time_until_next_allowed(str(user_id))
        print(f"Повідомлення {message_id:2d} | Користувач {user_id} | "
              f"{'✓' if result else f'× (очікування {wait_time:.1f}с)'}")
        time.sleep(random.uniform(0.1, 1.0))

if __name__ == "__main__":
    test_throttling_limiter()
