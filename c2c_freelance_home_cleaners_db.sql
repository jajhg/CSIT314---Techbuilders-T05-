-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2025 at 01:06 PM
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
(1, 2, 'Deep Cleaning', 'Deep Cleaning', 'Bukit Panjang', '739132', 10.00, 'hour', 3, 'wednesday', 'afternoon', 'Deep Cleaning', 1, 'eng', '2025-05-09 06:09:40', NULL),
(4, 2, 'WIndow ', 'Clean Window', 'Bedok', '820472', 10.00, 'hour', 2, 'wednesday', 'evening', 'Window Cleaning', 1, '', '2025-05-09 06:11:33', NULL),
(7, 7, 'Window Cleaning', 'Cleaning Window', 'Upper East Coast', '123567', 10.00, 'hour', 2, 'wednesday', 'evening', 'Window Cleaning', 1, '', '2025-05-18 06:11:33', NULL),
(8, 2, 'Regular Cleanup', 'Regular Cleaning', 'Jurong East', '567892', 32.00, 'hour', 3, 'tuesday', 'morning', 'Regular Cleaning', 2, 'chinese', '2025-05-19 09:37:24', NULL),
(9, 2, 'Post Reno', 'Post Reno cleanup', 'Woodlands', '249245', 23.00, 'hour', 5, 'saturday', 'morning', 'Post-renovation', 2, 'english', '2025-05-19 09:38:23', NULL),
(10, 2, 'Deep Cleaning', 'Deep Cleaning', 'Yishun', '940372', 24.00, 'hour', 0, 'friday', 'morning', 'Deep Cleaning', 1, '', '2025-05-19 09:39:36', NULL),
(11, 2, 'Office Cleanup', 'Cleaning of office', 'Orchard', '261472', 31.00, 'hour', 2, 'tuesday', 'evening', 'Office Cleaning', 1, '', '2025-05-19 09:40:22', NULL),
(12, 3, 'Deep Cleaning', 'Deep clean', 'Hougang', '729472', 35.00, 'hour', 2, 'thursday', 'morning', 'Deep Cleaning', 1, '', '2025-05-19 09:42:06', NULL),
(13, 3, 'Window Cleaning', 'Clean windows', 'Kovan', '483850', 20.00, 'hour', 1, 'thursday', 'afternoon', 'Window Cleaning', 2, '', '2025-05-19 09:42:44', NULL),
(14, 2, 'Move in cleaning', 'Cleanup for moving in', 'Punggol', '940274', 35.00, 'hour', 4, 'monday', 'afternoon', 'Move-in/out', 1, '', '2025-05-19 09:47:58', NULL),
(15, 2, 'Move out cleaning', 'Cleaning for moving out', 'Marine Parade', '654322', 30.00, 'hour', 3, 'monday', 'morning', 'Move-in/out', 1, '', '2025-05-19 09:48:45', NULL),
(16, 2, 'Office Cleanup', 'Cleaning of office', 'Serangoon', '194058', 34.00, 'hour', 1, 'sunday', 'morning', 'Office Cleaning', 1, '', '2025-05-19 09:49:43', NULL),
(17, 2, 'Reno Cleanup', 'Cleaning after renovation', 'Sengkang', '837456', 35.00, 'hour', 4, 'friday', 'afternoon', 'Post-renovation', 1, '', '2025-05-19 09:51:57', NULL),
(18, 3, 'Post reno cleaning', 'Cleaning up after renovations', 'Jurong West', '039692', 36.00, 'hour', 3, 'thursday', 'evening', 'Post-renovation', 1, '', '2025-05-19 09:53:00', NULL),
(19, 3, 'Regular Cleaning', 'Regular weekly cleaning', 'Bendemeer', '433445', 28.00, 'hour', 3, 'sunday', 'afternoon', 'Regular Cleaning', 2, '', '2025-05-19 09:55:08', NULL),
(20, 3, 'Moving out cleanup', 'Cleanup after moving out', 'Pasir Panjang', '859302', 35.00, 'hour', 4, 'saturday', 'afternoon', 'Move-in/out', 2, '', '2025-05-19 09:56:07', NULL),
(21, 3, 'Window Washing', 'Washing of windows', 'Serangoon', '379572', 30.00, 'hour', 2, 'monday', 'evening', 'Window Cleaning', 1, '', '2025-05-19 09:57:01', NULL),
(22, 3, 'Post reno tidying up', 'Clean up post renovation', 'Woodlands', '289905', 35.00, 'hour', 3, 'friday', 'evening', 'Post-renovation', 1, '', '2025-05-19 09:58:22', NULL),
(23, 3, 'Office cleanup', 'Cleaning of office', 'Bukit TImah', '387403', 100.00, 'job', 0, 'wednesday', 'morning', 'Office Cleaning', 1, '', '2025-05-19 10:00:49', NULL),
(24, 3, 'Deep cleaning', 'Standard deep cleaning', 'Paya Lebar', '234685', 28.00, 'hour', 2, 'tuesday', 'afternoon', 'Deep Cleaning', 2, '', '2025-05-19 10:01:56', NULL),
(25, 31, 'Moving in cleanup', 'Cleanup for moving in', 'Khatib', '299903', 35.00, 'hour', 0, 'sunday', 'evening', 'Move-in/out', 1, '', '2025-05-19 10:04:27', NULL),
(26, 31, 'Window Washing', 'Cleaning of windows', 'Tampines', '638249', 30.00, 'hour', 3, 'saturday', 'evening', 'Window Cleaning', 2, '', '2025-05-19 10:05:18', NULL),
(27, 39, 'Spring Cleaning', 'Spring Cleaning', 'Kovan', '485906', 12.00, 'hour', 3, 'thursday', 'evening', 'Spring Cleaning', 1, 'English, Chinese', '2025-05-19 10:33:18', NULL),
(28, 39, 'Regular Cleaning', 'Regular Cleaning', 'Jurong West', '689707', 12.00, 'job', 3, 'friday', 'afternoon', 'Regular Cleaning', 2, 'English, Chinese', '2025-05-19 10:34:05', NULL);

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
(34, 'Commercial Cleaning'),
(24, 'Deep Cleaning'),
(33, 'Gym Cleaning'),
(1, 'Move-in/out'),
(28, 'Office Cleaning'),
(27, 'Post-renovation'),
(26, 'Regular Cleaning'),
(31, 'School Cleaning'),
(32, 'Spring Cleaning'),
(29, 'Window Cleaning');

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
(6, 8, 4, 2, '2025-05-19 10:11:11'),
(7, 13, 4, 3, '2025-05-19 10:11:23'),
(8, 19, 4, 3, '2025-05-19 10:11:32'),
(9, 8, 4, 2, '2025-05-19 10:12:10'),
(10, 8, 4, 2, '2025-05-19 10:24:28'),
(11, 19, 4, 3, '2025-05-19 10:24:35'),
(12, 7, 4, 7, '2025-05-19 10:24:43'),
(13, 10, 4, 2, '2025-05-19 10:26:05'),
(14, 21, 4, 3, '2025-05-19 10:26:13'),
(15, 12, 5, 3, '2025-05-19 10:26:55'),
(16, 19, 5, 3, '2025-05-19 10:27:04'),
(17, 9, 5, 2, '2025-05-19 10:27:11'),
(18, 18, 5, 3, '2025-05-19 10:27:24'),
(19, 10, 5, 2, '2025-05-19 10:28:13'),
(20, 15, 5, 2, '2025-05-19 10:28:20'),
(21, 28, 4, 39, '2025-05-19 10:35:48'),
(22, 28, 4, 39, '2025-05-19 10:37:11');

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
(2, 7, 9, '2025-05-17 20:26:08'),
(3, 10, 4, '2025-05-19 11:00:43'),
(4, 11, 4, '2025-05-19 11:03:46'),
(5, 28, 4, '2025-05-19 11:04:05'),
(6, 18, 4, '2025-05-19 11:04:11'),
(7, 22, 4, '2025-05-19 11:04:17'),
(8, 7, 4, '2025-05-19 11:04:22'),
(9, 17, 5, '2025-05-19 11:04:34'),
(10, 4, 5, '2025-05-19 11:04:39'),
(11, 16, 5, '2025-05-19 11:04:46'),
(12, 18, 5, '2025-05-19 11:04:57'),
(13, 26, 5, '2025-05-19 11:05:14'),
(14, 12, 5, '2025-05-19 11:05:27'),
(15, 12, 5, '2025-05-19 11:05:35');

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
(4, 9, 7, '2025-05-17 19:31:44'),
(5, 4, 8, '2025-05-19 10:11:09'),
(6, 4, 13, '2025-05-19 10:11:22'),
(7, 4, 19, '2025-05-19 10:24:34'),
(8, 4, 7, '2025-05-19 10:24:50'),
(9, 4, 10, '2025-05-19 10:26:03'),
(10, 4, 15, '2025-05-19 10:26:21'),
(11, 4, 18, '2025-05-19 10:26:30'),
(12, 5, 12, '2025-05-19 10:26:54'),
(13, 5, 19, '2025-05-19 10:27:03'),
(14, 5, 9, '2025-05-19 10:27:18'),
(15, 5, 18, '2025-05-19 10:27:24'),
(16, 4, 28, '2025-05-19 10:37:19');

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
(1, 'UserAdmin1', 'scrypt:32768:8:1$tl2NvkS5LJSBgfxW$8b6f5cf2fe0ed477b764b9444e32926125ec7fa2221e977bd076b5314563a48bb305e7c1a4a74e64b250bcbf57ac2d8800eae4ce13b5a029d7f6164a8b3c6e42', 'UserAdmin1', '86385060', '1996-03-13', 'Male', 0, '2025-05-09 05:34:14', '2025-05-19 09:32:19'),
(2, 'Cleaner1', 'scrypt:32768:8:1$FBh8Ma9EG4w84NiV$f2bd5a559f1d943dfea2950769eba192ac6f94f7fc3b40a7777a88b410613d3f52887b9735dd8449ad2025617b9fed3a001e84345acd9f0449a2b5dba7e3bd31', 'Cleaner1', '87637070', '1993-05-17', 'Female', 0, '2025-05-09 05:34:36', '2025-05-19 09:32:35'),
(3, 'Cleaner2', 'scrypt:32768:8:1$YLSUgNI2Z07f0msV$82eea9d8ef64df86f3c0d5e138626fd3b93190eca1524217ba831a4fad0702344f5025ec4a0f69f85a4fa85870273ad31ee374ab2443788f2e8f7d578f93ba4b', 'Cleaner2', '90655730', '1999-05-17', 'Female', 0, '2025-05-09 05:38:01', '2025-05-19 09:41:23'),
(4, 'Homeowner1', 'scrypt:32768:8:1$i3v4SQr3a1KNj2Iz$42458b484fc76cfbd0485eef62681ed6559e8b8c219685884d70929f2613ce18bb691f65135ab3ee678d746d46263955716313b170761363c8ee746aaa15711d', 'Homeowner1', '99195654', '1997-04-30', 'Female', 0, '2025-05-09 05:50:45', '2025-05-19 09:42:59'),
(5, 'Homeowner2', 'scrypt:32768:8:1$zN0KalyVbxHVnVMj$30eb30234a8f6e9c4951e0716a9351bb2eca9253b5562846bf1594a9e488932e3ef9e9961025c5eaf2bfdc92bbe002eac4ffab11563c094b99fddc8c7b3785f6', 'Homeowner2', '92321518', '1994-05-11', 'Female', 0, '2025-05-09 05:53:47', '2025-05-19 09:43:01'),
(6, 'PlatformAdmin1', 'scrypt:32768:8:1$ZLSoYICx17thaE5O$94ffa8169cdec671aecb93e8b0658e89011d94ff663600252676886a65fba26ed7247dddba7e474074eb34f06f6021d58e1d587eaf67f998311dc43dbb95a651', 'PlatformAdmin1', '89098906', '1990-05-22', 'Female', 0, '2025-05-09 06:13:25', '2025-05-19 09:32:55'),
(7, 'PlatformAdmin2', 'scrypt:32768:8:1$Ln5GIuBzOWDy6U9B$f914d40d0f2757ca67854fe120aeff48c5c76a96957e633e4a1aaceafbdaa597245ebc1e42eef2f121264a0b752393e94808bce15cb11b26eabda99627e28407', 'PlatformAdmin2', '99517767', '1977-03-25', 'Male', 0, '2025-05-14 03:52:57', '2025-05-19 09:32:58'),
(8, 'UserAdmin2', 'scrypt:32768:8:1$AF1s9MZhplySve8y$516fb80864e13a36f772c2e173c5c6357468db9edfe31e130d386e2f605feee19daa50011f16c071dc322cbe5ada9eb2c6b9da07a53a0482a240ea59207a2c69', 'UserAdmin2', '85664744', '1997-07-14', 'Male', 0, '2025-05-14 04:17:37', '2025-05-19 09:33:05'),
(9, 'Ruth', 'scrypt:32768:8:1$ZovnP55bMsknTPbP$7f5631b0deb2337381fef726e97388dbd87e24343679ce1c39719b5db70c7042570a8fc9891a2e8b75720ef0fdc38e4e46a440d325e520345e579b92f6c0a3e6', 'Ruth Washington', '86931315', '1998-07-01', 'Male', 0, '2025-05-16 02:07:50', '2025-05-19 09:33:09'),
(10, 'Patrick', 'scrypt:32768:8:1$FBSZjGyIqPcUCXrI$3d7aaeb7a2bf672cc352f1837f10e401dc78f6ad47b4abfa2f6726810ccfdbdb0c5771ced4070022b7fe12de3b2b12b418d51978722b1849562fc726c3b2f751', 'Patrick Butler', '97367240', '2003-02-22', 'Male', 0, '2025-05-16 02:19:04', '2025-05-19 09:33:14'),
(11, 'James', 'scrypt:32768:8:1$35xUWEFbH4Ecd7qo$e11fa293d12c14471064d2447447f4e698ba9e66496e93cd3388e4642e19278e362351329a9d1c022c8dd0085bb445e0693dcecf9a13daf95476d52e2634725c', 'James Smith', '88290912', '1982-04-06', 'Male', 0, '2025-05-19 08:28:52', '2025-05-19 08:28:52'),
(12, 'Mary', 'scrypt:32768:8:1$wd1loyNfTjwi6egh$529071f63f87006b58345903de9e9116ea707e627b115b0ae1d0e8d7a3b12af526a16447cb9f6cec695dfede81ed8144f2a2b1a49901e315e1c6ce5c570d40f4', 'Mary Johnson', '86256951', '1942-02-10', 'Female', 0, '2025-05-19 08:29:59', '2025-05-19 08:29:59'),
(13, 'Robert', 'scrypt:32768:8:1$Nu132KobEYvM7XSY$6e7885caf8a4f488376d05939a7b62022009bfa10a538467d7a1547fcc12fe7a8b139e3741d48bd12d80136685944fe38b7e186a7f3403d563fbc5469cb0884f', 'Robert Williamson', '97483720', '1994-02-01', 'Male', 0, '2025-05-19 08:30:51', '2025-05-19 08:30:51'),
(14, 'Patricia', 'scrypt:32768:8:1$lzgz0l0uf3XaRkjV$e5fd6a6e23a3239ac59f91829259d0444273b26f0d712c1832705dbf612d11ea39d48b40f6c64986f84ca8ba7f0518dab628598f2cf0be006a9af3c703e917bf', 'Patricia Brown', '96881722', '1976-04-24', 'Female', 0, '2025-05-19 08:31:44', '2025-05-19 08:31:44'),
(15, 'Jones', 'scrypt:32768:8:1$CsPboxwGNnhI5CFu$6219bd90aede5f48bcef38a2956ec281608fe6a6c19c875c78a92ea8c879f292213fc3f9b0675350bf1642ecec4ae927e8785193704d7577d9509f56d6c0066b', 'John Jones', '80291944', '1943-07-11', 'Male', 0, '2025-05-19 08:32:34', '2025-05-19 08:32:34'),
(16, 'Jennifer', 'scrypt:32768:8:1$e8iXlAkUr83JttcP$0f7a13be733bdceea16ef0cb709a090535d80503ee1999071f33c678cfa31c68693c43166b373e538d2359b87f53971f62952c844a50b665d92b372bbbbf4f83', 'Jennifer Garcia', '81328355', '1951-09-15', 'Female', 0, '2025-05-19 08:33:52', '2025-05-19 08:33:52'),
(17, 'Michael', 'scrypt:32768:8:1$YDqMg8Y8pTHlgvle$5418915e25b6258cc36fc64199d284b22f6ef6bce480eb50d8313659e4ebd3956dc3fbad8d720e8060cf01cd6580366165fd337021a21b8e1adf08ff4d1a0b56', 'Michael Miller', '91086614', '1989-11-07', 'Male', 0, '2025-05-19 08:35:09', '2025-05-19 08:35:09'),
(18, 'Linda', 'scrypt:32768:8:1$5wmw4SNVcky6xm1r$d201b676176fae9a00ed1b0baf42b4b217af079282de0ff060003f4c1989e7fbc5ddd4eeeace6a026841ae703a758f2f066281ccca69f03b1dd0ddc9efe0e333', 'Linda Davis', '87166888', '1998-01-16', 'Female', 0, '2025-05-19 08:35:58', '2025-05-19 08:35:58'),
(19, 'David', 'scrypt:32768:8:1$LzuouDaJRxkALU0s$a7b45e8b622b270d6ee7d17e117e9fdeeced8ba431f56469e5c1236facda41b59770c155296965517f11dfa65f7f8ce497d1a257eb34ae951b71bdf879abec76', 'David Rodriguez', '86362938', '1935-10-12', 'Male', 0, '2025-05-19 08:36:51', '2025-05-19 08:36:51'),
(20, 'Elizabeth', 'scrypt:32768:8:1$zArxee1nQsxeMyvk$157205c988ff25b05d0d4b872338887dd9dd40a879cac88d56ae9f634e1580f550b68467a46b990d005e6f69135f721f9e636d107ec70b9143949d06425af8ce', 'Elizabeth Martinez', '83833032', '1998-08-25', 'Female', 0, '2025-05-19 08:37:55', '2025-05-19 08:37:55'),
(21, 'William', 'scrypt:32768:8:1$xdUmXx0Ia4awNLwH$32b4925ba237deeaa4d720b1c69619f6406b57b1e3a37b6a538a8620be47b0337e952920d755ae51a209de07644af23b049d0e45cb4b6b0d980314fe53c62c67', 'William Hernandez', '96881636', '1985-10-26', 'Male', 0, '2025-05-19 08:39:08', '2025-05-19 08:39:08'),
(22, 'Barbara', 'scrypt:32768:8:1$TqkdhJnyi0GJ0IeP$bbbedcc58817ab13e48e11d9873072c3b5e42affbf18ed003a9f3d9ca117ac430d46929590c82e1c64488635a3f75c6acb5889b33933faf17d3c4085158b281b', 'Barbara Lopez', '86961084', '1955-07-05', 'Female', 0, '2025-05-19 08:39:42', '2025-05-19 08:39:42'),
(23, 'Richard', 'scrypt:32768:8:1$od9UQ259UiDpw75z$c8a151bda8d83db64eef576c1b44ddd4dcc49de82f62169f605a643f6ad19975439bd6919c648d161ab41fa5c5697772b2d526a6ba38bfb20aca838d55a0d0c8', 'Richard Gonzalez', '80209743', '1937-07-15', 'Male', 0, '2025-05-19 08:40:15', '2025-05-19 08:40:15'),
(24, 'Susan ', 'scrypt:32768:8:1$lbQsEJhzB5yfWrbw$58500bab90290046746805fb9740e6fceb0469e415126926b93dec0bfa473ab57ce2d727231f03a15a0035c2ae02c6ace16cd941decf24a2c5ddbb83f02daf33', 'Susan Wilson', '88990477', '1984-06-08', 'Female', 0, '2025-05-19 08:40:48', '2025-05-19 08:40:48'),
(25, 'Joseph', 'scrypt:32768:8:1$cQe5uTfwrrF6wZBN$5b995c36c909a4102664e59351a20d127ec305f8e4d103113b83c97d7f635b7c7eb4870c811a1fc24668a991b7c32cd8dd1d1f207e7217a473034d190fcfa48f', 'Joseph Anderson', '91611552', '1960-12-26', 'Male', 0, '2025-05-19 08:41:29', '2025-05-19 08:41:29'),
(26, 'Jessica', 'scrypt:32768:8:1$BcU6AfHPBgRlA24P$723833811c8080545f822de27623d6a183e8c4496a073d93fe205ea41b5c0f1754a552afa59a0c3ca1a96daa798bd4fbf9ff9fc17967a52fa1de065bea868b32', 'Jessica Thomas', '81925027', '1962-04-01', 'Female', 0, '2025-05-19 08:42:18', '2025-05-19 08:42:18'),
(27, 'Thomas', 'scrypt:32768:8:1$H4FIVa7uQklCD8U5$b6325ad3d1f0073ede044d0387fc693b53411cd467b7a298a89330aa628d3da1b6ed726dd87fdf5b1ea02e7bd171807fe94a0ec7a968fa888155a74b5e9c6b30', 'Thomas Taylor', '84742113', '1950-01-05', 'Male', 0, '2025-05-19 08:43:01', '2025-05-19 08:43:01'),
(28, 'Sarah ', 'scrypt:32768:8:1$dEesVcwtsrjZURQO$c7bed18dbe194091a96b7fc8f15839848722c8fa58d7bad47730d38ac2b06a9ea044cc7fcc26180da70ee8bfa9f72c8fb326cdb249a121fa467d80646742bcbd', 'Sarah Moore', '82305045', '1983-09-12', 'Female', 0, '2025-05-19 08:43:30', '2025-05-19 08:43:30'),
(29, 'Charles', 'scrypt:32768:8:1$zyalYEVSnvrE0oLt$b252a5ffcce9c0e90521fc39afa126c7421ceb47264d42d894d132e3ac60a777cac6038dade3f664640af4f937960f350ca061fd751fe27c0de3af3bef09b222', 'Charles Jackson', '88729055', '1943-02-18', 'Male', 0, '2025-05-19 08:44:01', '2025-05-19 08:44:01'),
(30, 'Karen', 'scrypt:32768:8:1$4LYP7d02EchTtkLn$c9b9e05ffb087804c3830ff22e477999a4468f28fc5690382c8d242f439a20ed353069ce4874226df6f60d5d3c4d15a31293457dbd03d1dd3c73951b3033b55c', 'Karen Martin', '80004702', '1952-08-23', 'Female', 0, '2025-05-19 08:44:43', '2025-05-19 08:44:43'),
(31, 'Christopher', 'scrypt:32768:8:1$OOOMAs0SEwUFizjj$05b940a29515749d18551decebe36be0d9ad7fd24b49c13c6bdc27126e156821fdbc2046536fb54ba141095d985ebc2c849a9deb6e28215cc159b0a328a13482', 'Christopher Lee', '80262379', '1949-12-23', 'Male', 0, '2025-05-19 08:45:15', '2025-05-19 08:45:15'),
(32, 'Nancy', 'scrypt:32768:8:1$tn7jKckJuE2kUG5W$c976adae35214482dbe2d0d843f808f099d7a9c270efc7511941fdbbd0a43970de5385e9d06483d03b102f7fb77de2b327b31d1663c28ce8bd1978125c7b15f2', 'Nancy Perez', '84470803', '2000-02-24', 'Female', 0, '2025-05-19 08:45:48', '2025-05-19 08:45:48'),
(33, 'Daniel', 'scrypt:32768:8:1$ZLhBe9rXY0rHnUZn$1a4938bb72c6a0967e4f44e7fd32868548a4c1d6185b5ceb1d3d4268b30740911f1c3d0d79281efd394bc9169276648fbee6fd586559bdb1d6e54db312597f6b', 'Daniel Thompson', '97768679', '1970-12-25', 'Male', 0, '2025-05-19 08:46:31', '2025-05-19 08:46:31'),
(34, 'Lisa', 'scrypt:32768:8:1$vfzx79Y9oWy5saH7$4c5a64b914058f90572b2353c28238bf8bdd02fe3f5e4e39b70464b782cf18be0eaa8767d0a71cee2b383c03cebbf21559d55552b2296efc5a1e83ede0b17a91', 'Lisa White', '89691899', '2001-05-10', 'Female', 0, '2025-05-19 08:46:59', '2025-05-19 08:46:59'),
(35, 'Matthew', 'scrypt:32768:8:1$ebMK7HOyTZHr1Zyv$a4fbb71e38c2b4e63eb0a0c938eb841936b98179fb89554732b6ccb800e24470b264d9e54cea38bbe9008430bee04f961ff2ebef6db50b687c9fbdaff89b18cd', 'Matthew Harris', '93021646', '1970-07-24', 'Male', 0, '2025-05-19 08:47:29', '2025-05-19 08:47:29'),
(36, 'Betty', 'scrypt:32768:8:1$qhNpap1Ehqt3CTEI$96f625272834d11b9290b6e37143ddb4ec8139fcb6959d5236f31658480c9746448192379faf6fc80bc8c264a62560a60779e6730ecb5206e57dc9321050e29a', 'Betty Sanchez', '92782479', '1935-10-02', 'Female', 0, '2025-05-19 08:47:57', '2025-05-19 08:47:57'),
(37, 'Anthony', 'scrypt:32768:8:1$O8vUGgjYhKgVY2j1$abfdc4c0b4c47d2ad70fe1456d10bab52f523b00030af3f9360e1c7a2f33aca74a85ef56279fe6508f869eb2572d61e5050dbde12cf91401ee81e39770fe85c0', 'Anthony Clark', '81141747', '1964-04-30', 'Male', 0, '2025-05-19 08:48:32', '2025-05-19 08:48:32'),
(38, 'Margaret', 'scrypt:32768:8:1$AwTDxwMzRRQggYr2$5d66bdd9376d106126ebc410de72fecbf295398f8d55990b2111b57b89f1a1fd5325d1aeccfe330f56ece352f91cb98e648b92b7b09e48de93330dee7ed37324', 'Margaret Martinez', '94966395', '1987-05-04', 'Female', 0, '2025-05-19 08:50:04', '2025-05-19 08:50:04'),
(39, 'Mark', 'scrypt:32768:8:1$rQ0nomNNHOdQqDFO$ffd5e7b90b2fb8e655566567d33c119606ec2966e3d0c39f6fb2088d93f8a33f451f61fec24f54a51418d81adcb71ffceb902aa881322c27610a73d3b4f3a5f2', 'Mark Lewis', '86108472', '1937-06-25', 'Male', 0, '2025-05-19 08:50:33', '2025-05-19 08:50:33'),
(40, 'Sandra', 'scrypt:32768:8:1$1b9xz86SCP5g1psW$7aca5878b73f3b9b7278b2226a280e9a7b729627f9322d45df72d5a56a1061686ef5ac5ec284cef37bf6461cee7494c51c4bf84b330bcec90056677d62ca76f1', 'Sandra Robinson', '98702935', '1992-02-11', 'Female', 0, '2025-05-19 08:51:03', '2025-05-19 08:51:03'),
(41, 'Donald', 'scrypt:32768:8:1$kEJkZuvREHc2oMQ2$cb75ed403ef8e755eaacbfdeefc28e4c88c9ac0b56bdea0501d1bf43f9eaf67cc60172d7b3c1f948bbb82ac316e1793780e56a28b7f3b8d273460ab3b89d9d33', 'Donald Walker', '91328295', '2002-09-30', 'Male', 0, '2025-05-19 08:51:36', '2025-05-19 08:51:36'),
(42, 'Ashley', 'scrypt:32768:8:1$ppDXbJL2J6jOmN9p$d30c04c0363c9e7cefb19570dab30d6ddb26a60202fb37393e628636f071f0914ccd05b396e80b788f274f824f5230651f9613ec51580ad968dcf5de227aa5d1', 'Ashley Young', '97748756', '1949-02-20', 'Male', 0, '2025-05-19 08:52:08', '2025-05-19 08:52:08'),
(43, 'Steven', 'scrypt:32768:8:1$dk03lAAmzMQ6vn60$55228d87fdffd29af909670fce6858cad35506dce317925e1b3d7a08993f8d290960b02d597b1750ddbf794b145918d740319ac59e013c3cb00cd9167eaefdc0', 'Steven Allen', '95083784', '1950-01-14', 'Male', 0, '2025-05-19 08:52:43', '2025-05-19 08:52:43'),
(44, 'Kimberly', 'scrypt:32768:8:1$qB3rBp0Y1ooO4PCx$ce5873775bed8e84363ceee50237e5a2d5f43e8696701cd6836c4b0b052d26b2ece9ef3954e456c70cb4ce4501e52cec3a627021a115eca029833d05ea876769', 'Kimberly King', '98828673', '1999-07-21', 'Female', 0, '2025-05-19 08:53:10', '2025-05-19 08:53:10'),
(45, 'Paul', 'scrypt:32768:8:1$fdFLSps4GG8udINy$55a8672b603e93b357647540d0cc189f1b4cacbbf2d8d65968974ffe15fffbf6e9fbc25880aa04d03575e8367d33abf5a4bef00f83485b94955659f573382b02', 'Paul Wright', '93760005', '1988-04-19', 'Male', 0, '2025-05-19 08:53:37', '2025-05-19 08:53:37'),
(46, 'Emily', 'scrypt:32768:8:1$FYPAN2EXF8ipkJaf$dcb4f7c8a9be43ec322c077a025b97d538cd567bc8ba5c7fe4581b8c862a01b1d7034ca0467ebaff33009509c81097212280c1517fd8eb004ab4e6f7ac26f66a', 'Emily Scott', '85388264', '1956-02-02', 'Female', 0, '2025-05-19 08:54:23', '2025-05-19 08:54:23'),
(47, 'Andrew', 'scrypt:32768:8:1$8zHbi8z0VEeqmR5y$7fa305a4400ef697a2f7b7afa3edc01b6aa0259754f6642c3c7af8c1cc149ee83c85e3d6adafaa5da4c0b69f5f91a44331f6f39d0619a2e1da05a05f82b8055c', 'Andrew Torres', '84573472', '1993-07-02', 'Male', 0, '2025-05-19 08:55:05', '2025-05-19 08:55:05'),
(48, 'Donna', 'scrypt:32768:8:1$n8xct7DRWTFJg2X9$5f812bd3e9c664d31da646065ec597d806775c16c65a5e3040bc039807fde011291cf97ff14759f18bde7cdbb9e3d3236f64cd4b9bc18575a069b1aaf1820552', 'Donna Nguyen', '83099526', '1985-04-17', 'Female', 0, '2025-05-19 08:55:55', '2025-05-19 08:55:55'),
(49, 'Joshua', 'scrypt:32768:8:1$8NqAPVJX9IjPBxnX$2aaaf49131226cd2e53d3449ece6e184582e8304aca20d3874ed54e86bc0a546db71e8ab6e70563434aa1eb93b436aa342bb81850c75ba563f89c14598e6ae97', 'Joshua Hill', '86010674', '1977-06-17', 'Male', 0, '2025-05-19 08:56:30', '2025-05-19 08:56:30'),
(50, 'Michelle', 'scrypt:32768:8:1$WtoVpyIg2GrwXko4$c1e2544d167823e0207ff09d0540267fa420ee56608a5d0774025f12f59ff3bfbcadfa6f2b85cc37f7d1caebc6c9edbee520b38321221a0ad1bbf701ddcb0097', 'Michelle Flores', '87543735', '2002-12-08', 'Female', 0, '2025-05-19 08:57:01', '2025-05-19 08:57:01'),
(51, 'Kenneth ', 'scrypt:32768:8:1$5my9rR1C2BjaBArB$54c4eb4423acc9ab6471407fd3f8c64d9f581c4fdeb8ce613e891b78db5cc251cee019f06d7666b098ce23bfcf926866c2466caf968a59856f9c2bff84adcd8d', 'Kenneth Green', '83025306', '1998-03-29', 'Male', 0, '2025-05-19 08:59:59', '2025-05-19 08:59:59'),
(52, 'Carol', 'scrypt:32768:8:1$kixo8fxAd7dMqLwt$4c9970eca17c7108721723a0da472012c2c093b19f2334fc5adb17118460a70b2eab9cfee519cda457e0a7b43c2215b80ef37e86f9f1f894a83fe8c99244cad8', 'Carol Adams', '92544507', '1994-04-26', 'Female', 0, '2025-05-19 09:00:28', '2025-05-19 09:00:28'),
(53, 'Kevin', 'scrypt:32768:8:1$x0Urq54EygMl4pWG$d1a2f1a444093d64461f3639fc64f5e276bba86fee430f6426f18becbdf216500cedc8488dbc543a0f352bc98f2365b9dce615b5d3fe1c6d36a3c002c2b175ad', 'Kevin Nelson', '96440337', '1960-10-20', 'Male', 0, '2025-05-19 09:00:55', '2025-05-19 09:00:55'),
(54, 'Amanda ', 'scrypt:32768:8:1$OtMNudLSPJLQa4ZK$11ac42cf02c108dd8273d0a47930702404c4d95ca140f76fa09db679c23e4ec8e5ba7f5fc6d5e723ef34dafe199632f0c51c2395acb8491fa592d3e51d00a4bf', 'Amanda Baker', '99302935', '1992-09-07', 'Female', 0, '2025-05-19 09:01:26', '2025-05-19 09:01:26'),
(55, 'Brian', 'scrypt:32768:8:1$g5HOIxW5Mw41IzXD$77d291e6b074f6aa4e27f97ec6dae06330d4bb20fd5e3c65b3cea172fea7ea0167e358bb3409d842041990186d59ce702323178006a8c46664e9cf215d968f1f', 'Brian Hall', '90854095', '1970-12-21', 'Male', 0, '2025-05-19 09:01:57', '2025-05-19 09:01:57'),
(56, 'Melissa', 'scrypt:32768:8:1$4Dvo2uwKKpRcxnxi$583cb5054b9e7870bc5e919138823e41071b53d6148cf8c7a09309e06d02bbfd3194dda76e3e3e2a9dbaf02e15fc8930dffd82b0b840a807c5aaa213f112ba3c', 'Melissa Rivera', '81276708', '1973-01-09', 'Female', 0, '2025-05-19 09:02:32', '2025-05-19 09:02:32'),
(57, 'George', 'scrypt:32768:8:1$2YWdAqHHClPpR7LM$6b12073013c210c9bd8c68208ae1ecbc71344e7ac4056fece71e6255cd319ebf5c7d31fc201a147d0498f8b1d6411b2c06c1ce701bd0122dfb5b978b2058a993', 'George Campbell', '87170672', '1976-09-23', 'Male', 0, '2025-05-19 09:02:59', '2025-05-19 09:02:59'),
(58, 'Deborah', 'scrypt:32768:8:1$Nu7q160RYc47RGQF$e4afa86d5799116040b6527f36b7722a46250e1c7f0c430de8bfb1a5fd2a597a77c7bb98ba83ba30fabe731ad09f07d068892eab3c3219a1caaeb4c5e245a7c4', 'Deborah Mitchell', '96503761', '1977-11-24', 'Female', 0, '2025-05-19 09:03:41', '2025-05-19 09:03:41'),
(59, 'Edward', 'scrypt:32768:8:1$K5PMPmh6oBN5DeSW$a523b335c873e7aa7d02a7b77536c46dae78e905913585c6b12566311868c12282dc1ccb291442762996713aef092859d6beeb52f3be6405a3a2fa718aa3e010', 'Edward Carter', '92271560', '1990-05-13', 'Male', 0, '2025-05-19 09:04:09', '2025-05-19 09:04:09'),
(60, 'Stefanie', 'scrypt:32768:8:1$SVGyFPFaNaba5sy9$7f71517a8830fd8b6ff6cc0a3b7ba86794efd029da76043358a240cba01a3a63ad4f61ca883f0e1f941fb79e7570f599fd3eca605faf988ec2ff4223bb0a27d3', 'Stefanie Roberts', '90839269', '1990-03-12', 'Female', 0, '2025-05-19 09:04:37', '2025-05-19 09:04:37'),
(61, 'Ronald', 'scrypt:32768:8:1$mrCpRcQ5aoovP1BN$10f8d2066c89d2d6d56ab975fee0afed7bbd38e2f57e90e820642b99aab8dddc78fec356e3c133e95d4721edb2ba6bd7e278b8f441bc2b43121e15c566ab4138', 'Ronald Phillips', '83937161', '2004-04-16', 'Male', 0, '2025-05-19 09:05:16', '2025-05-19 09:05:16'),
(62, 'Rebecca', 'scrypt:32768:8:1$LrhxxD8FaEa0jBm3$f881fe2dd93955128a01bda4db76d0edd3df7b957f9813fd295e60dc742d9508c9e93f4494d867969705505f3a862b5a43082b5732c1021758c4464255ec8892', 'Rebecca Evans', '87848556', '1962-08-15', 'Female', 0, '2025-05-19 09:05:51', '2025-05-19 09:05:51'),
(63, 'Timothy', 'scrypt:32768:8:1$4PA9DyfVYUuo1b3Q$05a5c8ebed2307efac49b956feee89b0f83267e340a075a53d01a33f6ae29542e807f8fcf026bfebb7842f69b0181f4565fcfc968da0b25ba22ffc3e3610183c', 'Timothy Turner', '96493537', '1943-01-14', 'Male', 0, '2025-05-19 09:06:17', '2025-05-19 09:06:17'),
(64, 'Sharon', 'scrypt:32768:8:1$iGOUcjUJBHlWwngV$4ab430646e77745ffead5cd42f4228618bf62a19a84110afe9a69f7a4a8da5f45fd31401f9243c74ba4eedf9ae75e6ad697308728c331b09205f796268c99d43', 'Sharon Collins', '83265637', '1951-01-08', 'Female', 0, '2025-05-19 09:06:52', '2025-05-19 09:06:52'),
(65, 'Jason', 'scrypt:32768:8:1$MwKUcsz7dnek7Z0x$59b1428a84ddd8587363a048225001d38a50dcbe365deb8ba773e689f73f2a34466e45f103daec2008a5bed9f44209de9b861fa057674693e984b97d94f14ade', 'Jason Parker', '84656315', '1950-01-24', 'Male', 0, '2025-05-19 09:07:18', '2025-05-19 09:07:18'),
(66, 'Laura', 'scrypt:32768:8:1$x5qQkHiO2zrDURy9$ad5d08eb6e70bdffeac221e913adbe00015f9fd0643848254c9abe02f9e9f815d3d874e1e8a1d58af3289bcc56b4c3ae41e58ab2aaf1ea8e3530ab2839f26278', 'Laura Edwards', '92228048', '1991-07-12', 'Female', 0, '2025-05-19 09:08:02', '2025-05-19 09:08:02'),
(67, 'Jeffrey', 'scrypt:32768:8:1$nn5azWNIX0vvJKLm$10fae396ca0201419e74e1b7433abf6f4d465f89de3da78daedb3fec2b1c71498811c27b2c1846bea6c5023815b10555471d64f74cd1bf59a006415d73f19f29', 'Jeffrey Stewart', '81093419', '1960-12-18', 'Male', 0, '2025-05-19 09:08:35', '2025-05-19 09:08:35'),
(68, 'Cynthia', 'scrypt:32768:8:1$WuSe3bE8V5VJgk4f$23bc6f5d2a0e7fa5f185f354e3dda3d75a4779da9df3c10da0858801f13a5b98248f191992fe5e3eb6d4e8820a9022803a5f0db899a72925595fff8045855046', 'Cynthia Morris', '86196014', '1999-03-26', 'Female', 0, '2025-05-19 09:09:21', '2025-05-19 09:09:21'),
(69, 'Ryan', 'scrypt:32768:8:1$4d8RtarybPEKFhqf$a374f1221a853aeb28e689ad662860e9d54a86042ed147edfa300537f65ec45fb6bfc7294974ba4c6f7b18de9fa89c994116dca606db611dd175ad077da9ae88', 'Ryan Rogers', '99812571', '2005-06-03', 'Male', 0, '2025-05-19 09:09:46', '2025-05-19 09:09:46'),
(70, 'Kathleen', 'scrypt:32768:8:1$SSTqDfhbXnJjKsiJ$3c5fcb7fab2efb337652537354135c51c9408511496476343586799404681c96ea99748e493a534081472176d768c841909eca2bb567d618ed8d5c4ed6d0778a', 'Kathleen Cooks', '89085473', '1982-03-11', 'Female', 0, '2025-05-19 09:10:25', '2025-05-19 09:10:25'),
(71, 'Jacob', 'scrypt:32768:8:1$jItYgYLesRsvT4oW$38e436284339f6c986b0ffde137a9aaedff76037f04270e9f82f47e6c73ebaed1d0aa3d996d4ed9c5e19341bdace0a82b27f55d6f1678fb21fac2a256daa45a8', 'Jacob Morgan', '90917301', '1991-03-19', 'Male', 0, '2025-05-19 09:11:33', '2025-05-19 09:11:33'),
(72, 'Amy', 'scrypt:32768:8:1$jevuQIWWZZ458PO9$22249fd1bc076aed32d281010f5c19144a38f162a6409f5e57e974035cac99187c731d2cfe9f8b60eac8956637b555c35a2738ab3a686a993a9c25f5963e40fb', 'Amy Bell', '98427919', '1992-09-04', 'Female', 0, '2025-05-19 09:12:00', '2025-05-19 09:12:00'),
(73, 'Gary', 'scrypt:32768:8:1$NOovNvF0bUDkXYA4$8cf379f8f5a7a4609530d33bc0b1ea8f8e375b79cb235d9e44e5f8497597ab91406efb8ee0aee0ee22914651e6b3d193f0890b0639985cba5f86d72975299949', 'Gary Murphy', '92087546', '1980-08-13', 'Male', 0, '2025-05-19 09:12:26', '2025-05-19 09:12:26'),
(74, 'Angela', 'scrypt:32768:8:1$4bZFfNAG8op1ghqm$326863494b76ff76d9614f5386fded510df85f5f3c963979c799d3dc83111c639340b0efe47f12d3874e8e9b3a7d9f42999deda750344637ae57ed51da4fd04b', 'Angela Bailey', '80583669', '1999-07-23', 'Female', 0, '2025-05-19 09:12:56', '2025-05-19 09:12:56'),
(75, 'Nicolas', 'scrypt:32768:8:1$9FuArq4187oBMurN$6b165ea5a4d235cd8df34c533df000a103d44c15bad546b28618232515946a9d4f69ca7a06537727cb20dfe0b4464103a7afaf2cc7da569628eff1c51bd89a3f', 'Nicolas Cooper', '96963979', '1956-12-19', 'Male', 0, '2025-05-19 09:13:24', '2025-05-19 09:13:24'),
(76, 'Shirley', 'scrypt:32768:8:1$q0jeTjMzDMHItL2G$55fe2ed8bed98500c801ffe2f2a65e01ca5fa4e63a3ad6e08ffe58f1bc959e8f4ecf545a42a6b0e5cd44ee6a8452c17b5072c32bfdef839a44e8b1456ce2942c', 'Shirley Richardson', '92819982', '1976-04-19', 'Female', 0, '2025-05-19 09:13:59', '2025-05-19 09:13:59'),
(77, 'Eric', 'scrypt:32768:8:1$W6Fr5G1IxoN79vNn$a7d33baa0f7efe6aeb55403e29bace0f4a79729d91c289dee585f85ffb2b9a7460528d0a3aa3b52b9f13a2293d4101daf53c35bc01a2836a4058f62948cd3ce8', 'Eric Cox', '81158775', '1985-09-02', 'Male', 0, '2025-05-19 09:14:22', '2025-05-19 09:14:22'),
(78, 'Brenda', 'scrypt:32768:8:1$Zkty1IPII9SqqLJv$c3572ec3a9b74828eb803959c6175b56854287ab09b6f653ad295e56db77f249f324ca6a4b50f81836a861dfc475bf35942165ad56cf14c043060b593caa5a13', 'Brenda Howard', '80440704', '1958-07-30', 'Female', 0, '2025-05-19 09:14:52', '2025-05-19 09:14:52'),
(79, 'Stephen', 'scrypt:32768:8:1$k1mbJUtPRnf358cl$ccfbf4536555a630a4c399853ec82482d8c1f974ccaaee12563f1c87e335f14a34059133fca29de9bdd4d9612392f484207b2f4046b9bc8c3ae3072ef978ab6b', 'Stephen Ward', '98447931', '1967-11-02', 'Male', 0, '2025-05-19 09:15:20', '2025-05-19 09:15:20'),
(80, 'Pamela', 'scrypt:32768:8:1$zxPdjIuXilx6ydXa$5b217a80189c9d9d757ce7c9b262c0144c91629ae698f60ae859054d9780cc3a8f2a2de7b853ec73442436c8bc1c7509ab291b9a105932658ca33a2c614b8efe', 'Pamela Torres', '98401302', '1959-07-17', 'Female', 0, '2025-05-19 09:15:55', '2025-05-19 09:15:55'),
(81, 'Jonathan', 'scrypt:32768:8:1$X9daRSI4JwQ8KzdK$1ec7ebf53b7f9ad4ac9ced132c68874bd57d26ff05a1132c2eaff57c61e2c0176f1476d113aac59d3ddb2a6e3a1cbb632984617005ee31469656653c27876728', 'Jonathan Peterson', '81572706', '1975-04-09', 'Male', 0, '2025-05-19 09:16:45', '2025-05-19 09:16:45'),
(82, 'Emma', 'scrypt:32768:8:1$dXJUxKzaggDwLvUU$12560e995828425a59fed1d53d78ddbeed01dae12cdadacda90c526bdb3ab6482d835397db3e5d9db8b2f3a91b35f0efd61a1e4afe9ea0dd25fdc4f7ce6d1efb', 'Emma Grey', '92067514', '1999-06-03', 'Female', 0, '2025-05-19 09:17:09', '2025-05-19 09:17:09'),
(83, 'Larry', 'scrypt:32768:8:1$25gAfZiEquKtb2PL$d11783510e492f5c0f8c5ac7bda2c74f651e200591abe783c5aed4092d4ce292ce3b9114d614510259e8dbeae93cc9bfc5680f0c4ce2ac44bc26de503ccc3d9b', 'Larry Ramirez', '97427219', '1972-09-22', 'Male', 0, '2025-05-19 09:17:35', '2025-05-19 09:17:35'),
(84, 'Janet', 'scrypt:32768:8:1$LIycyYjXcUVaLrOV$517ad31e834b40500c7898ba6fec646c5e4a718dea92d8909597b3290071631eedefd952b38a299794c69147c72aa0e2b16c0dcf7e883d7499b3660b171d4ca7', 'Janet James', '99760363', '1983-04-22', 'Female', 0, '2025-05-19 09:18:01', '2025-05-19 09:18:01'),
(85, 'Justin', 'scrypt:32768:8:1$a210SCqTt21yoBug$c3d50b1cfeb9eb55ba046a7e49f5f9da860ac7cd051302599374a026534de1c01df0aa9c5bbd426ea7af2cc8d2f091902390b900736d0ab9ee978fc81e8930b5', 'Justin Watson', '86527086', '1966-09-27', 'Male', 0, '2025-05-19 09:18:29', '2025-05-19 09:18:29'),
(86, 'Rachel', 'scrypt:32768:8:1$HU043mMoYRK3g8os$57be8f655bccdbde457493db34f536e88378dd647c90ab345c350e2a9ef56216ace995cacec181dfe64b385217894bf4a60cf334709efa4bd28683d26f23552f', 'Rachel Brooks', '97409120', '1979-07-30', 'Female', 0, '2025-05-19 09:19:02', '2025-05-19 09:19:02'),
(87, 'Scott', 'scrypt:32768:8:1$WQPZwWEHPixcqwBV$84244ed4e52d4f56167ff12169f44ee43dab3a9a808f18735a08da97c557f14fb775c877ea9362a7705e759d4513e003f6d57467d5dbe2d511cb8e65c1fa53e0', 'Scott Kelly', '92224585', '1977-03-11', 'Female', 0, '2025-05-19 09:19:27', '2025-05-19 09:19:27'),
(88, 'Maria', 'scrypt:32768:8:1$98Qr0IyOVM4WQKZu$4d2fa603cf4a4d2803910bd9488843a2bedc25ebca37b283e4d8be557a8eb74a34f03fe41bcb8f1f3ed1bcf8057bb0a94f0721ac984716387788ef8b5f57f57c', 'Maria Sanders', '93286860', '1963-09-20', 'Female', 0, '2025-05-19 09:20:26', '2025-05-19 09:20:26'),
(89, 'Brandon', 'scrypt:32768:8:1$yrTX54DatxRCyhex$fcb3cc79f772b868fa5ce5436e4ef14d01c4a23236321fb9b29638af8013f8f79e2b6e7b48fe12c35ab32d930e110d37e247d6cabd3b6ba234b6db6217781c41', 'Brandon Price', '97544783', '1950-11-30', 'Male', 0, '2025-05-19 09:21:01', '2025-05-19 09:21:01'),
(90, 'Heather', 'scrypt:32768:8:1$dtmeq5uoOEB0hIdl$2e6116a036027f8a802f4b950589bab4ef1a2967c2b688a6ed7ee848546d5cfb8f45814c4b47f4ce3f5dc5ea46c3a5fa4eb38921a608fd8ce464e3fb5c550f09', 'Heather Bennett', '97738731', '2003-06-29', 'Female', 0, '2025-05-19 09:21:37', '2025-05-19 09:21:37'),
(91, 'Benjamin', 'scrypt:32768:8:1$EwxtjHjjvwByb7IA$2e4803f75eed0e6ce18d32e82d2b34ba784cab8359b7a8f4451a9efa61c3db1975ae7eca87b0310c7db0032fe39c14ba4e63ba1aaff850bda64def57117111dc', 'Benjamin Wood', '85185720', '1954-12-29', 'Male', 0, '2025-05-19 09:22:07', '2025-05-19 09:22:07'),
(92, 'Diane', 'scrypt:32768:8:1$ixl4DDtxIQeRPJWD$fc9876fb156ff45f3856fd771e5f29f1f2c29d1d3d53bad4aa6b36948f08e9d1ae4aac3ab467ac9461e2417e6a77ae0c3af3763fd88acc4f4c2245f742cae1a0', 'Diane Barnes', '96942565', '2002-08-23', 'Female', 0, '2025-05-19 09:22:33', '2025-05-19 09:22:33'),
(93, 'Samuel', 'scrypt:32768:8:1$unmistqZ3aGJndsD$680ad3bf856781a64bb79609ba0a23d8672ac6d1cced792e2818743b50cfbc1c26ae8da7e11e688ecf251ca521ae1b17474ff352dbd427d3c8297e33a5e6c930', 'Samuel Ross', '84841517', '2001-07-13', 'Male', 0, '2025-05-19 09:23:13', '2025-05-19 09:23:13'),
(94, 'Olivia', 'scrypt:32768:8:1$7CgR7PKBXQZmH3jr$9b957bdc171f8f48eabd65374352a1028413d1b16f2c0a76482d89d1ad6f1e1955a3e52e3fc192d7f8b11b53e9bc5aa25120b0e2c0ddd40a9f40e05e76d206cd', 'Olivia Henderson', '80565395', '1949-11-07', 'Female', 0, '2025-05-19 09:23:44', '2025-05-19 09:23:44'),
(95, 'Gregory', 'scrypt:32768:8:1$2iwsanCexcZP1edh$a4f800a7d645605dc8250a175ed199609054fe8e3abc50242d84756098ffb093ce47a307e2df181ff393b3ff3dce5f893c86ab4ef5451754803921ea752303be', 'Gregory Coleman', '96794515', '1951-07-06', 'Male', 0, '2025-05-19 09:24:11', '2025-05-19 09:24:11'),
(96, 'Frances', 'scrypt:32768:8:1$gxOZiOHNHjK5QmZB$5d39e6318f28bd0fc6e55bbf6993e43f8c2724451a97b8e7573f82a13d9cffa31eb149f82c8edfaee6e032dad4e44fc72cc4d16fc229db0aadc25ab0b0bc2805', 'Frances Jenkins', '96596966', '1945-01-28', 'Female', 0, '2025-05-19 09:24:50', '2025-05-19 09:24:50'),
(97, 'Frank', 'scrypt:32768:8:1$6wooAX6Zyrnr5Gbu$b1f6c000fdc77e40148c3cf8653e8181a4e1e74c15a5498b9527c4b6a1373dae81ad306cef5d7fac3376b2899b364232007f00d4953445444497f0b9cc30b8bd', 'Frank Perry', '97500578', '1957-04-30', 'Male', 0, '2025-05-19 09:25:22', '2025-05-19 09:25:22'),
(98, 'Helen', 'scrypt:32768:8:1$IuqYQOgqXnWE8vQv$f0b1953e554fec4a4ab5c5b38c2aed151f915a9e3f6fbbea9b3ccf59206d98918e2cf5099069cda22e6be4a4b664e3f0d065d73444a823f547d3e5a6da56a54d', 'Helen Powell', '98795043', '1990-07-03', 'Female', 0, '2025-05-19 09:25:52', '2025-05-19 09:25:52'),
(99, 'Alexander', 'scrypt:32768:8:1$bwFk6qXZt05OtmUa$48c19cb2f35314b14a48ca3f65a222fc2421ebdfa1cf43e2779c79e28df3d9a4a8905d07fc9de613f8f5631ef85f4fa0bba3ac0df2a3a52e342303851be134cf', 'Alexander Long', '82272948', '1995-05-22', 'Male', 0, '2025-05-19 09:26:19', '2025-05-19 09:26:19'),
(100, 'Anna ', 'scrypt:32768:8:1$7KmUd5Dtq2piUCEf$98e6cfab9b9abb1580982b35572217e4ec6a1658c03f0e94f53c9cb4a7d4ff23bd4b4065fc5614ebb01db02dfda18ed4676a5fba89ff2f2be56174a323590fe1', 'Anna Patterson', '84116188', '2003-12-07', 'Female', 0, '2025-05-19 09:26:44', '2025-05-19 09:26:44');

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
(4, 'HomeOwner'),
(5, 'HomeOwner'),
(6, 'Platform Management'),
(7, 'Platform Management'),
(8, 'User Admin'),
(9, 'HomeOwner'),
(10, 'Cleaner'),
(11, 'Platform Management'),
(12, 'Platform Management'),
(13, 'Platform Management'),
(14, 'Platform Management'),
(15, 'Platform Management'),
(16, 'Platform Management'),
(17, 'Platform Management'),
(18, 'Platform Management'),
(19, 'Platform Management'),
(20, 'Platform Management'),
(21, 'User Admin'),
(22, 'User Admin'),
(23, 'User Admin'),
(24, 'User Admin'),
(25, 'User Admin'),
(26, 'User Admin'),
(27, 'User Admin'),
(28, 'User Admin'),
(29, 'User Admin'),
(30, 'User Admin'),
(31, 'Cleaner'),
(32, 'Cleaner'),
(33, 'Cleaner'),
(34, 'Cleaner'),
(35, 'Cleaner'),
(36, 'Cleaner'),
(37, 'Cleaner'),
(38, 'Cleaner'),
(39, 'Cleaner'),
(40, 'Cleaner'),
(41, 'Cleaner'),
(42, 'Cleaner'),
(43, 'Cleaner'),
(44, 'Cleaner'),
(45, 'Cleaner'),
(46, 'Cleaner'),
(47, 'Cleaner'),
(48, 'Cleaner'),
(49, 'Cleaner'),
(50, 'Cleaner'),
(51, 'HomeOwner'),
(52, 'HomeOwner'),
(53, 'HomeOwner'),
(54, 'HomeOwner'),
(55, 'HomeOwner'),
(56, 'HomeOwner'),
(57, 'HomeOwner'),
(58, 'HomeOwner'),
(59, 'HomeOwner'),
(60, 'HomeOwner'),
(61, 'HomeOwner'),
(62, 'HomeOwner'),
(63, 'HomeOwner'),
(64, 'HomeOwner'),
(65, 'HomeOwner'),
(66, 'HomeOwner'),
(67, 'HomeOwner'),
(68, 'HomeOwner'),
(69, 'HomeOwner'),
(70, 'HomeOwner'),
(71, 'Cleaner'),
(72, 'Cleaner'),
(73, 'Cleaner'),
(74, 'Cleaner'),
(75, 'Cleaner'),
(76, 'Cleaner'),
(77, 'Cleaner'),
(78, 'Cleaner'),
(79, 'Cleaner'),
(80, 'Cleaner'),
(81, 'Cleaner'),
(82, 'Cleaner'),
(83, 'Cleaner'),
(84, 'Cleaner'),
(85, 'Cleaner'),
(86, 'HomeOwner'),
(87, 'HomeOwner'),
(88, 'HomeOwner'),
(89, 'HomeOwner'),
(90, 'HomeOwner'),
(91, 'HomeOwner'),
(92, 'HomeOwner'),
(93, 'HomeOwner'),
(94, 'HomeOwner'),
(95, 'HomeOwner'),
(96, 'HomeOwner'),
(97, 'HomeOwner'),
(98, 'HomeOwner'),
(99, 'HomeOwner'),
(100, 'HomeOwner');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `service_category`
--
ALTER TABLE `service_category`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `service_matches`
--
ALTER TABLE `service_matches`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `service_views`
--
ALTER TABLE `service_views`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `shortlist`
--
ALTER TABLE `shortlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `user_account`
--
ALTER TABLE `user_account`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

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
