CREATE PARTITION FUNCTION NutrientsPartitionFunction(INT)
AS RANGE LEFT FOR VALUES(50, 100);

CREATE PARTITION SCHEME NutrientsPartitionScheme
AS PARTITION NutrientsPartitionFunction
TO (Nutrients_PrimaryFG, Nutrients_SecondaryFG1, Nutrients_SecondaryFG1_2);

CREATE TABLE Cheese (
  cheeseID NUMERIC PRIMARY KEY,
  Type NVARCHAR(25),
  Calories NUMERIC(5,3),
  Proteins NUMERIC(5,3),
  Carbohidrates NUMERIC(5,3),
  Fat NUMERIC(5,3)
) ON NutrientsPartitionScheme(cheeseID);