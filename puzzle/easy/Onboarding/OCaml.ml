while true do
    let enemy1 = input_line stdin in
    let dist1 = int_of_string (input_line stdin) in
    let enemy2 = input_line stdin in
    let dist2 = int_of_string (input_line stdin) in
    
    if dist1 < dist2 then
        print_endline enemy1
    else
        print_endline enemy2;
    ();
done;
