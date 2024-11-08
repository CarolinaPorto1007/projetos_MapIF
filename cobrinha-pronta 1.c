#include <stdio.h>
#include <stdlib.h>
#include <windows.h> // system("cls")
#include <conio.h> // não foi utilizada nessa versão
#include<time.h> // rand(time())


const int altura = 20;
const int largura = 50;
char m[20][50]; // matriz para realizar as funções que precisam de coordenadas
char direcao,sentido,comecar;



struct posicao { // apenas as coordenadas 
    int cordx, cordy;
};

struct No { // coordenadas e o pronteiro para o proximo nó 
    struct posicao dado;
    struct No* prox;
};


struct posicao maca;

void criar_cenario();
void inserir(struct posicao ca);
void gerar_maca();
char movimento_cobra(char Direcao, char Sentido);
void movimento_corpo();
void imprimir_cenario();
char snake_game();
void game_over();
void jogo_finalizado();


struct No* cabeca_cobra = NULL, * cauda_cobra = NULL; //ponteiro para a cabeça e a cauda da cobra

int main() {


    int x, y; 
    int pontos=0;
    struct posicao cabeca = { 9,24 }, cauda = { 9,25 }; // criação da cobra (ainda não ta na matriz)
    inserir(cabeca);
    inserir(cauda);

    criar_cenario();
    gerar_maca();
    criar_cenario();
    
     
    
    sentido= 'A';

    if(snake_game() == 'c'){ // retorna o char para o jogo começar depois das instruções 

    

    while(1){ // loop game ( o loop vai acabar quando o usuario bater nas paredes ou no corpo da cobra e ainda se quiser sair do jogo ele digita a tecla x)

        criar_cenario();
        system("cls");
        imprimir_cenario();

        printf("Instrunções: w- Para cima / s- Para baixo / a- Para esquerda / d- Para direita / x- Para sair do jogo\n");
        printf("Digite a direção escolhida:");
        scanf("%c", &direcao); 
        

        sentido = movimento_cobra(direcao, sentido); // recebe o sentido atualizado para a cobra se movimentar 

        if(direcao == 'x'){
            jogo_finalizado();
            break;
        }

       
        if(cabeca_cobra->dado.cordx== maca.cordx && cabeca_cobra->dado.cordy == maca.cordy){ // lógica do jogo se a cobra comer a maçã 
            gerar_maca();
            pontos++;
            if(sentido == 'W'){
                x=cauda_cobra->dado.cordx++;
                y=cauda_cobra->dado.cordy;

            }
            else if (sentido == 'S'){
                x=cauda_cobra->dado.cordx--;
                y=cauda_cobra->dado.cordy;

            }
            else if (sentido == 'A'){
                x=cauda_cobra->dado.cordx;
                y=cauda_cobra->dado.cordy++;

            }
            else{
                x=cauda_cobra->dado.cordx;
                y=cauda_cobra->dado.cordy--;

            }
            struct posicao coords={x,y}; // envia as coordenadas sempre atualizadas 

            inserir(coords);

        } 

        else if(m[cabeca_cobra->dado.cordx][ cabeca_cobra->dado.cordy] == '#'){ // lógica se a cobra bater nas paredes
            game_over();
            printf("PONTOS FINAIS:");
            printf("%d",pontos);

            break;
        }

        else if(m[cabeca_cobra->dado.cordx][ cabeca_cobra->dado.cordy] == 'o'){ // lógica se a cobra comer o corpo
           game_over();
           printf("PONTOS FINAIS:");
           printf("%d",pontos);
            break; 
        }
        
    }
 }
    

    return 0;
}


void inserir(struct posicao ca) {  // criando a cobra (lista para formar a cobra)
    struct No* novo = (struct No*)malloc(sizeof(struct No));
    novo->dado = ca;
    novo->prox = NULL;

    if (!cabeca_cobra)
        cabeca_cobra = cauda_cobra = novo;
    else {
        //cauda_cobra->prox=novo;
        novo->prox=cauda_cobra;
        cauda_cobra = novo;
    }
}

void criar_cenario() { // juntando tudo no cenário criado

    // inicializa a matriz do cenário
    for (int i = 0; i < 20; i++) {
        for (int j = 0; j < 50; j++) {
            if (j == 0 || j == largura - 1) { //preenchendo as duas colunas das laterais
                m[i][j] = '#';
            }
            else if (i == 0 || i == altura - 1) {
                m[i][j] = '#';
            }
            else {
                m[i][j] = ' ';
            }
        }
    }

    // iniciarlizar a cobra

    struct No* aux = cauda_cobra;

    while (aux) {
        if (aux == cabeca_cobra) {
            m[cabeca_cobra->dado.cordx][cabeca_cobra->dado.cordy] = 'O';
        }
        else {
            m[aux->dado.cordx][aux->dado.cordy] = 'o';
        }
        aux = aux->prox;
    }

    //maça
    m[maca.cordx][maca.cordy] = 'C';

}


void imprimir_cenario() { // imprime o cenário real do jogo
    for (int i = 0; i < 20; i++) {
        for (int j = 0; j < 50; j++) {
            printf("%c", m[i][j]);
        }
        printf("\n");
    }

}

void gerar_maca() {
    int a = largura - 1, b = altura - 1;
    srand(time(NULL));
    do {
        maca.cordx = rand() % (a); //gerando a maçã aleatoriamente na cordx
        maca.cordy = rand() % (b); //gerando a maçã aleatoriamente na cordy
    } while (m[maca.cordx][maca.cordy] != ' '); // recalcula pra caso o espaço não possa ocupado
}

char movimento_cobra(char Direcao, char Sentido){  // argumentos enviados para gerar a direção e o sentido que a cobra pode ir 

// DIREÇÃO(usuário informa)-> w= cima; s= baixo; a= esquerda; d= direita
// SENTIDO(indica a posição da cobra antes de ser digitada a direção)-> W-cima, S-baixo, A-esquerda, D-direita

    if(Direcao=='w' && Sentido!= 'S'){
        movimento_corpo();
        cabeca_cobra->dado.cordx--;
        Sentido= 'W';
    }

    else if(Direcao== 's' && Sentido!= 'W'){
        movimento_corpo();
        cabeca_cobra->dado.cordx++;
        Sentido= 'S';
    }

    else if(Direcao== 'a' && Sentido !='D'){
        movimento_corpo();
        cabeca_cobra->dado.cordy--;
        Sentido= 'A';
    }

    else if(Direcao== 'd' && Sentido!='A'){
        movimento_corpo();
        cabeca_cobra->dado.cordy++;
        Sentido= 'D';
    }
    return Sentido;
}


void movimento_corpo(){  
    struct No *aux= cauda_cobra;

    while(aux!=cabeca_cobra){ // percorrendo a minha lista da cauda até um elemento antes da cebaça
        aux->dado.cordx=aux->prox->dado.cordx; // atualiza as coordenadas de x do proximo elemento
        aux->dado.cordy=aux->prox->dado.cordy; // atualiza as coordenadas de y do proximo elemento
        aux=aux->prox;
    }

 }

 char snake_game(){

    
printf("          ________  ________   ________  ___  __    _______       \n");
printf("         |\\   ____\\|\\   ___  \\|\\   __  \\|\\  \\|\\  \\ |\\  ___ \\         \n");
printf("  ___     \\ \\  \\___|\\ \\  \\ \\  \\ \\  \\|\\  \\ \\  \\/  /|\\ \\   __/|         \n");
printf(" |\\__\\     \\ \\_____  \\ \\  \\ \\  \\ \\   __  \\ \\   ___  \\ \\  \\_|/__  \n");
printf(" \\|__|      \\|____|\\  \\ \\  \\ \\  \\ \\  \\ \\  \\ \\  \\ \\  \\ \\  \\_|\\ \\      \n");
printf("              ____\\_\\  \\ \\__\\ \\__\\ \\__\\ \\__\\ \\__\\ \\__\\ \\_______\\     \n");
printf("              |\\_________\\|__| \\|__|\\|__|\\|__|\\|__| \\|__|\\|_____|    \n");
printf("              \\|_________|                                              \n");

printf("\n");

printf(" ________  ________  _____ ______   _______                            \n");
printf("|\\   ____\\|\\   __  \\|\\   _ \\  _   \\|\\  ___ \\                           \n");
printf("\\ \\  \\___|\\ \\  \\|\\  \\ \\  \\\\__\\ \\  \\ \\   __/|          ___             \n");
printf(" \\ \\  \\  __\\ \\   __  \\ \\  \\|__| \\  \\ \\  \\_|/__       |\\__\\       \n");
printf("  \\ \\  \\|\\  \\ \\  \\ \\  \\ \\  \\    \\ \\  \\ \\  \\_|\\ \\     \\|__|            \n");
printf("   \\ \\_______\\ \\__\\ \\__\\ \\__\\    \\ \\__\\ \\_______\\                      \n");
printf("    \\|_______|\\|__|\\|__|\\|__|     \\|__|\\|_______|                     \n");




printf("\n\n\n");

printf("BEM VINDO AO JOGO DA COBRINHA!!\n");
printf("SABE JOGAR?\n");
printf("INSTRUNÇÕES PARA O MOVIMENTO DA SUA COBRINHA:  w- Para cima / s- Para baixo / a- Para esquerda / d- Para direita / x- Para sair do jogo\n");
printf("COMO FUNCIONA?\n");
printf("SE A COBRINHA BATER NA PAREDE OU A COBRA COMER O SEU CORPO O JOGO ACABA (GAME OVER)\n");
printf("SE DESEJAR ENCERRAR O JOGO DIGITE A TECLA x\n");


printf("\n\n");




printf("           /^\\ /^\\    \n");
printf("         _|__|  O|     \n");
printf("\\/     /~     \\_/ \\     \n");
printf(" \\____|__________/  \\     \n");
printf("        \\_______      \\    \n");
printf("                `\\     \\                 \\    \n");
printf("                  |     |                  \\     \n");
printf("                 /      /                    \\     \n");
printf("                /     /                       \\     \n");
printf("              /      /                         \\ \\    \n");
printf("             /     /                            \\  \\    \n");
printf("           /     /             _----_            \\   \\    \n");
printf("          /     /           _-~      ~-_         |   |     \n");
printf("         (      (        _-~    _--_    ~-_     _/   |     \n");
printf("          \\      ~-____-~    _-~    ~-_    ~-_-~    / \n");
printf("             ~-_           _-~          ~-_       _-~    \n");
printf("               ~--______-~                ~-___-~    \n");

printf("DIGITE C PARA JOGAR!");
scanf("%c",&comecar);

return comecar;
 }


void game_over(){

    
printf("            _____          __  __ ______    ______      ________ _____                \n");
printf("           / ____|   /\\   |  \\/  |  ____|  / __ \\ \\    / /  ____|  __ \\               \n");
printf("  ______  | |  __   /  \\  | \\  / | |__    | |  | \\ \\  / /| |__  | |__) |  ______      \n");
printf(" |______| | | |_ | / /\\ \\ | |\\/| |  __|   | |  | |\\ \\/ / |  __| |  _  /  |______|    \n");
printf("          | |__| |/ ____ \\| |  | | |____  | |__| | \\  /  | |____| | \\ \\               \n");
printf("           \\_____/_/    \\_\\_|  |_|______|  \\____/   \\/   |______|_|  \\_\\              \n");

printf("\n\n\n");



printf("           /^\\ /^\\    \n");
printf("         _|__|  O|     \n");
printf("\\/     /~     \\_/ \\     \n");
printf(" \\____|__________/  \\     \n");
printf("        \\_______      \\    \n");
printf("                `\\     \\                 \\    \n");
printf("                  |     |                  \\     \n");
printf("                 /      /                    \\     \n");
printf("                /     /                       \\     \n");
printf("              /      /                         \\ \\    \n");
printf("             /     /                            \\  \\    \n");
printf("           /     /             _----_            \\   \\    \n");
printf("          /     /           _-~      ~-_         |   |     \n");
printf("         (      (        _-~    _--_    ~-_     _/   |     \n");
printf("          \\      ~-____-~    _-~    ~-_    ~-_-~    / \n");
printf("             ~-_           _-~          ~-_       _-~    \n");
printf("               ~--______-~                ~-___-~    \n");


}


void jogo_finalizado(){
    
printf("                _  ____   _____  ____      ______ _____ _   _          _      _____ ______         _____   ____                \n");
printf("               | |/ __ \\ / ____|/ __ \\    |  ____|_   _| \\ | |   /\\   | |    |_   _|___  /   /\\   |  __ \\ / __ \\               \n");
printf("  ______       | | |  | | |  __| |  | |   | |__    | | |  \\| |  /  \\  | |      | |    / /   /  \\  | |  | | |  | |  ______      \n");
printf(" |______|  _   | | |  | | | |_ | |  | |   |  __|   | | | . ` | / /\\ \\ | |      | |   / /   / /\\ \\ | |  | | |  | | |______|     \n");
printf("          | |__| | |__| | |__| | |__| |   | |     _| |_| |\\  |/ ____ \\| |____ _| |_ / /__ / ____ \\| |__| | |__| |              \n");
printf("           \\____/ \\____/ \\_____|\\____/    |_|    |_____|_| \\_/_/    \\_\\______|_____/_____/_/    \\_\\_____/ \\____/              \n");

}



/*void logica(){
    int x, y;
    if(cabeca_cobra->dado.cordx== maca.cordx && cabeca_cobra->dado.cordy == maca.cordy){
        gerar_maca();
        if(Sentido == 'W'){
            x=cauda_cobra->dado.cordx++;
            y=cauda_cobra->dado.cordy;

        }
        else if (Sentido == 'S'){
            x=cauda_cobra->dado.cordx--;
            y=cauda_cobra->dado.cordy;

        }
        else if (Sentido == 'A'){
            x=cauda_cobra->dado.cordx;
            y=cauda_cobra->dado.cordy++;

        }
        else{
            x=cauda_cobra->dado.cordx;
            y=cauda_cobra->dado.cordy--;

        }
        struct posicao coords={x,y};

        inserir(coords);

     } 

     else if(m[cabeca_cobra->dado.cordx][ cabeca_cobra->dado.cordy] == '#'){
        printf("GAME OVER!!!");
        break;
     }

 
        
}
*/