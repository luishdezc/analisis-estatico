## Equivalence Partitioning

1\. Function that validates credit card numbers.

- Valid card numbers: Length between 13 and 16 digits, containing only numeric digits.

| Entrada           | Partición             | Resultado esperado |
| ----------------- | --------------------- | ------------------ |
| 1234567890123     | Válida                | Aceptada           |
| 1234567890123456  | Válida                | Aceptada           |
| 123456789012      | Muy corta             | Rechazada          |
| 12345678901234567 | Muy larga             | Rechazada          |
| 1234567890123a    | Letras                | Rechazada          |
| 1234-5678-9012    | Caracteres especiales | Rechazada          |
| ""                | Cadena vacía          | Rechazada          |

2\. Function that validates dates.

- Valid years: Between 1900 and 2100.
- Valid months: Between 1 and 12.
- Valid days: Between 1 and 31.

| Entrada    | Partición                                  | Resultado esperado |
| ---------- | ------------------------------------------ | ------------------ |
| 1900-01-1  | Ninguna                                    | Aceptada           |
| 2100-12-31 | Ninguna                                    | Aceptada           |
| 1899-12-31 | Año menor a 1900                           | Rechazada          |
| 2101-01-1  | Año mayor a 2100                           | Rechazada          |
| 2025-13-10 | Mes mayor a 12                             | Rechazada          |
| 2025-05-0  | Día menor a 1                              | Rechazada          |
| 2025-08-32 | Día mayor a 31                             | Rechazada          |
| 2025-02-30 | Mes que no cuenta con esa cantidad de días | Rechazada          |

3\. Function that checks the eligibility of a passenger to book a flight.

- Eligible ages: Between 18 and 65.
- Frequent flyers: True or False.

| Edad | Viajero frecuente | Partición        | Resultado esperado |
| ---- | ----------------- | ---------------- | ------------------ |
| 17   | True              | Inválida (menor) | No elegible        |
| 18   | False             | Válida           | Elegible           |
| 65   | True              | Válida           | Elegible           |
| 66   | False             | Inválida (mayor) | No elegible        |

4\. Function that validates URLs.

- Valid URLs: Length less than or equal to 255, starting with "http://" or "https://".

| Entrada             | Partición         | Resultado esperado |
| ------------------- | ----------------- | ------------------ |
| http://example.com  | Válida            | Aceptada           |
| https://example.com | Válida            | Aceptada           |
| ftp://example.com   | Prefijo inválido  | Rechazada          |
| 256 caracteres      | Longitud inválida | Rechazada          |
| example.com         | Sin prefijo       | Rechazada          |
| ""                  | Cadena vacía      | Rechazada          |

## Boundary Value Analysis

1\. Function that calculates the eligibility of a person for a loan based on their income and credit score. The eligibility rules are as follows:

- If the income is less than $30,000, the person is not eligible for a loan.
- If the income is between $30,000 and $60,000 (inclusive) and the credit score is above 700, the person is eligible for a standard loan.
- If the income is between $30,000 and $60,000 (inclusive) and the credit score is below or equal to 700, the person is eligible for a secured loan.
- If the income is greater than $60,000 and the credit score is above 750, the person is eligible for a premium loan.
- If the income is greater than $60,000 and the credit score is between 700 and 750 (inclusive), the person is eligible for a standard loan.

| Entrada | Crédito | Resultado esperado |
| ------- | ------- | ------------------ |
| 29,999  | 720     | No elegible        |
| 30,000  | 701     | Préstamo estándar  |
| 59,999  | 701     | Préstamo estándar  |
| 60,000  | 701     | Préstamo estándar  |
| 30,000  | 700     | Préstamo asegurado |
| 59,999  | 700     | Préstamo asegurado |
| 60,000  | 700     | Préstamo asegurado |
| 60,001  | 751     | Préstamo premium   |
| 60,001  | 750     | Préstamo estándar  |

2\. Function that determines the category of a product in an e-commerce system based on its price. The product categories and pricing rules are as follows:

- Category A: Products priced between $10 and $50 (inclusive).
- Category B: Products priced between $51 and $100 (inclusive).
- Category C: Products priced between $101 and $200 (inclusive).
- Category D: Products priced above $200.

| Precio | Categoría esperada |
| ------ | ------------------ |
| 9.9    | Sin categoría      |
| 10     | Categoría A        |
| 49.9   | Categoría A        |
| 50     | Categoría A        |
| 51     | Categoría B        |
| 99.9   | Categoría B        |
| 100    | Categoría B        |
| 101    | Categoría C        |
| 199.9  | Categoría C        |
| 200    | Categoría C        |
| 200.1  | Categoría D        |

3\. Function that calculates the cost of shipping for packages based on their weight and dimensions. The shipping cost rules are as follows:

- If the weight of the package is less than or equal to 1 kg and the dimensions (length, width, and height) are each less than or equal to 10 cm, the cost is $5.
- If the weight is between 1 and 5 kg (inclusive) and the dimensions are each between 11 and 30 cm (inclusive), the cost is $10.
- If the weight is greater than 5 kg or any of the dimensions is greater than 30 cm, the cost is $20.

| Peso | Dimensiones | Resultado esperado |
| ---- | ----------- | ------------------ |
| 0.99 | 9x9x9       | $5                 |
| 1    | 10x10x10    | $5                 |
| 1.01 | 11x11x11    | $10                |
| 4.9  | 29x29x29    | $10                |
| 5    | 30x30x30    | $10                |
| 5.1  | 10x10x10    | $20                |
| 1    | 30.1x15x10  | $20                |

## Decision Table

1\. Create the decision table for a system that provides weather advisories based on temperature and humidity. The rules are:

- Weather recommendation "High temperature and humidity. Stay hydrated." for temperature > 30 and humidity > 70.
- Weather recommendation "Low temperature. Don't forget your jacket!" for temperature < 0 and any humidity.
- No weather recommendation for any other temperature and humidity combination.

| Caso      | C1  | C2  | C3                                            | C4                | C5                                         | C6                                         | C7                | C8  |
| --------- | --- | --- | --------------------------------------------- | ----------------- | ------------------------------------------ | ------------------------------------------ | ----------------- | --- |
| Temp > 30 | V   | V   | V                                             | V                 | F                                          | F                                          | F                 | F   |
| Temp < 0  | V   | V   | F                                             | F                 | V                                          | V                                          | F                 | F   |
| Hum > 70  | V   | F   | V                                             | F                 | V                                          | F                                          | V                 | F   |
| **Aviso** | -   | -   | High temperature and humidity. Stay hydrated. | No recommendation | Low temperature. Don't forget your jacket! | Low temperature. Don't forget your jacket! | No recommendation | -   |

2\. Create the decision table for a system that authenticates users based on their username and password. The rules are:

- Returns "Admin" for username "admin" and password "admin123".
- Returns "User" for any other username with at least 5 characters and password with at least 8 characters.
- Returns "Invalid" if the username or password lenghts are not met.

| Caso                | C1  | C2  | C3    | C4    | C5  | C6  | C7  | C8  | C9  | C10 | C11 | C12 | C13  | C14     | C15     | C16     |
| ------------------- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------- | ------- | ------- |
| username = admin    | V   | V   | V     | V     | V   | V   | V   | V   | F   | F   | F   | F   | F    | F       | F       | F       |
| password = admin123 | V   | V   | V     | V     | F   | F   | F   | F   | V   | V   | V   | V   | F    | F       | F       | F       |
| username >= 5 car.  | V   | V   | F     | F     | V   | V   | F   | F   | V   | V   | F   | F   | V    | V       | F       | F       |
| password >= 8 car.  | V   | F   | V     | F     | V   | F   | V   | F   | V   | F   | V   | F   | V    | F       | V       | F       |
| **Salida esperada** | -   | -   | admin | admin | -   | -   | -   | -   | -   | -   | -   | -   | user | invalid | invalid | invalid |
