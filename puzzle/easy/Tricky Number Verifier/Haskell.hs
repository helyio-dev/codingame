import Data.Char (isDigit, digitToInt)
import Data.List (splitAt)

isLeapYear :: Int -> Bool
isLeapYear y
  | y `mod` 400 == 0 = True
  | y `mod` 100 == 0 = False
  | y `mod` 4 == 0 = True
  | otherwise = False

isValidDate :: Int -> Int -> Int -> Bool
isValidDate dd mm yy
  | mm < 1 || mm > 12 = False
  | dd < 1 = False
  | mm `elem` [4,6,9,11] && dd > 30 = False
  | mm == 2 && isLeapYear year && dd > 29 = False
  | mm == 2 && not (isLeapYear year) && dd > 28 = False
  | otherwise = dd <= 31
  where year = 2000 + yy

computeCheckDigit :: [Int] -> [Int] -> Int
computeCheckDigit lll ddmmyy =
  let factorsLLL = [3,7,9]
      factorsDDMMYY = [5,8,4,2,1,6]
      products = zipWith (*) lll factorsLLL ++ zipWith (*) ddmmyy factorsDDMMYY
      total = sum products
      remainder = total `mod` 11
  in if remainder == 10 then -1 else remainder

correctNumber :: [Int] -> [Int] -> String
correctNumber lll ddmmyy =
  let check = computeCheckDigit lll ddmmyy
  in if check /= -1
     then concatMap show lll ++ show check ++ concatMap show ddmmyy
     else correctNumber (incrementLLL lll) ddmmyy
  where incrementLLL [a,b,c] = 
          let total = a*100 + b*10 + c + 1
          in [total `div` 100, (total `div` 10) `mod` 10, total `mod` 10]

validate :: String -> String
validate s
  | length s /= 10 = "INVALID SYNTAX"
  | not (all isDigit s) = "INVALID SYNTAX"
  | head (take 3 s) == '0' = "INVALID SYNTAX"
  | otherwise =
      let (lllStr, rest) = splitAt 3 s
          (xStr, ddmmyyStr) = splitAt 1 rest
          lll = map digitToInt lllStr
          x = digitToInt (head xStr)
          ddmmyy = map digitToInt ddmmyyStr
          dd = ddmmyy!!0 * 10 + ddmmyy!!1
          mm = ddmmyy!!2 * 10 + ddmmyy!!3
          yy = ddmmyy!!4 * 10 + ddmmyy!!5
      in if not (isValidDate dd mm yy)
         then "INVALID DATE"
         else let computedX = computeCheckDigit lll ddmmyy
              in if computedX == -1
                 then correctNumber (incrementLLL lll) ddmmyy
                 else if x == computedX
                      then "OK"
                      else correctNumber lll ddmmyy
  where incrementLLL [a,b,c] = 
          let total = a*100 + b*10 + c + 1
          in [total `div` 100, (total `div` 10) `mod` 10, total `mod` 10]

main :: IO ()
main = do
  n <- readLn
  inputs <- sequence (replicate n getLine)
  mapM_ putStrLn (map validate inputs)