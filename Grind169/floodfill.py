def floodFill(self, image, sr, sc, color):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type color: int
    :rtype: List[List[int]]
    """
    def dfs(image, r, c, color, startingColor):
        if r > len(image) - 1 or r < 0 or c > len(image[0]) - 1 or c < 0 or image[r][c] != startingColor or image[r][c] == color:
            return image
        image[r][c] = color
        dfs(image, r + 1, c, color, startingColor)
        dfs(image, r - 1, c, color, startingColor)
        dfs(image, r, c + 1, color, startingColor)
        dfs(image, r, c - 1, color, startingColor)
        return image

    startingColor = image[sr][sc]
    return dfs(image, sr, sc, color, startingColor)


    