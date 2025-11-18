let sum_digits n =
  let rec aux n acc =
    if n = 0 then acc
    else aux (n / 10) (acc + (n mod 10))
  in
  aux n 0

let () =
  let r = read_int () in
  let c = read_int () in
  let t = read_int () in
  
  let visited = Array.make_matrix r c false in
  let queue = Queue.create () in
  let count = ref 0 in
  
  if sum_digits 0 + sum_digits 0 <= t then (
    Queue.add (0, 0) queue;
    visited.(0).(0) <- true;
    count := !count + 1
  );
  
  let directions = [(0, 1); (1, 0); (0, -1); (-1, 0)] in
  
  while not (Queue.is_empty queue) do
    let (x, y) = Queue.take queue in
    
    List.iter (fun (dx, dy) ->
      let nx = x + dx in
      let ny = y + dy in
      
      if nx >= 0 && nx < r && ny >= 0 && ny < c && not visited.(nx).(ny) then
        if sum_digits nx + sum_digits ny <= t then (
          visited.(nx).(ny) <- true;
          Queue.add (nx, ny) queue;
          count := !count + 1
        )
    ) directions
  done;
  
  print_int !count;
  print_newline ()