class Solution:
    def calculate(self, s: str) -> int:
        # break s into tokens
        tokens = []
        for ch in s:
            if ch == " ":
                continue
            if ch.isnumeric():
                if tokens and tokens[-1].isnumeric():
                    tokens[-1] += ch
                else:
                    tokens.append(ch)
            else:
                tokens.append(ch)

        # keep track of the active sign with a stack
        sign = [1]
        ans, i = 0, 0
        while i < len(tokens):
            # add/subtract each number to/from the answer 
            # based on the active sign
            if tokens[i].isnumeric():
                ans += int(tokens[i]) * sign[-1]

            elif tokens[i] == '-':
                # same as first if statement, but reversed due to sign
                if tokens[i + 1].isnumeric():
                    ans += -1 * int(tokens[i + 1]) * sign[-1]
                
                # take the active sign and add a flipped version of it 
                # to the top of the active sign stack
                else: # tokens[i + 1] == '('
                    sign.append(sign[-1] * -1)
                i += 1

            elif tokens[i] == ')':
                sign.pop()

            # the operator preceeding this parenthesis was not a negative sign,
            # so add another of the active sign to the top of the sign stack
            elif tokens[i] == '(':
                sign.append(sign[-1])
                
            i += 1
        
        return ans
