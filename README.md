Trabalho N2 da matéria de desenvolvimento web, do curso de segurança da informação.

pequeno quiz sobre segurança de dados. 

usuário: root
senha: root

porta de comunicação: 8000

O jogo inicialmente possuí 15 questões sobre segurança de dados, onde ao final do quiz e mostrada sua pontuação.

Com o usuário 'root', é possível cadastrar novas perguntas, alterá-las ou deletá-las. ainda, tem acesso a gestão de usuarios e penguntas, sabendo quantidades de acertos e numero de vezes que as questões foram respondidas e acertadas.

link do container: https://hub.docker.com/r/1rodrigo/quizsec_webv1.0


CASO O CONTAINER NÂO FUNCIONE
*resito ter o python3 instalado na máquina

Cole os arquivos disponibilizados em uma nova pasta
abra um novo terminal nessa pasta e dê o comando
"python3 -m venv venv"

isso criará um novo ambiente virtual, com um próprio interpretador do python.
Apos, digite: .\venv\Scripts\activate (no Windows) ou
              source venv/bin/activate (no Linux)

use o servidor web nativo do python, digitando: python manage.py runserver

a partir de agora, a página estará disponível para o acesso em ser navegador,
na barra de endereço do navegador digite: localhost:8000

para encerrar o servidor web, na janela do terminal que ficou aberta, dê um "CTRL+C".


para ter acesso a administração do site, vá em: localhost:8000/admin
e use:

usuario: root
senha: root

para ter acesso total ao banco de dados.

vídeo com demonstração do site: https://youtu.be/iJPwmOYd8_k
