#вывести наиболее популярного по количеству подписчиков человека
SELECT u.username, COUNT(f.follower_id) AS num_follower
FROM users u
LEFT JOIN followers f ON u.id = f.follower_id
GROUP BY u.id
ORDER BY num_follower DESC
LIMIT 1;

#вывести человека, который ни на кого не подписан
SELECT u.username
FROM users u
LEFT JOIN followers f ON u.id = f.follower_id
WHERE f.follower_id IS NULL;

#показать информацию пользователя по id из таблицы профиля
SELECT *
FROM users
WHERE id = 1; #здесь подставляем ID пользователя

#вывести непрочитанные сообщения для пользователя по id,"прочитать" эти сообщения
ALTER TABLE user_messages ADD read_at DATETIME;

SELECT * FROM user_messages
WHERE to_user > 0 AND read_at IS NULL;

UPDATE user_messages
SET read_at = NOW()
WHERE to_user > 0 AND read_at IS NULL;

#получить историю переписки между двумя пользователями
SELECT m.text, m.created_at
FROM user_messages um
JOIN messages m ON um.message_id = m.id
WHERE (um.from_user = 1 AND um.to_user = 2) OR (um.from_user = 2 AND um.to_user = 1)
ORDER BY m.created_at;

#вывести наиболее активного пользователя (с бОльшим количеством сообщений)
SELECT id, COUNT(*) AS message_count
FROM messages
GROUP BY id
ORDER BY message_count DESC
LIMIT 1;

#узнать среднее количество сообщений по всем пользователям
SELECT COUNT(*) / COUNT(DISTINCT id) AS average_messages_per_user
FROM messages