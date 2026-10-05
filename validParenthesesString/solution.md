## Anotações

Esse foi meu primeiro leetcode. Consegui resolver as 4 etapas de teste com o código 

```python
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        possible_characters = ['(', ')', '*']
        for characters in s:
            if characters in possible_characters:
                if s == '(' and len(characters) == 1:
                    return False
                return True
```

Porém, ainda assim, ele não atendeu aos requisitos do desafio do dia. Tive que recorrer à IA e então compreendi melhor qual solução poderia adotar:

char |	low	| high |	observação
----|---|---|---
(| 1 |	1	|
*|0|2| * pode ser ), vazio ou (
)	| -1 → 0	| 1	| ajusta low para 0
)| 	-1 → 0	| 0	| high ainda não ficou negativo

## O código final

```python
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = high = 0
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1
            
            if high < 0:
                return False
            low = max(low, 0)
        return low == 0
```