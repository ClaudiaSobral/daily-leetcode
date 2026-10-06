Esse problema gira em torno de saber quantos parênteses precisamos adicionar a s para que s seja válido (ou seja, todos os parênteses fechem).

A resposta é um número.

Eu iniciei com a solução mais simples, que resolveu 45 de 116 testcases, mas minha solução não considerava ordem, que é importante para esse teste.

```python
    class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_parentheses = closed_parentheses = 0

        for char in s:
            if char == '(':
                open_parentheses += 1
            else:
                closed_parentheses +=1
        
        if open_parentheses != closed_parentheses:
            score = abs(open_parentheses - closed_parentheses)
            return score
        else:
            return 0
```


Achei que teria de recorrer a uma stack, mas uma variável simples resolveu o problema.

```python
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_parentheses = 0        # Inicializa a contagem de parentêses
        res = 0                     # Inicializa o resultado

        for char in s:
            if char == '(':
                open_parentheses += 1       # Adiciona um a contagem de parentêses abertos
            else:
                open_parentheses -=1        # Decresce um a contagem de parentêses abertos quando identifica um parêntese fechado
                if open_parentheses < 0:        # Cada vez que a contagem de parênteses fica desbalanceada, open_parentheses volta a 0 e adiciona-se 1 a res, como se fosse a contagem de parênteses abertos que sobram
                    open_parentheses = 0
                    res += 1

        return open_parentheses + res # Soma-se open_parentheses a res para ter a contagem de parenteses que precisam ser fechados
```