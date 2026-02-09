1\. Function that checks if a given number is positive, negative, or zero.

| Entrada | Resultado esperado |
| ------- | ------------------ |
| -5      | Negativo           |
| -1      | Negativo           |
| 0       | Cero               |
| 1       | Positivo           |
| 10      | Positivo           |

2\. Function that validates user passwords.

The password validation rules are as follows:

- The password must be at least 8 characters long.
- The password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (!, @, #, $, %, or \&).

| Contraseña | Falla                   | Resultado esperado |
| ---------- | ----------------------- | ------------------ |
| Abc1@xyz   | Ninguna                 | Válida             |
| abc1@xyz   | Falta letra mayúscula   | Inválida           |
| ABC1@XYZ   | Falta letra minúscula   | Inválida           |
| Abcdef@x   | Falta dígito            | Inválida           |
| Abc12345   | Falta carácter especial | Inválida           |
| Ab1@x      | Menor a 8 caracteres    | Inválida           |

3\. Function that calculates the discount for a customer's purchase based on the total amount.

The discount rules are as follows:

- If the total amount is less than 100, no discount is applied.
- If the total amount is between 100 and 500 (inclusive), a 10% discount is applied.
- If the total amount is greater than 500, a 20% discount is applied.

| Limite          | Valor  | Resultado esperado |
| --------------- | ------ | ------------------ |
| Límite inferior | 99.99  | 0% descuento       |
| Frontera inicio | 100    | 10% descuento      |
| Frontera fin    | 500    | 10% descuento      |
| Límite superior | 500.01 | 20% descuento      |

4\. Function that processes user orders in an e-commerce system.

The function calculates the total price of the items in the order, applying different discounts based on the quantity of each item.

The discount rules are as follows:

- If the quantity of a single item is between 1 and 5 (inclusive), no discount is applied.
- If the quantity of a single item is between 6 and 10 (inclusive), a 5% discount is applied.
- If the quantity of a single item is greater than 10, a 10% discount is applied.

| Rango      | Valor | Resultado esperado |
| ---------- | ----- | ------------------ |
| 1-5        | 5     | 0% descuento       |
| 6-10       | 6     | 5% descuento       |
| 6-10       | 10    | 5% descuento       |
| Mayor a 10 | 11    | 10% descuento      |

5\. Function that calculates shipping costs for an online shopping system.

The function calculates shipping costs based on the total weight of the items in the order and the shipping method chosen by the customer.

The shipping cost rules are as follows:

For standard shipping:

- If the total weight is less than or equal to 5 kg, the cost is $10.
- If the total weight is between 5 and 10 kg (inclusive), the cost is $15.
- If the total weight is greater than 10 kg, the cost is $20.

For express shipping:

- If the total weight is less than or equal to 5 kg, the cost is $20.
- If the total weight is between 5 and 10 kg (inclusive), the cost is $30.
- If the total weight is greater than 10 kg, the cost is $40.

| Metodo   | Peso | Costo esperado |
| -------- | ---- | -------------- |
| Estandar | 5    | $10            |
| Estandar | 7    | $15            |
| Estandar | 10   | $15            |
| Estandar | 11   | $20            |
| Expres   | 5    | $20            |
| Expres   | 8    | $30            |
| Expres   | 10   | $30            |
| Expres   | 12   | $40            |
