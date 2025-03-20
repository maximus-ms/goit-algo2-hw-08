# Algo2. Home work 8
## "Flow Control and Rate Limiting Algorithms"

### Task 1. Implementation of Rate Limiter Using Sliding Window Algorithm for Chat Message Frequency Control

A chat system needs to implement a mechanism for limiting the frequency of user messages to prevent spam. The implementation should use the Sliding Window algorithm for precise time interval control, which allows tracking the number of messages in a given time window and limiting users from sending messages if the limit is exceeded.

#### Technical Requirements

1. The implementation must use the Sliding Window algorithm for precise time interval control.

2. Basic system parameters: window size (window_size) — 10 seconds and maximum number of messages in the window (max_requests) — 1.

3. Implement the `SlidingWindowRateLimiter` class.

4. Implement the following class methods:

 - `_cleanup_window` — for cleaning up outdated requests from the window and updating the active time window;
 - `can_send_message` — for checking if a message can be sent in the current time window;
 - `record_message` — for recording a new message and updating user history;
 - `time_until_next_allowed` — for calculating the waiting time until the next message can be sent.

5. Data structure for storing message history — `collections.deque`.

#### Acceptance Criteria

1. When attempting to send a message earlier than 10 seconds, the `can_send_message` method returns `False`.

2. For the user's first message, it always returns `True`.

3. When all messages are removed from the user's window, the user record is deleted from the data structure.

4. The `time_until_next_allowed` method returns the waiting time in seconds.

5. The test function according to the example has been run and works as expected.

#### Solution

The taks implemented in file `task1.py`

Output: 
```
=== Симуляція потоку повідомлень ===
Повідомлення  1 | Користувач 2 | ✓
Повідомлення  2 | Користувач 3 | ✓
Повідомлення  3 | Користувач 4 | ✓
Повідомлення  4 | Користувач 5 | ✓
Повідомлення  5 | Користувач 1 | ✓
Повідомлення  6 | Користувач 2 | × (очікування 7.0с)
Повідомлення  7 | Користувач 3 | × (очікування 6.8с)
Повідомлення  8 | Користувач 4 | × (очікування 7.0с)
Повідомлення  9 | Користувач 5 | × (очікування 6.2с)
Повідомлення 10 | Користувач 1 | × (очікування 6.4с)

Очікуємо 4 секунди...

=== Нова серія повідомлень після очікування ===
Повідомлення 11 | Користувач 2 | × (очікування 0.0с)
Повідомлення 12 | Користувач 3 | × (очікування 0.0с)
Повідомлення 13 | Користувач 4 | × (очікування 0.4с)
Повідомлення 14 | Користувач 5 | × (очікування 0.0с)
Повідомлення 15 | Користувач 1 | × (очікування 0.4с)
Повідомлення 16 | Користувач 2 | ✓
Повідомлення 17 | Користувач 3 | ✓
Повідомлення 18 | Користувач 4 | ✓
Повідомлення 19 | Користувач 5 | ✓
Повідомлення 20 | Користувач 1 | ✓
```

### Task 2. Implementation of Rate Limiter Using Throttling Algorithm for Chat Message Frequency Control

A chat system needs to implement a mechanism for limiting the frequency of user messages to prevent spam. The implementation should use the Throttling algorithm for controlling time intervals between messages, which ensures a fixed waiting interval between user messages and limits the sending frequency if this interval is not observed.

#### Technical Requirements

1. The implementation must use the `Throttling` algorithm for time interval control.

2. Basic system parameter: minimum interval between messages (`min_interval`) — 10 seconds.

3. Implement the `ThrottlingRateLimiter` class.

4. Implement the following class methods:

 - `can_send_message` — for checking if a message can be sent based on the time of the last message;
 - `record_message` — for recording a new message and updating the time of the last message;
 - `time_until_next_allowed` — for calculating the time until the next message can be sent.

5. Data structure for storing the time of last message — `Dict[str, float]`.

#### Acceptance Criteria

1. When attempting to send a message earlier than 10 seconds after the previous one, the `can_send_message` method returns `False`.

2. For the user's first message, it always returns `True`.

3. The `time_until_next_allowed` method returns the waiting time in seconds until the next allowed message.

4. The test function according to the example has been run and works as expected.

#### Solution

The taks implemented in file `task2.py`

Output: 
```
=== Симуляція потоку повідомлень (Throttling) ===
Повідомлення  1 | Користувач 2 | ✓
Повідомлення  2 | Користувач 3 | ✓
Повідомлення  3 | Користувач 4 | ✓
Повідомлення  4 | Користувач 5 | ✓
Повідомлення  5 | Користувач 1 | ✓
Повідомлення  6 | Користувач 2 | × (очікування 7.1с)
Повідомлення  7 | Користувач 3 | × (очікування 7.0с)
Повідомлення  8 | Користувач 4 | × (очікування 7.3с)
Повідомлення  9 | Користувач 5 | × (очікування 7.2с)
Повідомлення 10 | Користувач 1 | × (очікування 7.3с)

Очікуємо 10 секунд...

=== Нова серія повідомлень після очікування ===
Повідомлення 11 | Користувач 2 | ✓
Повідомлення 12 | Користувач 3 | ✓
Повідомлення 13 | Користувач 4 | ✓
Повідомлення 14 | Користувач 5 | ✓
Повідомлення 15 | Користувач 1 | ✓
Повідомлення 16 | Користувач 2 | × (очікування 6.7с)
Повідомлення 17 | Користувач 3 | × (очікування 7.3с)
Повідомлення 18 | Користувач 4 | × (очікування 7.9с)
Повідомлення 19 | Користувач 5 | × (очікування 7.6с)
Повідомлення 20 | Користувач 1 | × (очікування 7.5с)
```
