import System.IO
import Control.Monad
import Data.Char

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering 
  
  input_line <- getLine
  let width = read input_line :: Int
  input_line <- getLine
  let height = read input_line :: Int
  t <- getLine
  let text = map toUpper t
  
  replicateM height $ do
    row <- getLine
    let output = map (rowOutput width row) text
    printList output
    putStrLn ""
    return ()
  return ()

printList :: [[Char]] -> IO ()
printList [] = return ()
printList (x:xs) = do
  putStr x
  printList xs

rowOutput :: Int -> String -> Char -> [Char]
rowOutput width row c =
  let p = (ord c) - (ord 'A') in
  if p < 0 || p > 25 then
    rowOutput2 width row c 26
  else
    rowOutput2 width row c p

rowOutput2 :: Int -> String -> Char -> Int -> [Char]
rowOutput2 width row c position = take width $ drop (position * width) row