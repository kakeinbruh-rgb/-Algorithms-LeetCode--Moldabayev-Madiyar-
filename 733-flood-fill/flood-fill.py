class Solution:
    def floodFill(self, image, sr, sc, color):
        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]

        # если цвет уже такой же — ничего делать не надо
        if start_color == color:
            return image

        def dfs(r, c):
            # проверка выхода за границы и цвета
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != start_color:
                return

            # красим пиксель
            image[r][c] = color

            # идем в 4 направления
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image