Inicialmente, eu tratei o problema apenas como uma contagem de parênteses, dessa maneira:

```python
    class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        aberto = 0
        fechado = 0
        for char in s:
            if char == '(':
                aberto += 1
            elif char == ')':
                fechado += 1

        return aberto + fechado
```

Mas estudei mais e percebi que essa resolução não atendia às regras estabelecidas, contando um par parênteses fechados aninhado dentro de outro como * 2 - (()) -> Esse, por exemplo, teria o valor de 4.

Se trata de um problema de stacks, em que é necessário acompanhar a quantidade de camadas de parênteses. Portanto, o seguinte código foi uma saída melhor

```python
class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]

        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack.pop()

solucao = Solution()
resultado = solucao.scoreOfParentheses("(())")
print(resultado)
```

A linha ```stack.append(0)``` quando um caractere é '(' adiciona um 0 à lista "stack".

Quando char é um caractere '(', a linha ```v = stack.pop()``` tira a camada superior da stack e atribui o valor v, pois a camada se fechou. 

A linha ```stack[-1] += max(2 * v, 1)``` adiciona à última posição da stack o valor de v * 2 (ou 1, caso v seja 0), +1.

Ao fim do loop, é retornado o último valor retirado da pilha, que é o score de caracteres.