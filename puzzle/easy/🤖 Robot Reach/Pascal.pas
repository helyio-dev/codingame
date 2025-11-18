program Answer;

function sumDigits(n: Integer): Integer;
var
  s: string;
  i, sum: Integer;
begin
  str(n, s);
  sum := 0;
  for i := 1 to Length(s) do
    sum := sum + (Ord(s[i]) - Ord('0'));
  sumDigits := sum;
end;

var
  R, C, T: Integer;
  visited: array of array of Boolean;
  queue: array of array[0..1] of Integer;
  count, front, rear: Integer;
  directions: array[0..3, 0..1] of Integer;
  i, x, y, nx, ny, dx, dy: Integer;
begin
  ReadLn(R);
  ReadLn(C);
  ReadLn(T);
  
  SetLength(visited, R, C);
  for x := 0 to R-1 do
    for y := 0 to C-1 do
      visited[x][y] := False;
  
  SetLength(queue, R * C);
  front := 0;
  rear := 0;
  count := 0;
  
  if (sumDigits(0) + sumDigits(0) <= T) then
  begin
    queue[rear][0] := 0;
    queue[rear][1] := 0;
    rear := rear + 1;
    visited[0][0] := True;
    count := count + 1;
  end;
  
  directions[0][0] := 0; directions[0][1] := 1;
  directions[1][0] := 1; directions[1][1] := 0;
  directions[2][0] := 0; directions[2][1] := -1;
  directions[3][0] := -1; directions[3][1] := 0;
  
  while front < rear do
  begin
    x := queue[front][0];
    y := queue[front][1];
    front := front + 1;
    
    for i := 0 to 3 do
    begin
      dx := directions[i][0];
      dy := directions[i][1];
      nx := x + dx;
      ny := y + dy;
      
      if (nx >= 0) and (nx < R) and (ny >= 0) and (ny < C) and (not visited[nx][ny]) then
      begin
        if (sumDigits(nx) + sumDigits(ny) <= T) then
        begin
          visited[nx][ny] := True;
          queue[rear][0] := nx;
          queue[rear][1] := ny;
          rear := rear + 1;
          count := count + 1;
        end;
      end;
    end;
  end;
  
  WriteLn(count);
end.