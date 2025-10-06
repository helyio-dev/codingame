#pragma GCC optimize("O3,inline,omit-frame-pointer,unroll-loops")
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <iomanip>
#include <chrono>
#include <ctime>
#include <thread>
#include <fstream>

#include <stdio.h>    
#include <stdlib.h>    
#include <time.h>       


using namespace std;

float RandomFloat01() {
	return (static_cast <float> (rand()) / static_cast <float> (RAND_MAX));
}

int RandomNumber(int N) {
	return rand() % N + 1;
}

int RandomNumber0(int N) {
	return rand() % N ;
}

class Point {
    public:
	float x;
	float y;
	bool alive;

	float distance2(Point p) {
		return (x - p.x)*(x - p.x) + (y - p.y)*(y - p.y);
	}
	float distance(Point p) {
		return sqrt(distance2(p));
	}
	
	void Move (Point target, float dist) {
	    float d = distance(target);	
        if (d>0) {    
	        x = floor( x + dist * (target.x - x)/d );
	        y = floor( y + dist * (target.y - y)/d );
        }   
	}
	  
     float getAngle(Point p) {
       float d = distance(p);
       float dx = (p.x - x) / d;
       float dy = -(p.y - y) / d;

       float a = atan2(dy,dx)* 57.29577951;
       if (a < 0) { a = 360.0 + a;}
       return a;
     }
    
	
};

class Gene {
public:

	float RotCom;
	int DistCom;

	void SetRandom() {

        RotCom = ( RandomNumber0(359) ) * 0.017453293; 
        DistCom = 900 +  RandomNumber(100);


	}

	Point Command(Point me) {
	    Point p;
	    p.x = floor (me.x + DistCom * cos(RotCom) );
	    p.y = floor (me.y - DistCom * sin(RotCom) );
	    
	    if (p.x < 0) {p.x = 0;}
	    if (p.x > 16000) {p.x = 16000;}
	    if (p.y < 0) {p.y = 0;}
	    if (p.y > 9000) {p.y = 9000;}
	    
		return p;
	}
};





class Game {
    
    public: 
    
    Point me;
    vector<Point> human;
    vector<Point> zombie;
    int score;
    int timeStep;
    
    void Read() {
        
        human.clear();
        zombie.clear();
        
        cin >> me.x >> me.y; cin.ignore();
        
        int humanCount;
        cin >> humanCount; cin.ignore();
                
        for (int i = 0; i < humanCount; i++) {
            Point p;
            int id;
            cin >> id >> p.x >> p.y; cin.ignore();
            p.alive=true;
            human.push_back(p);
        }
        
        int zombieCount;
        cin >> zombieCount; cin.ignore();
        
        for (int i = 0; i < zombieCount; i++) {
            Point p;
            int id;
            cin >> id >> p.x >> p.y >> id >> id; cin.ignore();
            p.alive=true;
            zombie.push_back(p);
        }   
    }

    void Write() {
              
        cerr << me.x << " " << me.y << endl;
        cerr << human.size() << endl;
        for (Point h : human) {
            cerr << "0 " << h.x << " " << h.y << endl;
        }
        cerr << zombie.size() << endl;
        for (Point z : zombie) {
            cerr << "0 " << z.x << " " << z.y << " 0 0 " << endl;
        }
    }

    void FakeRead() {
        int dummy;
        
        cin >> dummy >> dummy; cin.ignore();
        
        int humanCount;
        cin >> humanCount; cin.ignore();
                
        for (int i = 0; i < humanCount; i++) {
            cin >> dummy >> dummy >> dummy; cin.ignore();
        }
        
        int zombieCount;
        cin >> zombieCount; cin.ignore();
        
        for (int i = 0; i < zombieCount; i++) {
            cin >> dummy >> dummy >> dummy >> dummy >> dummy; cin.ignore();
        }   
    }
    
    
    void playAturn(Gene g) {

        float zombieStepSize = 400.0;
        for (Point& z : zombie) {
            Point target = me;
            float minDist = z.distance2(me);
            for (Point h : human) {
                float dist = z.distance2(h);
                if (dist < minDist) {
                    minDist = dist;
                    target = h;
                }
            }
            minDist = min(sqrt(minDist),zombieStepSize);

            z.Move(target,minDist);

        }

        me = g.Command(me);
        
        vector<Point> oldzombie = zombie;
        int nKill = 0;
        zombie.clear();
        for (Point z : oldzombie) {
            if (z.distance2(me)>4000000) { zombie.push_back(z); 
            } else {
                nKill++;    
            }
        }

        int fa = 0, fb = 1, f;        
        for (int i=0; i<nKill; i++) {
            f = fa + fb;
            fa = fb;
            fb = f;

            score = score + 10*pow(human.size(),2)*f;
        }
        

        vector<Point> oldhuman = human;
        human.clear();
        for (Point h : oldhuman) {
            for (Point z : zombie) {
                if (z.x == h.x & z.y == h.y) {
                    h.alive=false;
                }
            }
            if (h.alive==true) {
                human.push_back(h);    
            }
        }
        if (human.size() == 0) {score = 0; }
        
    }
    
    void sendCommand(Gene g) {
        Point target = g.Command(me);
        cout << (int) target.x << " " <<  (int) target.y << endl;
    }
};



class Chromosome : public Gene {
public:
	vector<Gene> genes;
	float objF;
	float fitness;
	float probability;
	float cumProb; 
	int nSteps;

	void EvaluateObjF(Game game) {

        int i = game.timeStep;
        while (game.human.size()>0 & game.zombie.size()>0) {
            game.playAturn(genes[i]);            
			i++;
        }
		
		nSteps = i-1;
		objF = game.score;
		
		
	}
	void EvaluateFitness() {
		fitness = (1.0 + objF); 
	}

};

class Population : public Chromosome {
public:
	vector<Chromosome> chromosomes;
	float totalFitness;
	int Ngenes;
	int Nchron;
	float CrossOverRate;
	float MutationRate;
	int MutationNumber;
	int niter;

	void EvaluteTotalFintess() {
		totalFitness = 0.0;
		for (Chromosome c : chromosomes) {
			totalFitness += c.fitness;
		}
	}

	void EvaluateMutationNumber() {
		MutationNumber = (int)((chromosomes.size() * chromosomes[0].genes.size()) * MutationRate);
	}


	void GenerateInitialPopulation() {
		for (int i = 0; i < Nchron; i++) {
			Chromosome cro;
			for (int j = 0; j < Ngenes; j++) {
				Gene gen;
				gen.SetRandom();
				cro.genes.push_back(gen);
			}
			chromosomes.push_back(cro);
		}
	}

	Chromosome EvaluatePopulation(Game game) {
		float maxObjF = -1.0E10;
		Chromosome best;
		for (Chromosome &c : chromosomes) {
			c.EvaluateObjF(game);
			if (c.objF >= maxObjF) { maxObjF = c.objF; best = c; }
		}
		return (best);
	}
};


void ga(Population &pop, float time, Game game, Chromosome &bestBest) {

	std::clock_t c_start = std::clock();
	std::clock_t c_end = std::clock();
	float maxTime = time * CLOCKS_PER_SEC / 1000.0;

    cerr << "pop.niter" << endl;
	Chromosome best = pop.EvaluatePopulation(game);
    cerr << "pop.niter" << endl;
	if (best.objF > bestBest.objF) { bestBest = best; }

	pop.niter = 0;
	while (c_end - c_start < maxTime) {
		pop.niter++;
      
		for (Chromosome &c : pop.chromosomes) {
			c.EvaluateFitness();
		}
		pop.EvaluteTotalFintess();

		float cp = 0.0;
		for (Chromosome &c : pop.chromosomes) {
			c.probability = c.fitness / pop.totalFitness;
			cp = cp + c.probability;
			c.cumProb = cp;
		}

		Population newPop = pop;
		newPop.chromosomes.clear();

		for (int j = 0; j < pop.chromosomes.size(); j++) { 
			float r = RandomFloat01();
			for (int i = 0; i < pop.chromosomes.size(); i++) {
				if (r <= pop.chromosomes[i].cumProb) {
					newPop.chromosomes.push_back(pop.chromosomes[i]);
					break;
				}
			}
		}

		pop = newPop;
		newPop.chromosomes.clear();

		for (Chromosome c : pop.chromosomes) {
			float r = RandomFloat01();
			if (r<pop.CrossOverRate) { 
				Chromosome cro;
				int ata = RandomNumber(pop.chromosomes.size()) - 1;
				for (int i = 0; i < c.genes.size(); i++) {  
					if (RandomFloat01() < 0.5) {
						cro.genes.push_back(c.genes[i]);  
					}
					else {
						cro.genes.push_back(pop.chromosomes[ata].genes[i]);  
					}
				}
				newPop.chromosomes.push_back(cro);
			}
			else { 
				newPop.chromosomes.push_back(c);
			}
		}

		pop = newPop;
		newPop.chromosomes.clear();

		pop.EvaluateMutationNumber();
		for (int i = 0; i < pop.MutationNumber; i++) {  
			int cr = RandomNumber(pop.chromosomes.size()) - 1;
			int ge = RandomNumber(pop.chromosomes[0].genes.size()) - 1; 
			pop.chromosomes[cr].genes[ge].SetRandom();
		}


		best = pop.EvaluatePopulation(game);
		if (best.objF > bestBest.objF) { bestBest = best; }

		c_end = clock();
	}
};


int main()
{
	srand(time(NULL));    
    Game game;
    game.score = 0;
	game.timeStep = 0;


	Population pop;

	pop.Ngenes = 100;
	pop.Nchron = 150;
	pop.CrossOverRate = 0.25;
	pop.MutationRate = 0.02;
	float timems = 135.0; 

	pop.GenerateInitialPopulation();

	Chromosome best;
	best.objF = -1.0E10;
	best.nSteps = 1;
    
    while (1) {

        game.timeStep++;
        if (game.timeStep==1) {
            game.Read(); 
          
            float minD=1.0E10;
            Point target;
            for (Point h : game.human) {
                float d = game.me.distance(h);
                if (d<minD) {minD=d; target = h;}
            }

            for (Gene& g : pop.chromosomes[0].genes) {
                g.RotCom=game.me.getAngle(target)/180.0*3.141592;
                g.DistCom=1000.0;
            } 
        
          
        } else {game.FakeRead(); }
        
		ga(pop, timems, game, best);
                    
        game.sendCommand(best.genes[game.timeStep]);

        game.playAturn(best.genes[game.timeStep]);
        
        cerr << "nz " << game.zombie.size() << " nh " << game.human.size() << " s " << game.score << " of " << best.objF  << endl;
      
    }
}