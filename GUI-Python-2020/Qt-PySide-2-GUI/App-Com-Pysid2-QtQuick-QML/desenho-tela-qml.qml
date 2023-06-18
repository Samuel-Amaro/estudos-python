/*desenhando uma tela com o a linguagem QML
# é uma linguagem declarativa que permite desenvolver aplicativos mais rapidamente do que com as linguagens tradicionais. É ideal para projetar a interface do usuário de seu aplicativo devido à sua natureza declarativa. Em QML, uma interface de usuário é especificada como uma árvore de objetos com propriedades.

# Um aplicativo PySide2 / QML consiste, pelo menos, em dois arquivos diferentes - um arquivo com a descrição QML da interface do usuário e um arquivo python que carrega o arquivo QML. 
*/
/*DESENHANDO UMA TELA DE TESTE COM QML*/

/*DESENHANDO UMA TELA DE TESTE COM QML*/

import QtQuick 2.0
/*um modulo qml*/

/*desenhando um retangulo*/
Rectangle {
       width: 200 /*largura*/
       height: 200 /*altura*/
       color: "green" /*uma cor*/
       /*e dentro do retangulo vai ter um texto, isso e o retangulo e pai do componentente de texto*/
       Text {
           text: "Ola Mundo" /*texto*/
           anchors.centerIn: parent /*o texto vai estar centralizado em relaçaõ ao seu componente pai imediato no caso o retangulo*/
       }
}
