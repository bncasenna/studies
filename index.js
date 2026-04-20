 
    function analisarNumeros() {
     num1 = 0; num2 = 0; num3 = 0; num4 = 0; num5 = 0;
        let num1 =parseInt(prompt("Digite o primeiro número."));
        let num2 =parseInt(prompt("Digite o segundo número."));
        let num3 =parseInt(prompt("Digite o terceiro número."));
        let num4 =parseInt(prompt("Digite o quarto número."));
        let num5 =parseInt(prompt("Digite o quinto número."));
    
        alert(`A soma total dos números é ${num1 + num2 + num3 + num4 + num5}`);
        }
        
let pares = [];
if (num1 % 2 === 0) pares.push(num1);
if (num2 % 2 === 0) pares.push(num2);
if (num3 % 2 === 0) pares.push(num3);
if (num4 % 2 === 0) pares.push(num4);
if (num5 % 2 === 0) pares.push(num5); 

 alert(`Você digitou numeros pares: ${pares.join(", ")}`);
        