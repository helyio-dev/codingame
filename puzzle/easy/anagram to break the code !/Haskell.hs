import System.IO
import Control.Monad
import Data.List
import Data.Char

isAnagram :: String -> String -> Bool
isAnagram w1 w2 = 
    let s1 = map toLower w1
        s2 = map toLower w2
    in s1 /= s2 && sort s1 == sort s2

clean :: String -> String
clean = map (\c -> if isLetter c then c else ' ')

main :: IO ()
main = do
    hSetBuffering stdout NoBuffering
    
    w <- getLine
    s <- getLine
    
    let ws = words (clean s)
    
    case findIndex (isAnagram w) ws of
        Nothing -> putStrLn "IMPOSSIBLE"
        Just i -> do
            let (before, keyAndAfter) = splitAt i ws
                after = tail keyAndAfter
                d1 = i `mod` 10
                d2 = length after `mod` 10
                d3 = sum (map length before) `mod` 10
                d4 = sum (map length after) `mod` 10
            putStrLn $ intercalate "." (map show [d1, d2, d3, d4])