#include <iostream>
#include <string>

std::string nextGrowing( std::string p_num ) {

    for ( int c1 = p_num.size() -1; c1 >= 0; c1-- ) {

        if ( p_num[c1] != '9' ) {
            p_num[c1]++;
            for ( int c2 = c1 + 1; c2 < p_num.size(); c2++ ) {
                p_num[c2] = '0';
            }
            break;
        }

        if ( c1 == 0 ) {
            for ( int c2 = 0; c2 < p_num.size(); c2++ ) {
                p_num[c2] = '0';
            }
            p_num.insert(0, 1, '1');
        }
    }

    char  l_cur{ p_num[0] };
    bool  l_did{ false    };
    for ( auto& c : p_num ) {
        if ( c < l_cur || l_did ) { c = l_cur; l_did = true;  }
        l_cur = c;
    }

    return p_num;
}

int main()
{
    std::string N;
    std::getline(std::cin, N);

    std::cout << nextGrowing(N) << std::endl;
}
