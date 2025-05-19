-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2025 at 08:53 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `c2c_freelance_home_cleaners_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `cleaning_services`
--

CREATE TABLE `cleaning_services` (
  `id` int(11) NOT NULL,
  `cleaner_id` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `postal_code` varchar(255) DEFAULT NULL,
  `rate` decimal(10,2) DEFAULT NULL,
  `rate_type` varchar(255) DEFAULT NULL,
  `min_hours` int(11) DEFAULT NULL,
  `available_day` varchar(255) DEFAULT NULL,
  `time_slot` varchar(255) DEFAULT NULL,
  `type_of_cleaning` varchar(255) DEFAULT NULL,
  `bring_supplies` tinyint(1) DEFAULT NULL,
  `languages` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `category_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cleaning_services`
--

INSERT INTO `cleaning_services` (`id`, `cleaner_id`, `title`, `description`, `location`, `postal_code`, `rate`, `rate_type`, `min_hours`, `available_day`, `time_slot`, `type_of_cleaning`, `bring_supplies`, `languages`, `created_at`, `category_id`) VALUES
(1, 2, 'week', 'asdaf', 'bbp', '123456', 10.00, 'hour', 3, 'wednesday', 'afternoon', 'regular', 1, 'eng', '2025-05-09 06:09:40', NULL),
(4, 2, 'asdf', 'asdf', 'asdf', '123567', 10.00, 'hour', 2, 'wednesday', 'evening', 'hello', 1, '', '2025-05-09 06:11:33', NULL),
(7, 7, 'yfy', 'asdf', 'asdf', '123567', 10.00, 'hour', 2, 'wednesday', 'evening', 'hello', 1, '', '2025-05-18 06:11:33', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `service_category`
--

CREATE TABLE `service_category` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `service_category`
--

INSERT INTO `service_category` (`category_id`, `category_name`) VALUES
(24, 'Deep Cleaning'),
(29, 'hello'),
(32, 'Ho'),
(1, 'Move-in/out'),
(28, 'Office Cleaning'),
(27, 'Post-renovation'),
(26, 'Regular Cleaning');

-- --------------------------------------------------------

--
-- Table structure for table `service_matches`
--

CREATE TABLE `service_matches` (
  `id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  `homeowner_id` int(11) NOT NULL,
  `cleaner_id` int(11) NOT NULL,
  `match_date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `service_matches`
--

INSERT INTO `service_matches` (`id`, `service_id`, `homeowner_id`, `cleaner_id`, `match_date`) VALUES
(1, 4, 9, 2, '2025-05-17 17:51:11'),
(2, 1, 9, 2, '2025-05-17 17:51:17'),
(4, 7, 9, 7, '2025-05-17 19:17:19'),
(5, 7, 9, 7, '2025-05-17 20:26:11'),
(6, 1, 9, 2, '2025-05-18 09:20:56');

-- --------------------------------------------------------

--
-- Table structure for table `service_views`
--

CREATE TABLE `service_views` (
  `id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  `viewer_id` int(11) NOT NULL,
  `view_time` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `service_views`
--

INSERT INTO `service_views` (`id`, `service_id`, `viewer_id`, `view_time`) VALUES
(1, 7, 9, '2025-05-17 20:19:19'),
(2, 7, 9, '2025-05-17 20:26:08');

-- --------------------------------------------------------

--
-- Table structure for table `shortlist`
--

CREATE TABLE `shortlist` (
  `id` int(11) NOT NULL,
  `homeowner_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  `saved_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `shortlist`
--

INSERT INTO `shortlist` (`id`, `homeowner_id`, `service_id`, `saved_at`) VALUES
(1, 8, 1, '2025-05-13 22:06:48'),
(2, 8, 4, '2025-05-14 01:01:24'),
(3, 9, 1, '2025-05-16 02:37:48'),
(4, 9, 7, '2025-05-17 19:31:44');

-- --------------------------------------------------------

--
-- Table structure for table `user_account`
--

CREATE TABLE `user_account` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `fullname` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `gender` enum('Male','Female','Other') DEFAULT NULL,
  `is_suspended` tinyint(1) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_account`
--

INSERT INTO `user_account` (`id`, `username`, `password_hash`, `fullname`, `phone`, `date_of_birth`, `gender`, `is_suspended`, `created_at`, `updated_at`) VALUES
(1, 'lol', 'scrypt:32768:8:1$tl2NvkS5LJSBgfxW$8b6f5cf2fe0ed477b764b9444e32926125ec7fa2221e977bd076b5314563a48bb305e7c1a4a74e64b250bcbf57ac2d8800eae4ce13b5a029d7f6164a8b3c6e42', 'tyutyu', '23960978', '1996-03-13', 'Male', 0, '2025-05-09 05:34:14', '2025-05-09 05:34:14'),
(2, 'fty', 'scrypt:32768:8:1$FBh8Ma9EG4w84NiV$f2bd5a559f1d943dfea2950769eba192ac6f94f7fc3b40a7777a88b410613d3f52887b9735dd8449ad2025617b9fed3a001e84345acd9f0449a2b5dba7e3bd31', 'ytutyu', '12396098', '1993-05-17', 'Female', 0, '2025-05-09 05:34:36', '2025-05-09 05:34:36'),
(3, 'asdf', 'scrypt:32768:8:1$YLSUgNI2Z07f0msV$82eea9d8ef64df86f3c0d5e138626fd3b93190eca1524217ba831a4fad0702344f5025ec4a0f69f85a4fa85870273ad31ee374ab2443788f2e8f7d578f93ba4b', 'susacctest', '56456854', '1999-05-17', 'Female', 1, '2025-05-09 05:38:01', '2025-05-09 06:15:16'),
(4, 'you', 'scrypt:32768:8:1$i3v4SQr3a1KNj2Iz$42458b484fc76cfbd0485eef62681ed6559e8b8c219685884d70929f2613ce18bb691f65135ab3ee678d746d46263955716313b170761363c8ee746aaa15711d', 'ertert', '34567890', '1997-04-30', 'Female', 1, '2025-05-09 05:50:45', '2025-05-09 05:52:47'),
(5, 'jkl', 'scrypt:32768:8:1$zN0KalyVbxHVnVMj$30eb30234a8f6e9c4951e0716a9351bb2eca9253b5562846bf1594a9e488932e3ef9e9961025c5eaf2bfdc92bbe002eac4ffab11563c094b99fddc8c7b3785f6', 'rtyy', '75869088', '1994-05-11', 'Female', 1, '2025-05-09 05:53:47', '2025-05-09 06:14:59'),
(6, 'fk', 'scrypt:32768:8:1$ZLSoYICx17thaE5O$94ffa8169cdec671aecb93e8b0658e89011d94ff663600252676886a65fba26ed7247dddba7e474074eb34f06f6021d58e1d587eaf67f998311dc43dbb95a651', 'trurty', '89098906', '1990-05-22', 'Female', 0, '2025-05-09 06:13:25', '2025-05-09 06:13:25'),
(7, 'cf', 'scrypt:32768:8:1$Ln5GIuBzOWDy6U9B$f914d40d0f2757ca67854fe120aeff48c5c76a96957e633e4a1aaceafbdaa597245ebc1e42eef2f121264a0b752393e94808bce15cb11b26eabda99627e28407', 'dsfsffddsf', '22652329', '1977-03-25', 'Male', 0, '2025-05-14 03:52:57', '2025-05-14 03:52:57'),
(8, 'dfdkfggfh', 'scrypt:32768:8:1$AF1s9MZhplySve8y$516fb80864e13a36f772c2e173c5c6357468db9edfe31e130d386e2f605feee19daa50011f16c071dc322cbe5ada9eb2c6b9da07a53a0482a240ea59207a2c69', 'hyvby', '59596312', '1997-07-14', 'Male', 0, '2025-05-14 04:17:37', '2025-05-14 04:17:37'),
(9, 'dfdkfggfhfgddggdg', 'scrypt:32768:8:1$ZovnP55bMsknTPbP$7f5631b0deb2337381fef726e97388dbd87e24343679ce1c39719b5db70c7042570a8fc9891a2e8b75720ef0fdc38e4e46a440d325e520345e579b92f6c0a3e6', 'fgfbghgfhfhfhh', '45242777', '1998-07-01', 'Male', 0, '2025-05-16 02:07:50', '2025-05-16 02:07:50'),
(10, 'dfdkfggfhvfgvgfgd', 'scrypt:32768:8:1$FBSZjGyIqPcUCXrI$3d7aaeb7a2bf672cc352f1837f10e401dc78f6ad47b4abfa2f6726810ccfdbdb0c5771ced4070022b7fe12de3b2b12b418d51978722b1849562fc726c3b2f751', 'xcvcxvxcvxvvxv', '45778669', '2003-02-22', 'Male', 0, '2025-05-16 02:19:04', '2025-05-16 02:19:04');

-- --------------------------------------------------------

--
-- Table structure for table `user_profile`
--

CREATE TABLE `user_profile` (
  `id` int(11) NOT NULL,
  `user_type` enum('User Admin','Cleaner','HomeOwner','Platform Management') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_profile`
--

INSERT INTO `user_profile` (`id`, `user_type`) VALUES
(1, 'User Admin'),
(2, 'Cleaner'),
(3, 'Cleaner'),
(4, 'Cleaner'),
(5, 'User Admin'),
(6, 'Cleaner'),
(7, 'Cleaner'),
(8, 'Platform Management'),
(9, 'HomeOwner'),
(10, 'User Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cleaning_services`
--
ALTER TABLE `cleaning_services`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_category` (`category_id`);

--
-- Indexes for table `service_category`
--
ALTER TABLE `service_category`
  ADD PRIMARY KEY (`category_id`),
  ADD UNIQUE KEY `category_name` (`category_name`);

--
-- Indexes for table `service_matches`
--
ALTER TABLE `service_matches`
  ADD PRIMARY KEY (`id`),
  ADD KEY `service_id` (`service_id`),
  ADD KEY `homeowner_id` (`homeowner_id`),
  ADD KEY `cleaner_id` (`cleaner_id`);

--
-- Indexes for table `service_views`
--
ALTER TABLE `service_views`
  ADD PRIMARY KEY (`id`),
  ADD KEY `service_id` (`service_id`),
  ADD KEY `viewer_id` (`viewer_id`);

--
-- Indexes for table `shortlist`
--
ALTER TABLE `shortlist`
  ADD PRIMARY KEY (`id`),
  ADD KEY `homeowner_id` (`homeowner_id`),
  ADD KEY `service_id` (`service_id`);

--
-- Indexes for table `user_account`
--
ALTER TABLE `user_account`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `phone` (`phone`);

--
-- Indexes for table `user_profile`
--
ALTER TABLE `user_profile`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cleaning_services`
--
ALTER TABLE `cleaning_services`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `service_category`
--
ALTER TABLE `service_category`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `service_matches`
--
ALTER TABLE `service_matches`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `service_views`
--
ALTER TABLE `service_views`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `shortlist`
--
ALTER TABLE `shortlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user_account`
--
ALTER TABLE `user_account`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cleaning_services`
--
ALTER TABLE `cleaning_services`
  ADD CONSTRAINT `fk_category` FOREIGN KEY (`category_id`) REFERENCES `service_category` (`category_id`);

--
-- Constraints for table `service_matches`
--
ALTER TABLE `service_matches`
  ADD CONSTRAINT `service_matches_ibfk_1` FOREIGN KEY (`service_id`) REFERENCES `cleaning_services` (`id`),
  ADD CONSTRAINT `service_matches_ibfk_2` FOREIGN KEY (`homeowner_id`) REFERENCES `user_account` (`id`),
  ADD CONSTRAINT `service_matches_ibfk_3` FOREIGN KEY (`cleaner_id`) REFERENCES `user_account` (`id`);

--
-- Constraints for table `service_views`
--
ALTER TABLE `service_views`
  ADD CONSTRAINT `service_views_ibfk_1` FOREIGN KEY (`service_id`) REFERENCES `cleaning_services` (`id`),
  ADD CONSTRAINT `service_views_ibfk_2` FOREIGN KEY (`viewer_id`) REFERENCES `user_account` (`id`);

--
-- Constraints for table `user_profile`
--
ALTER TABLE `user_profile`
  ADD CONSTRAINT `user_profile_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user_account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
