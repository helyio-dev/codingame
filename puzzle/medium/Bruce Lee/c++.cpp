#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> split(const string &str, char delimiter)
{
  vector<string> tokens;
  string token;
  istringstream tokenStream(str);

  while (getline(tokenStream, token, delimiter))
  {
    tokens.push_back(token);
  }

  return tokens;
}
int binaryToDecimal(const int *binary)
{
  int decimal = 0;
  int power = 1;

  for (int i = 7 - 1; i >= 0; --i)
  {
    if (binary[i] == 1)
    {
      decimal += power;
    }

    power *= 2;
  }

  return decimal;
}
int invalidInput()
{
  cout << "INVALID" << endl;
  return 0;
}

int main()
{
  string encrypt;
  getline(cin, encrypt);
  vector<string> splitedEncrypt = split(encrypt, ' ');
  int bytes[7] = {0, 0, 0, 0, 0, 0, 0}, countByte = 0;
  string answer = "";
  while (splitedEncrypt.size() >= 2)
  {
    string digit = splitedEncrypt.front();
    splitedEncrypt.erase(splitedEncrypt.begin());

    string nbOccurrence = splitedEncrypt.front();
    splitedEncrypt.erase(splitedEncrypt.begin());

    if (digit != "00" && digit != "0")
    {
      return invalidInput();
    }

    for (int i = 0; i < nbOccurrence.length(); i++)
    {
      if (nbOccurrence[i] != '0')
      {
        return invalidInput();
      }
      bytes[countByte] = digit == "00" ? 0 : 1; 
      countByte++;                             

      if (countByte == 7)
      {
        answer += binaryToDecimal(bytes);
        countByte = 0;
      }
    }
  }

  if (splitedEncrypt.size() != 0 || countByte != 0)
  {
    return invalidInput();
  }

  cout << answer << endl;
}