class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None

    def push(self, val: int) -> None:

        if not self.stack:
            self.stack.append(val)
            self.minVal = val

        elif val >= self.minVal:
            self.stack.append(val)

        else:
            # Store encoded value
            self.stack.append(2 * val - self.minVal)
            self.minVal = val

    def pop(self) -> None:

        if not self.stack:
            return

        top = self.stack.pop()

        # Encoded value
        if top < self.minVal:
            self.minVal = 2 * self.minVal - top

        # Optional: reset when stack becomes empty
        if not self.stack:
            self.minVal = None

    def top(self) -> int:

        top = self.stack[-1]

        if top >= self.minVal:
            return top

        return self.minVal

    def getMin(self) -> int:
        return self.minVal