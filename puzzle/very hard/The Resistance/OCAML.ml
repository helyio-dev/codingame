module StrMap = Map.Make(String) ;;

let map = ref StrMap.empty in

let times m x = if StrMap.mem x m then StrMap.find x m else 0 in

let rec sum = function
| [] -> 0
| (x::l) -> x + sum l in

let rec subs = function
| "" -> []
| x -> if String.length x > 80 then subs (String.sub x 0 80) else x :: subs (String.sub x 0 (String.length x - 1)) in

let br = [".-" ; "-..." ; "-.-." ; "-.." ; "." ; "..-." ; "--." ; "...." ; ".." ; ".---" ; "-.-" ; ".-.." ; "--" ; "-." ; "---" ; ".--." ; "--.-" ; ".-." ; "..." ; "-" ; "..-" ; "...-" ; ".--" ; "-..-" ; "-.--" ; "--.."]
in

let char_to_morse c = List.nth br (int_of_char c - int_of_char 'A') in

let skip_ltr s = String.sub s 1 (String.length s - 1) in

let solve_one s nxt = sum (List.map (fun str -> (times !map str) * (List.nth nxt (String.length str - 1))) (subs s)) in

let rec solve = function
| "" -> [1]
| s -> let nxt = solve (skip_ltr s) in (solve_one s nxt) :: nxt in

let str_to_morse x =
    let rec to_b = function
    | "" -> ""
    | s -> let ch = String.get s 0 in (char_to_morse ch) ^ to_b (skip_ltr s) in to_b x
in

let l = input_line stdin in
let n = int_of_string (input_line stdin) in
for i = 0 to n - 1 do
    let w = str_to_morse (input_line stdin) in
    map := StrMap.add w
        ((if StrMap.mem w !map then StrMap.find w !map else 0)+1) !map
done;
print_int (List.hd (solve l))