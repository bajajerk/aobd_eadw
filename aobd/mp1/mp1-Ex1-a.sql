CREATE DATABASE NutrientsDB
ON PRIMARY Nutrients_PrimaryFG (
  NAME = "NutrientsFG1",
  FILENAME = "D:\Nutrients\NutrientsFG1.mdf",
  SIZE = 50MB,
  MAXSIZE = 1GB,
  FILEGROWTH = 5MB
),
FILEGROUP Nutrients_SecondaryFG1
(
  NAME = Nutrients_SecondaryFG1_1,
  FILENAME = "D:\Nutrients\Nutrients_SecondaryFG1_1.ndf",
  SIZE = 100MB,
  MAXSIZE = UNLIMITED,
  FILEGROWTH = 50%
),
(
  NAME = Nutrients_SecondaryFG1_2,
  FILENAME = "D:\Nutrients\Nutrients_SecondaryFG1_2.ndf",
  SIZE = 50MB,
  MAXSIZE = UNLIMITED,
  FILEGROWTH = 50%
),
(
  NAME = Nutrients_SecondaryFG1_3,
  FILENAME = "D:\Nutrients\Nutrients_SecondaryFG1_3.ndf",
  SIZE = 50MB,
  MAXSIZE = UNLIMITED,
  FILEGROWTH = 50%
),
FILEGROUP Nutrients_SecondaryFG2
(
  NAME = Nutrients_SecondaryFG2_1,
  FILENAME = "D:\Nutrients\Nutrients_SecondaryFG2_1.ndf",
  SIZE = 50MB,
  MAXSIZE = UNLIMITED,
  FILEGROWTH = 50%
),
(
  NAME = Nutrients_SecondaryFG2_2,
  FILENAME = "D:\Nutrients\Nutrients_SecondaryFG2_2.ndf",
  SIZE = 50MB,
  MAXSIZE = UNLIMITED,
  FILEGROWTH = 50%
),
(
  NAME = Nutrients_SecondaryFG2_3,
  FILENAME = "D:\Nutrients\Nutrients_SecondaryFG2_3.ndf",
  SIZE = 50MB,
  MAXSIZE = UNLIMITED,
  FILEGROWTH = 50%
),
LOG ON (
  NAME = "Logfile",
  FILENAME = "D:\NutrientsLog\Logfile.ldf",
  SIZE = 25MB,
  MAXSIZE = 250MB,
  FILEGROWTH = 50%
);