class Solution:
    def floodFill(self, image, sr, sc, color):

        original_color = image[sr][sc]

        if original_color == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):

            # Outside the grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Not part of the original region
            if image[r][c] != original_color:
                return

            # Change the color
            image[r][c] = color

            # Visit four neighbors
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        dfs(sr, sc)

        return image