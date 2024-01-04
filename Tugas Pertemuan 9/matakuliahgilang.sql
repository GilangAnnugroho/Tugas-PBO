-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 04 Jan 2024 pada 09.48
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gilang`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `matakuliahgilang`
--

CREATE TABLE `matakuliahgilang` (
  `id` int(11) NOT NULL,
  `kodemk` varchar(5) NOT NULL,
  `namamk` varchar(15) NOT NULL,
  `sks` enum('1','2','3') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `matakuliahgilang`
--

INSERT INTO `matakuliahgilang` (`id`, `kodemk`, `namamk`, `sks`) VALUES
(1, '321', 'PBO II', '3'),
(2, '322', 'AIK II', '2'),
(3, '323', 'Kalkulus II', '2'),
(4, '324', 'Sistem Informas', '3'),
(5, '325', 'Statistik', '2'),
(6, '326', 'Arsitektur Komp', '3'),
(7, '327', 'Algoritma', '3');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `matakuliahgilang`
--
ALTER TABLE `matakuliahgilang`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kodemk` (`kodemk`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `matakuliahgilang`
--
ALTER TABLE `matakuliahgilang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
