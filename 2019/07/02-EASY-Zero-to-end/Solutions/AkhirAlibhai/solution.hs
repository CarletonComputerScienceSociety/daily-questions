moveZeros :: [Int] -> [Int]
moveZeros (h:t)
    | h == 0 = (moveZeros t) ++ [h]
    | otherwise = h:(moveZeros t)
moveZeros _ = []