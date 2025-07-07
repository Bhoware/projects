#include<iostream>

using namespace std;
            
            void Board (char board[3][3]){
            	
            	for(int i=0;i<3;i++){
            		for(int j=0;j<3;j++){
            			cout<<board[i][j];
            			if(j<2){
            				cout<<"  |";
            							
						}
						
					}
					cout<<"\n";
					if(i<2){
            				cout<<" --+---+-- \n";
				}
			}
		}
		bool win(char board[3][3],char player){
			for(int i=0;i<3;i++){
				
				if(board[i][0]==player&&
				   board[i][1]==player&&
				   board[i][2]==player)
				   
				   return true;
				
				if(board[0][i]==player&&
				   board[1][i]==player&&
				   board[2][i]==player)
				   
				   return true;
				
			}
			if(    board[0][2]==player&&
				   board[1][1]==player&&
				   board[2][0]==player)
				   
				   return true;
				
				if(board[0][0]==player&&
				   board[1][1]==player&&
				   board[2][2]==player)
				   
				   return true;
				
				return false;
		}
			int main(){
				
				cout<<"**TIC TAC TOE**\n";
				
				char board[3][3]{ 
				{' ',' ',' ',},
				{' ',' ',' ',},
				{' ',' ',' ',}
			};
				
				int row,col;
				
				     char player='x';
				     
				     int moves=0;
				   while(true){
				   	
						
				Board(board);
									 		  				
				cout<<"Enter coordinates  :  ";
				     cin>>row>>col;
				     if(row>=0 && row<3 && col>=0 && col<3){
				     	if(board[row][col]==' '){
				     	 	board[row][col] =player;
				     	 	moves++;
				    	 	//cout<<board[row][col];
				     	 	if(win(board,player)){
				     	 		cout<<player<<"\t"<<"Wins !";
				     	 		break;
							  }
							  if(moves==9){
							  	cout<<"IT'S A DRAW ! ";
							  	break;
							  }
				     	 	if(player=='x'){
				      	player='o';
					  }else{
					  	player='x';
					  }
				     	 	
					 }else{
					  	cout<<"spot already taken!\n";
						  }
						 
					 }
					 
				Board(board);
		}
				   }
