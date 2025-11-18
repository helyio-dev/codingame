import System.IO
import Control.Monad
import Data.Sequence (Seq, (|>), ViewL(..), viewl, empty, singleton)
import Data.IntMap (IntMap)
import qualified Data.IntMap as IntMap

s :: Int -> Int
s 0 = 0
s n = (n `mod` 10) + s (n `div` 10)

type Coords = (Int, Int)
type Visited = IntMap Bool

directions :: [Coords]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

toIndex :: Int -> Coords -> Int
toIndex maxC (r, c) = r * maxC + c

inBounds :: Int -> Int -> Coords -> Bool
inBounds maxR maxC (r, c) = r >= 0 && r < maxR && c >= 0 && c < maxC

solve :: Int -> Int -> Int -> Int
solve maxR maxC threshold
    | s 0 + s 0 > threshold = 0
    | otherwise = go initialQueue initialVisited 1
    where
        startNode = (0, 0)
        initialQueue = singleton startNode
        initialVisited = IntMap.singleton (toIndex maxC startNode) True

        go queue visited count =
            case viewl queue of
                EmptyL -> count
                (x, y) :< restQueue ->
                    let
                        neighbors =
                            [ (nx, ny)
                            | (dx, dy) <- directions
                            , let nx = x + dx
                            , let ny = y + dy
                            , inBounds maxR maxC (nx, ny)
                            , IntMap.notMember (toIndex maxC (nx, ny)) visited
                            , s nx + s ny <= threshold
                            ]
                        (newQueue, newVisited, newCount) =
                            foldr
                                (\coord (q, v, c) ->
                                    (q |> coord, IntMap.insert (toIndex maxC coord) True v, c + 1)
                                )
                                (restQueue, visited, count)
                                neighbors
                    in
                    go newQueue newVisited newCount

main :: IO ()
main = do
    hSetBuffering stdout NoBuffering

    input_line <- getLine
    let r = read input_line :: Int
    input_line <- getLine
    let c = read input_line :: Int
    input_line <- getLine
    let t = read input_line :: Int

    let result = solve r c t
    print result
    return ()