CREATE TABLE `preferences_accountsettings` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(150) NOT NULL,
    `email` VARCHAR(254) NOT NULL,
    `password` VARCHAR(128) NOT NULL
);

CREATE TABLE `preferences_notificationsettings` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT NOT NULL,
    `frequency` ENUM('daily', 'weekly', 'monthly', 'on-demand') NOT NULL,
    `email_notifications` BOOLEAN DEFAULT TRUE,
    `push_notifications` BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (`user_id`) REFERENCES `preferences_accountsettings`(`id`) ON DELETE CASCADE
);

CREATE TABLE `preferences_themesettings` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT NOT NULL,
    `theme` ENUM('light', 'dark') NOT NULL,
    `font_size` ENUM('small', 'medium', 'large') NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES `preferences_accountsettings`(`id`) ON DELETE CASCADE
);

CREATE TABLE `preferences_privacysettings` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT NOT NULL,
    `profile_visibility` ENUM('public', 'private') NOT NULL,
    `data_sharing` BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (`user_id`) REFERENCES `preferences_accountsettings`(`id`) ON DELETE CASCADE
);

INSERT INTO preferences_accountsettings (username, email, password)
VALUES
('user1', 'user1@example.com', 'password123'),
('user2', 'user2@example.com', 'password456');

INSERT INTO preferences_notificationsettings (user_id, frequency, email_notifications, push_notifications)
VALUES
(1, 'daily', TRUE, TRUE),
(2, 'weekly', FALSE, TRUE);

INSERT INTO preferences_themesettings (user_id, theme, font_size)
VALUES
(1, 'dark', 'medium'),
(2, 'light', 'large');

INSERT INTO preferences_privacysettings (user_id, profile_visibility, data_sharing)
VALUES
(1, 'public', TRUE),
(2, 'private', FALSE);